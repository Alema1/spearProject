import os
import sys
import cv2
import time
import torch
import serial
import argparse
import numpy as np
from pathlib import Path
from msvcrt import kbhit
import pywinusb.hid as hid
import torch.backends.cudnn as cudnn

import autoTrackingMode
import detect

joystickID = 0xb108
#ser = serial.Serial('COM5', 9600, serial.EIGHTBITS) #porta do arduino
globals()['operationMode'] = 0

def sample_handler(data):
    global operationMode
    # essa funcao tem como objetivo lidar com os dados crus obtidos do joystick
    if data[1] == 2 and operationMode < 3:
        operationMode += 1
    if data[1] == 2 and operationMode > 2:
        operationMode = 0
'''
    # Modo manual
    if(operationMode == 0):
        # Eixo X Esq
        if data[5] == 0:
            if data[4] > 128:
                ser.write('3'.encode('utf-8'))
            else:
                ser.write('4'.encode('utf-8'))            
        if data[5] == 1:
            if data[4] > 128:
                ser.write('1'.encode('utf-8'))
            else:
                ser.write('2'.encode('utf-8'))

        # Eixo X Dir
        if data[5] == 2:
            if data[4] > 128:
                ser.write('6'.encode('utf-8'))
            if data[4] < 128 and data[4] != 0:
                ser.write('5'.encode('utf-8')) 
        if data[5] == 3:
            if data[4] > 128:
                ser.write('8'.encode('utf-8'))
            else:
                ser.write('7'.encode('utf-8'))
           
        # Eixo Y Cima
        if data[7] == 0:
            if data[6] > 128:
                ser.write('b'.encode('utf-8'))
            else:
                ser.write('c'.encode('utf-8')) 
        if data[7] == 1:
            if data[6] > 128:
                ser.write('9'.encode('utf-8'))
            else:
                ser.write('a'.encode('utf-8'))
                    
        # Eixo Y Baixo
        if data[7] == 2:
            if data[6] > 128:
                ser.write('e'.encode('utf-8'))
            if data[6] < 128 and data[6] != 0:
                ser.write('d'.encode('utf-8')) 
        if data[7] == 3:
            if data[6] > 128:
                ser.write('g'.encode('utf-8'))
            else:
                ser.write('f'.encode('utf-8'))

        if (data[5] == 2 and data[4] == 0 and data[6] == 0) or (data[7] ==2 and data[6] == 0 and data[4] == 0):
            ser.write('0'.encode('utf-8'))
        
    print('data[4]:'+str(data[4])+'| data[5]:'+str(data[5])+'| data[6]:'+str(data[6])+'| data[7]:'+str(data[7])+'| data[1]:'+str(data[1]))
'''
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
                            try: # Nas primeiras iterações a data vai ser None, por isso o try except                    
                                #ser.flush()
                            except:
                                #print("Erro ao enviar os dados para o microcontrolador!")
                                #pass # Se não conseguir escrever vai para a proxima interação
                            time.sleep(0.04) #retirar para maior desempenho
                       # return
                    finally:
                        device.close()
                else:
                    print("Joystick não conectado!")

        sys.stdout = codecs.getwriter('mbcs')(sys.stdout)
    print("\nReconhecendo Dispositivo e iniciado calibragem... ")

if __name__ == '__main__':
    import sys
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0
    print(__doc__)
raw_test()    
if(operationMode == 2):
    autoTrackingMode.App(video_src).run()
    
