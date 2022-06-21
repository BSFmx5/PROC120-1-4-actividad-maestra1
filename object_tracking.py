import cv2
import time
import math


video = cv2.VideoCapture("bb3.mp4")

# Cargar raestreador 
tracker = cv2.TrackerCSRT_create()

# Lee el primer fotograma del vídeo
returned, img = video.read()

# Selecciona el cuadro delimitador de la imagen
bbox = cv2.selectROI("Rastreando", img, False)

# Inicializa el rastreador en el img y el cuadro delimitador
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Rastreando",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


def goal_track(img, bbox):
    
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    #Comenzar aquí
    

while True:
    
    check, img = video.read()   

    # Actualiza el rastreador en el img y el cuadro delimitador
    success, bbox = tracker.update(img)

    # Llama drawBox()
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Perdiste",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    # Llamma goal_track()
    

    # Muestra el video
    cv2.imshow("resultado", img)


    # Sal de la ventana de visualización cuando se pulsa la tecla de la barra espaciadora        
    key = cv2.waitKey(25)
    if key == 32:
        print("Detenido")
        break

video.release()
cv2.destroyALLwindows()
