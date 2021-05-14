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
    
    