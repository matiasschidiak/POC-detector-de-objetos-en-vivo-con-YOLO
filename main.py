from detector import Detector


detector = Detector(
    modelo="yolo11n.pt",
    fuente_video=0,
    umbral_confianza=0.5
)

detector.ejecutar()