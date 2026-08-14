import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self, modelo, fuente_video, umbral_confianza):
        self.modelo = YOLO(modelo)
        self.fuente_video = fuente_video
        self.umbral_confianza = umbral_confianza