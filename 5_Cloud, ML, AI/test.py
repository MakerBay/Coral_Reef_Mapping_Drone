import json
import boto3
import numpy as np
import cv2

runtime = boto3.Session().client('runtime.sagemaker', region_name='us-east-2')

with open("coral.jpg", "rb") as f:
    payload = bytearray(f.read())

response = runtime.invoke_endpoint(EndpointName="coralbot", ContentType='application/x-image', Body=payload)
result = response['Body'].read()
pred_bboxes = json.loads(result)

original_image = cv2.imread("/Users/utkarsh/dev/LFSEEC/ml/coral.jpg")

for box in pred_bboxes:
  height, width = original_image.shape[:2]
  x,y,w,h,cl,co = box['x']*width, box['y']*height, box['width']*width, box['height']*height, box['class_id'], box["confidence"]
  start_point = (int(x-w/2), int(y-h/2))
  end_point = (int(x+w/2), int(y+h/2))
  cv2.rectangle(original_image,start_point, end_point,(0,255,0),3)
  # original_image = cv2.rectangle(original_image, start_point, end_point, color=(255,0,0), thickness=2)

cv2.imshow("image", original_image)
cv2.waitKey(0)