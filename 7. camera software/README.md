# Raspberry pi 4 setup guides

<img src="https://github.com/MakerBay/Coral_Reef_Mapping_Drone/blob/master/7.%20camera%20software/raspberrypi4-640x353.jpg" width=400>


## Connect camera to Raspberry pi 4
[![Setup Rasberry pi4](https://github.com/MakerBay/Coral_Reef_Mapping_Drone/blob/master/7.%20camera%20software/cam%20setup.PNG)](https://www.youtube.com/watch?v=0hrF8Wq8SSQ&t=190s")
### Steps
1. Connect Camera Module
2. Enable Camera Interface
3. Capture videos and images

## Guides to take photos and videos with Raspberry pi 4

[![coding for camera](https://github.com/MakerBay/Coral_Reef_Mapping_Drone/blob/master/7.%20camera%20software/cam%20code%20raspberry%20pi4.PNG)](https://www.youtube.com/watch?v=T8T6S5eFpqE&t=172s")

### Coding Steps
* taking a photo: rapistill -o image.jpg
* take a 10 seconds video : raspivid -o video.h264 -t 10000

### Tips
"image" is the name of the photo 
* "10000" is in miliseconds so 10000 is 10 seconds
* "video.h264" is the name of the video

# Editing Photos in Lightroom

### How to Edit Underwater Photos in Lightroom 
* White Balancing the image 
  * Using the White Balance Selector tool, estimate the ‘Temp’ and ‘Tint’ sliders to fine tube the image until it has a natural look without any colour cast
* Correct the Exposure 
  * Using the Exposure slider, adjust the individual light levels of the ‘highlights’, ‘shadows’, ‘whites’ and ‘blacks’ sliders
* Colour Correction through HSL (general instructions)
  * Since we are working with underwater images, use Blue, Aqua, purple and yellow mostly
  * Saturate the blue and push Aqua closer to blue 
  * Increase the hue of the aqua, yellow and green channels
  * Decrease it in the blue purple channels 
  * Adjust luminescence of each colour depending on the photo itself
* Manual Cleanup (This step is optional as it isn’t recommended to have brush tools inserted into Batch edits)
  * Make local adjustments such as using a radial filter to create a focus on the desired area of the image 
  * Make further adjustments such sharpening it 
* Export final image
  * It is important to note that all these individual specific steps are dependable on the image itself
  
### Short video tutorial
Here is a video tutorial to show and explain in details how the editing goes. It is simple and basic so that even complete beginners in Lightroom can do it. 
[![Tutorial video](https://github.com/MakerBay/Coral_Reef_Mapping_Drone/blob/master/7.%20camera%20software/photo_edit_screenshot.jpg)](https://www.youtube.com/watch?v=nOCerZy6DG4)
  
### How to Batch Edit Photos in Lightroom 
* Highlight the photo which contains all the edits that you want to apply to the other images
* Select the multiple photos you want to edit as well and sync the changes (Settings —> Sync Settings)
* Check the settings you want to sync and enter 
* Changes should now be applied to all photos selected 

### How to stitch images
* Software used for stitching is webODM (https://webodm.net/) 
* Add all images and make sure lighting is consistent
* Render 3d and 2d images
