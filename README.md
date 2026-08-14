# POC-detector-de-objetos-en-vivo-con-YOLO


Proyecto de detección de objetos en tiempo real utilizando YOLO de Ultralytics y OpenCV.

## Requisitos

- Python 3.10 o superior
- Cámara web

## Instalación

Clonar el repositorio:

    git clone https://github.com/matiasschidiak/POC-detector-de-objetos-en-vivo-con-YOLO.git

Entrar en la carpeta:

    cd POC-detector-de-objetos-en-vivo-con-YOLO

Crear un entorno virtual:

    python -m venv .venv

Activar el entorno virtual en Windows:

    source .venv\Scripts\activate

Instalar las dependencias:

    pip install -r requirements.txt

## Ejecución

Ejecutar el programa:

    python main.py

El programa utilizará la cámara principal del equipo y realizará la detección de objetos en tiempo real.

Presionar `Q` para cerrar el programa.

## Configuración

La configuración se encuentra en `main.py`:

    detector = Detector(
        modelo="yolo11n.pt",
        fuente_video=0,
        umbral_confianza=0.5
    )

- `modelo`: modelo YOLO utilizado.
- `fuente_video`: cámara utilizada (`0` corresponde a la cámara principal).
- `umbral_confianza`: confianza mínima para mostrar una detección.
