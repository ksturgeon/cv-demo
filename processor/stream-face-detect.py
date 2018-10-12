import cv2 
import sys 
import time 
import datetime 
import json 
import base64

from confluent_kafka import Consumer, KafkaError
import numpy as np

# Get user supplied values
#imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

""" 
Removing the original read from file - replacing with a Streams consumer
# Read the image
image = cv2.imread(imagePath)
"""
c = Consumer({'group.id': 'mygroup',
              'default.topic.config': {'auto.offset.reset': 'earliest'}})
c.subscribe(['/demo-streams/dbchanges:topic1'])
running = True
while running:
  msg = c.poll(timeout=1.0)
  if msg is None: continue
  if not msg.error():
    # Replace the simple receiver with the streams consumer
    # Get the message and pull off the image field
    # Load as a json document, retrieve image element and decode from base64
    nparr = np.fromstring(base64.b64decode(json.loads(msg.value())['$$document']['image']), np.uint8)
    img = cv2.imdecode(nparr, 1)
    image = cv2.imencode('.jpg', img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
      gray,
      scaleFactor=1.1,
      minNeighbors=5,
      minSize=(30, 30)
    )
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
      cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #  Write processed image
    with open('test.jpg', 'wb') as f_output:
      f_output.write(image)
  elif msg.error().code() != KafkaError._PARTITION_EOF:
    print(msg.error())
    running = False
c.close()



