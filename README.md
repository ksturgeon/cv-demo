### Background ###
Provides a similar demonstration to Ian Downard’s Facial Recognition post in blogs ([https://mapr.com/blog/dynamic-scaling-computer-vision-pub-sub-messaging-docker/](https://mapr.com/blog/dynamic-scaling-computer-vision-pub-sub-messaging-docker/) ) and the MapR public demo repo ([https://github.com/mapr-demos/mapr-streams-mxnet-face](https://github.com/mapr-demos/mapr-streams-mxnet-face) ).  That demo has certain limitations to making it transportable:
* It requires GPUs due to the mxnet/tensorflow/CUDA libraries used.
* It requires the web capture client run inside a container, inside of a Linux VM on the user’s laptop due to device mapping limitations with Docker for Mac.

**App Lariat Demo ([http://git.se.corp.maprtech.com/ksturgeon/cv-demo](http://git.se.corp.maprtech.com/ksturgeon/cv-demo))**
Consists of four major components;
**1. Client.**  The client runs a small python script (capture-camera-to-dag-db.py) that;
Captures webcam (either built in or USB web camera) frames at a given rate (default of one every 2 seconds to save resources).
* Serializes the captured frame as a string and writes to MapR-DB using the 6.1 lightweight maprdb-python-client (OJAI client for MapR-DB JSON).
**2. Cluster.** The cluster hosts three entities;
* The MapR-DB table listed above (/demo-tables/raw-images), which has Change Data Capture turned on.
* A stream:topic called “/demo-streams/dbchanges:topic1”
* A stream:topic called “/demo/streams/processed-images:topic1”
**3. Image Processor.**  The Edge Node is running a script (stream-face-detect.py) that;
* Waits for a message to be produced to the “/demo-streams/dbchanges” stream.  This stream is populated by CDC messages from the “/demo-tables/raw-images” table.
* Deserializes the image into the proper format to run a very simple facial recognition routine.
* Draws a green square around the recognized face(s).
* Writes the original image, the marked image, and the number of faces to a new stream called “/demo-streams/processed-images”.
**4. Processed Image Viewer.**  A small script (myflask.py) that runs on the Edge node that;
* Listens for HTTP requests on port 5010.
* Responds with the “processed” image JPEG so you can see it in your browser.

**Environment Setup.  Your Mac needs some prerequisites.**
**1. Stable Python 2.7 environment.**  Either native or via condas/anaconda.  I used Anaconda Navigator ([https://docs.anaconda.com/anaconda/navigator/](https://docs.anaconda.com/anaconda/navigator/)) to build a python 2.7 environment I enable using conda command “source activate <name>” where <name> is the environment I built. 
* Install the following packages to the environment (sudo pip install):
scipy, numpy, opencv-python


