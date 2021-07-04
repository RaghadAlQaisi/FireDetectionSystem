# USAGE
# python capture.py

### Takes snapshots of camera stream then save it and adds timestamp amd location to image metadata

# Imports
import config
import os
import cv2
import time
from datetime import datetime
from iptcinfo3 import IPTCInfo
from pathlib import Path
import multiprocessing
import requests
from slugify import slugify

def capture(camera):
    """ Capture and save snapshots from camera feed """

    image_dir = config.SNAPSHOTS_PATH
    camera_name = slugify(camera['name'])
    camera_location = camera['location']
    camera_id = str(camera['id'])
    images_folder = os.path.join(image_dir,camera_name)
    Path(images_folder).mkdir(parents=True, exist_ok=True) # Create directory if doesn't exist

    cap = cv2.VideoCapture(camera_location) # To capture frame from webcam
    
    # start_time_1min measures 1 minute
    start_time_1min = time.time() - 59  # Subtract 59 seconds for start grabbing first frame after one second (instead of waiting a minute for the first frame).

    while cap.isOpened():
        ret, frame = cap.read()
        if (ret != True):
            break

        cur_time = time.time()  # Get current time
        elapsed_time_1min = cur_time - start_time_1min  # Time elapsed from previous image saving

        # Capture snapshot each 1 second
        if elapsed_time_1min >= 1:
            start_time_1min = cur_time # Reset the timer

            # Save frame to path
            timestamp =  str(datetime.now().strftime("%Y%m%dT%H%M%S,%f")) # Get current Timestamp
            image_name = timestamp + ".jpeg"
            image_path = os.path.join(images_folder,image_name)
            cv2.imwrite(image_path, frame)
            print("Snapshot taken: {}".format(timestamp))

            # Write timestamp and location to 'Tags' section in proprties 
            info = IPTCInfo(image_path, force=True)
            info['keywords'] = [timestamp, camera_id]
            info.save()

            # Wait.. but WHY?!
            # cv2.waitKey(1)


if __name__ == '__main__':

  # Get cameras from API
  API_URL = config.API_URL
  cam = requests.get(API_URL + '/camera/all') 
  cameras = cam.json()
  print('Cameras: {}'.format(cameras))

  # Run capture for all cameras in parallel
  pool = multiprocessing.Pool(processes=len(cameras))
  pool.map(capture, cameras)
  
