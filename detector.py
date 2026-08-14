import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self, modelo, fuente_video, umbral_confianza):
        self.modelo = YOLO(modelo)
        self.fuente_video = fuente_video
        self.umbral_confianza = umbral_confianza

    def procesar_frame(self, frame):
        resultados = self.modelo(
            frame,
            conf=self.umbral_confianza
        )

        frame_procesado = resultados[0].plot()

        return frame_procesado

    def ejecutar(self):
        camara = cv2.VideoCapture(self.fuente_video)

        if not camara.isOpened():
            raise RuntimeError("No se pudo abrir la fuente de video")

        try:
            while True:
                correcto, frame = camara.read()

                if not correcto:
                    break

                frame_procesado = self.procesar_frame(frame)

                cv2.imshow("Deteccion", frame_procesado)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        finally:
            camara.release()
            cv2.destroyAllWindows()