import key
import asyncio
import glob
import os
import sys
import time
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
import dbconnect as db
# This key will serve all examples in this document.
KEY = key.key
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = key.endpoint
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def nfl(fl):
    print("o person group criado foi: ", fl)
    face_client.face_list.create(face_list_id= fl,name= fl)

def nr(nome,fl):
    local = "faces/" + nome[0] + "*.jpg"
    image = glob.glob(local)
    foto = open(image[0], 'r+b')
    pessoa = face_client.face_list.add_face_from_stream(fl, foto)
    pes = pessoa.persisted_face_id
    db.alunonovo(nome,pes,"1")
    return pessoa

def dfl(nome):
    face_client.face_list.delete(face_list_id=nome)
    print("delete")

def detecao(img,facelist):
    test_image_array = glob.glob(img)
    imagem = open(test_image_array[0], 'r+b')
    detected_faces = face_client.face.detect_with_stream(imagem, detection_model='detection_03')
    rostos = []
    print("here2")
    for face in detected_faces:
        print(face.face_id)
        rostos.append(face.face_id)
    results = face_client.face.find_similar(rostos[0], face_list_id= facelist)
    print(results)
    if not results:
        print('no comento')
    for persistent in results:
        print("here")
        db.retornome(persistent.persisted_face_id)