# import the necessary packages
import os

# initialize the path to the fire and non-fire dataset directories
FIRE_PATH = os.path.sep.join(["Datasets", "Fire"])
NON_FIRE_PATH = os.path.sep.join(["Datasets", "NonFire"])

# initialize the class labels in the dataset
CLASSES = ["Non-Fire", "Fire"]

# define the size of the training and testing split
TRAIN_SPLIT = 0.75
TEST_SPLIT = 0.25

# define the initial learning rate, batch size, and number of epochs
INIT_LR = 1e-2
BATCH_SIZE = 64
NUM_EPOCHS = 50

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join(["Model", "detection_network.model"])

# define the path to the output learning rate finder plot and
# training history plot
LRFIND_PLOT_PATH = os.path.sep.join(["Model", "lrfind_plot.png"])
TRAINING_PLOT_PATH = os.path.sep.join(["Model", "training_plot.png"])

# define the path to the output directory that will store our final
# output with labels/annotations along with the number of iamges to
# sample
SNAPSHOTS_PATH = os.path.sep.join(["Output", "Camera_Snapshots"])
OUTPUT_FIRE_PATH =  os.path.sep.join(["Output", "Fire_Images"])
OUTPUT_NONFIRE_PATH =  os.path.sep.join(["Output", "NonFire_Images"])

## Database
DATABAE_PATH = os.path.sep.join(["Database", "sqlite_db.db"])

# API
API_URL='http://localhost:5000'
