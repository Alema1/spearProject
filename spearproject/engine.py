
"""

Grupo de Automação e Robótica aplicada - GARRA

Spear Manual Control V2.2

ID Thrustmaster T.Flight HOTAS 0xb108
ID Old Joystick 0xb011
"""

import time
from   msvcrt import kbhit
import pywinusb.hid as hid
import serial
import sys
import autoTrackingMode

import numpy as np
import cv2
import serial
import time
#resolucao da camera
horizontalRes = 640
verticalRes = 480
#variaveis da mira
reticleCircleSize = 1 
reticleLineSize = 5
#cores
red   = (0, 0, 255)
green = (0, 255, 0)
blue  = (255, 0, 0)
#reticleColor = green

joystickID = 0xb108
globals()['xAxis'] = 0
globals()['yAxis'] = 0
globals()['triggerState'] = 0
globals()['operationMode'] = 0
globals()['reticleMultiplier'] = 25
globals()['buttons'] = 0
globals()['reticleColor'] = red

#ser = serial.Serial('COM5', 9600, serial.EIGHTBITS) #porta do arduino

if sys.version_info >= (3,):
    # as is, don't handle unicodes
    unicode = str
    raw_input = input
else:
    # allow to show encoded strings
    import codecs

def Alema1map(valor, in_min, in_max, out_min, out_max):
    return int((valor-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def sample_handler(data):
    # essa funcao tem como objetivo lidar com os dados crus obtidos do joystick   
    global operationMode
    global triggerState
    global xAxis
    global yAxis
    global reticleMultiplier
    global buttons
    global reticleColor

    reticleMultiplier = Alema1map(data[8], 255, 0, 1, 50)

    # Estado cor reticulo
    if data[2] == 244 and reticleColor == red:
        reticleColor = green
    else:
        reticleColor = red

    
    # Estado do botao modo de operação
    if (data[1] == 2 and operationMode == 2):
        operationMode = 0
    if operationMode == 0 and data[1] == 1:
        operationMode = 1
    if (data[1] == 2 and operationMode == 1):
        operationMode = 2

    # Eixo X
    if data[5] == 1:
        if data[4] > 128:
            xAxis = 1
        else:
            xAxis = 2
    if data[5] == 0:
        if data[4] > 128:
            xAxis = 3
        else:
            xAxis = 4
            
    if data[5] == 2 and data[4] == 0:
        xAxis = 0
    if data[5] == 2 and data[4] != 0:
        if data[4] < 128:
            xAxis = 5
        else:
            xAxis = 6
            
    if data[5] == 3:
        if data[4] < 128:
            xAxis = 7
        else:
            xAxis = 8

    # Eixo Y
    if data[7] == 1:
        if data[6] > 128:
            yAxis = 9
        else:
            yAxis = 10
    if data[7] == 0:
        if data[6] > 128:
            yAxis = 11
        else:
            yAxis = 12
            
    if data[7] == 2 and data[6] == 0:
        yAxis = 0
    if data[7] == 2 and data[6] != 0:
        if data[6] < 128:
            yAxis = 13
        else:
            yAxis = 14
            
    if data[7] == 3:
        if data[6] < 128:
            yAxis = 15
        else:
            yAxis = 16

    print(data[2])

def raw_test():
    all_hids = hid.find_all_hid_devices()
    if all_hids:
        while True:
            for index, device in enumerate(all_hids):
                if(device.product_id==joystickID):
                    print("Joystick Reconhecido!")
                    try:
                        device.open()
                        device.set_raw_data_handler(sample_handler)
                        print("\nRecebendo Dados...Pressione qualquer tecla pra sair ")
                        while not kbhit() and device.is_plugged():
                            App(autoTrackingMode).run()
                            try: # Nas primeiras iterações a data vai ser None, por isso o try except
                                #ser.flush()
                                if operationMode == 0:
                                    #ser.write([xAxis])
                                    #ser.write([yAxis])
                                    print('enviando dados')
                                            
                            except:
                                print("Erro ao enviar os dados para o microcontrolador!")
                                pass # Se não conseguir escrever vai para a proxima interação
                            #time.sleep(0.005) #retirar para maior desempenho
                       # return
                    finally:
                        device.close()
                else:
                    print("Joystick não conectado!")

        sys.stdout = codecs.getwriter('mbcs')(sys.stdout)
    print("\nReconhecendo Dispositivo e iniciado calibragem... ")

# roda
raw_test()

