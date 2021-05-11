import cv2
def selfie(frame):
    local = 'faces/c1.png'
    cv2.imwrite(local,frame)
    return local