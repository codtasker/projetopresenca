import key
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
# This key will serve all examples in this document.
KEY = key.key
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = key.endpoint
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def detecao(img):
    test_image_array = glob.glob(img)
    imagem = open(test_image_array[0], 'r+b')
    detected_faces = face_client.face.detect_with_stream(imagem, detection_model='detection_03')
    if not detected_faces:
        raise Exception('sem rostos para treinar')
    print('rostos treinados')
    for face in detected_faces: print (face.face_id)
    first_image_face_ID = detected_faces[0].face_id
    test_image_array2 = glob.glob('faces/sebastiao.jpg')
    imagem2 = open(test_image_array[0], 'r+b')
    detected_faces2 = face_client.face.detect_with_stream(imagem2, detection_model='detection_03')
    second_image_face_IDs = list(map(lambda x: x.face_id, detected_faces2))
    similar_faces = face_client.face.find_similar(face_id=first_image_face_ID, face_ids=second_image_face_IDs)
    if not similar_faces:
        print('No similar faces found')
    else:print('sebastião detectado')
    