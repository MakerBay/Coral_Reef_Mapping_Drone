# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

from __future__ import print_function

import os
import json

import flask
from flask import request
import base64

import tensorflow as tf
import numpy as np
import cv2
from yolov4.tf import YOLOv4

yolo = YOLOv4(tiny=True)

prefix = '/opt/ml/'

model_path = os.path.join(prefix, 'model')

WEIGHTS_FILE = os.path.join(model_path, "yolov4-tiny-custom_final.weights")
CONFIF_FILE = os.path.join(model_path, "yolov4-tiny-custom.cfg")
NAMES_FILE = os.path.join(model_path, "obj.names")

yolo.classes = NAMES_FILE
yolo.make_model()
yolo.load_weights(WEIGHTS_FILE, weights_type="yolo")

# The flask app for serving predictions
app = flask.Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    status = 200
    return flask.Response(response='OK\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    """Do an inference on a single batch of data. In this sample server, we take data as CSV, convert
    it to a pandas data frame for internal use and then convert the predictions back to CSV (which really
    just means one prediction per line, since there's a single column.
    """

    def detect(original_image):
        resized_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        resized_image = yolo.resize_image(resized_image)
        # 0 ~ 255 to 0.0 ~ 1.0
        resized_image = resized_image / 255
        # input_data == Dim(1, input_size, input_size, channels)
        input_data = resized_image[np.newaxis, ...].astype(np.float32)

        candidates = yolo.model.predict(input_data)

        _candidates = []
        for candidate in candidates:
            batch_size = candidate.shape[0]
            grid_size = candidate.shape[1]
            _candidates.append(
                tf.reshape(
                    candidate, shape=(1, grid_size * grid_size * 3, -1)
                )
            )
        # candidates == Dim(batch, candidates, (bbox))
        candidates = np.concatenate(_candidates, axis=1)

        # pred_bboxes == Dim(candidates, (x, y, w, h, class_id, prob))
        pred_bboxes = yolo.candidates_to_pred_bboxes(candidates[0])
        pred_bboxes = yolo.fit_pred_bboxes_to_original(
            pred_bboxes, original_image.shape
        )

        return pred_bboxes

    data = request.get_data()
    image = np.fromstring(data, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(image)
    bboxes = detect(image)
    result = list(map(lambda bbox: {'x': bbox[0], 'y': bbox[1], 'width': bbox[2], 'height': bbox[3], 'class_id': bbox[4], 'confidence': bbox[5]}, bboxes))
    return flask.Response(response=json.dumps(result), status=200, mimetype='application/json')
