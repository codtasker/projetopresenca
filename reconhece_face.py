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

def npg(Id):
    PERSON_GROUP_ID = Id
    print("o person group criado foi: ", PERSON_GROUP_ID)
    face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

def np(nome,persongroup):
    pessoa = face_client.person_group_person.create(persongroup, nome)
    local = "faces/" + nome[0] + "*.jpg"
    pessoa_imagens = [file for file in glob.glob(local)]
    for image in pessoa_imagens:
        foto = open(image, 'r+b')
        face_client.person_group_person.add_face_from_stream(persongroup, pessoa.person_id, foto)
    face_client.person_group.train(persongroup)
    while (True):
        training_status = face_client.person_group.get_training_status(persongroup)
        print("Training status: {}.".format(training_status.status))
        print()
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            face_client.person_group.delete(person_group_id=persongroup)
            sys.exit('Training the person group has failed.')
        time.sleep(5)

def dpg(nome):
    face_client.person_group.delete(person_group_id=nome)
    print("delete")

def detecao(img,persongroup):
    test_image_array = glob.glob(img)
    imagem = open(test_image_array[0], 'r+b')
    detected_faces = face_client.face.detect_with_stream(imagem, detection_model='detection_03')
    rostos = []
    for face in detected_faces:
        rostos.append(face.face_id)
    results = face_client.face.identify(rostos, persongroup)
    for person in results:
        print(person.candidates[0].confidence)

    
