'''
S.P.E.A.R. Control

Vinicius H. Schreiner - Grupo de Automação e Robótica Aplicada/UFSM

V 2.0

'''

import numpy as np
import cv2
import serial
import time
import manualMode
import detect
import autoTrackingMode


if __name__ == '__main__':
    import sys
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0
    print(__doc__)
    autoTrackingMode.App(video_src).run()
