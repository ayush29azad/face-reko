import cv2
import os
from google.cloud import pubsub_v1
import face_recognition


credentials_path = 'ace-forest-354809-eea35b1c5b06.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/ace-forest-354809/topics/Face_Det'

img = cv2.imread("images/owner.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]  
img2 = cv2.imread("test.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
if result==[True]:
    data = "Face-Recognsed Welcome to Your Car !!!!"
else:
     data = "Face Not Recognised Please Try Again !!"

data = data.encode('utf-8')


future = publisher.publish(topic_path, data)
print(f'published message id {future.result()}')

