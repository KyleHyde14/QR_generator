import os 
import time

def deleteQR():
    route = 'static/images/'

    if len(os.listdir(route)) >= 1:
        for elem in os.listdir(route):
            QRroute = os.path.join(route, elem)
            creation = os.path.getctime(QRroute)
            if time.time() - creation >= 7200:
                os.remove(QRroute)

def execute_delete():
    waiting = 21600

    while True:
        deleteQR()
        time.sleep(waiting)
