#Archivo para la extraccion de los assets al ejecutar el proyecto (.EXE)

import os
import sys

def recurso_ruta(relative_path):
    """ Obtiene la ruta absoluta para recursos, funciona para dev y para PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)