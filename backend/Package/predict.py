# USAGE
# python predict.py

# Imports
import config
from tensorflow.keras.models import load_model
from imutils import paths
import numpy as np
import imutils
import cv2
import os
from iptcinfo3 import IPTCInfo
from pathlib import Path
from skimage import io
import requests


def verify_image(img_file):
	""" Check if image is not corrupt """
	try:
			img = io.imread(img_file)
	except:
			return False
	return True


def create_image(label, image_name, image_data, old_info):
	""" Create new image based on prediction """

	if label == "Fire" :
		output_dir = config.OUTPUT_FIRE_PATH
	else:
		output_dir = config.OUTPUT_NONFIRE_PATH

	# Write new image
	image = os.path.sep.join([output_dir, image_name])
	cv2.imwrite(image, image_data)

	# Write metadata
	info = IPTCInfo(image, force=True)
	info['keywords'] = old_info	
	info['caption/abstract'] = label
	info.save()

	return image


def predict(images):
	""" Run prediction on a list of images """

	# Loop over the sampled image paths
	for (i, image_path) in enumerate(images):

			# Get image name
			image_name = os.path.split(image_path)[-1] # Image name
			if (verify_image(image_path)): # Check if image is not corrupt
				
				# load the image and clone it	
				image = cv2.imread(image_path)
				image_copy = image.copy()

				# Extract the timestamp of every image before resizing it
				info_org = IPTCInfo(image_path, force=True)
				keywords_org = info_org['Keywords']
				
				# resize the input image to be a fixed 128x128 pixels, ignoring aspect ratio
				image = cv2.resize(image, (128, 128))
				image = image.astype("float32") / 255.0
					
				# make predictions on the image
				preds = model.predict(np.expand_dims(image, axis=0))[0]
				j = np.argmax(preds)
				label = config.CLASSES[j]
				
				# draw the prediction on the output frame
				text = label if label == "Non-Fire" else "WARNING! Fire!"
				output = imutils.resize(image_copy, width=500)
				cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,
					1.25, (0, 255, 0), 5)

				# Create predicted image
				image_new = create_image(label, image_name, output, keywords_org)
				if image_new:
					print("Created prediction on image: {}".format(image_name))

				# Create alert and post to API if Fire
				if label == "Fire":
					info_new = IPTCInfo(image_new, force=True)
					timestamp = info_new['keywords'][0].decode("utf-8")
					camera_id = info_new['keywords'][1].decode("utf-8")
					alert = {
						"timestamp": timestamp, 
						"cameraId": camera_id, 
						"image": image_new
						}
					resp = requests.post('http://localhost:5000/alert/create', json=alert)
					resp_json = resp.json()
					print("WARNING FIRE!! Alert #{} at {}".format(resp_json['id'], timestamp))

				# Delete original image, no longer needed
				os.remove(image_path)
			
			# Break loop if image are corrupt
			else:
				break

	# Return `True` when done
	return True


# Main
if __name__ == '__main__':

	# Create output paths
	Path(config.OUTPUT_NONFIRE_PATH).mkdir(parents=True, exist_ok=True) # Create directory if doesn't exist
	Path(config.OUTPUT_FIRE_PATH).mkdir(parents=True, exist_ok=True) # Create directory if doesn't exist

	# load the trained model from disk
	print("[INFO] loading model...")
	model = load_model(config.MODEL_PATH)

	# Run prediction on all images in the snapshot directory
	print("[INFO] predicting...")
	while True:
		image_paths = list(paths.list_images(config.SNAPSHOTS_PATH))
		predict(image_paths)

