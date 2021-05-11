import cv2
import foto as f
import reconhece_face as rc
#declarando as coisas
c = 0
#coisas relacionasdas ao cv2
video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#iniciando a classe reconhece_face

#rc.treino('faces/sebastiao.jpg')
#while para gerar um video com varios frames
while True:
    #lendo a camera e guardando numa variavel
    ret, frame = video_capture.read()
    #transformando a imagem em tons de ciza para o tracking de rostos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #inicio do tracking
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    #verifica a quantidade de pessoas num fame
    try:
        if c < faces.shape[0]: 
            print(faces.shape[0])
            c = faces.shape[0]
            f.selfie(frame)
            rc.detecao('faces/c1.png')
    except: c = 0
    #cria retangulos nas imagens
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #exibe o frame
    cv2.imshow('video', frame)
    #tecla q para sair do app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#destruindo as janelas e dados captados pelo cv2
video_capture.release()
cv2.destroyAllWindows()
#antes do programa 7 - 8 % de cpu
#depois do programa 45 - 50 % de cpu
#cada pessoa varia de 5 - 10 % de cpu
#teste feito com i7-8565U
#faces.shape[0] retorna a quantidade de faces na cena