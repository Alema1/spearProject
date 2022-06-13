"""

Grupo de Automação e Robótica aplicada - GARRA

Spear Manual Control V2.2

ID Thrustmaster T.Flight HOTAS 0xb108
ID Old Joystick 0xb011
"""

import time
from msvcrt import kbhit
import pywinusb.hid as hid
import serial
import sys

joystickID = 0xb108
ser = serial.Serial('COM5', 19200, serial.EIGHTBITS) #porta do arduino

globals()['indicatorX'] = 2
globals()['convertedValueX'] = 0
#global convertedValueX
#global indicatorX

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
    global indicatorX
    global convertedValueX
    # essa funcao tem como objetivo lidar com os dados crus obtidos do joystick   
    if data[5] == 0:
        convertedValueX = Alema1map(data[4],0,255,255,0)
        indicatorX = 0
    if data[5] == 1:
        convertedValueX = Alema1map(data[4],0,255,255,0)
        indicatorX = 1
    if data[5] == 2:
        convertedValueX = Alema1map(data[4],0,255,0,255)
        indicatorX = 2
        #if data[4] == 0:
            #print('Eixo X centrado')
    if data[5] == 3:
        convertedValueX = Alema1map(data[4],0,255,0,255)
        indicatorX = 3
        
    print('Valor: ',convertedValueX, 'Quadrante: ', indicatorX)


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
                                ser.write([1, indicatorX, convertedValueX])
                                #ser.write([2, convertedValueX])
                                #print('Dados enviados')
                                print([1, indicatorX, convertedValueX])
                            except:
                                print("Erro ao enviar os dados para o microcontrolador!")
                               # pass # Se não conseguir escrever vai para a proxima interação
                            #time.sleep(0.04) #retirar para maior desempenho
                       # return
                    finally:
                        device.close()
                else:
                    print("Joystick não conectado!")

        sys.stdout = codecs.getwriter('mbcs')(sys.stdout)
    print("\nReconhecendo Dispositivo e iniciado calibragem... ")

# roda
raw_test()

'''
    # botoes
    if data[1] == 1:
        print('botao 1 pressionado')
    if data[1] == 2:
        print('botao 2 pressionado')
    if data[1] == 4:
        print('botao 3 pressionado')
    if data[1] == 8:
        print('botao 4 pressionado')

    # eixo x
    if data[5] == 0:
        print('Eixo X no 1 quadrante')
    if data[5] == 1:
        print('Eixo X no 2 quadrante')
    if data[5] == 2:
        print('Eixo X no 3 quadrante')
        if data[4] == 0:
            print('Eixo X centrado')
    if data[5] == 3:
        print('Eixo X no 4 quadrante')
        
    # eixo y
    if data[7] == 0:
        print('Eixo Y no 1 quadrante')
    if data[7] == 1:
        print('Eixo Y no 2 quadrante')
    if data[7] == 2:
        print('Eixo Y no 3 quadrante')
        if data[6] == 0:
            print('Eixo Y centrado')
    if data[7] == 3:
        print('Eixo Y no 4 quadrante')

    #eixo z
    if data[9] > 128:
        print('Eixo Z na direita')
    if data[9] < 128:
        print('Eixo Z na esquerda')
    if data[9] == 128:
        print('Eixo Z centrado')
    '''

"""
    if((data [2]>128)or(data [2]<128)):# Eixo Y 0-255
        ser.write([2,data[2]])
        print("Eixo Y",[2,data[2]])

    if((data [3]>128)or(data [3]<128)):# Eixo Z 0-255
        ser.write([3,data[3]])
        print("Eixo Z",[3,data[3]])

    if((data [4]<255)and(data [4]>0)):# 4 Eixo 0-255
        ser.write([4,data[4]])
        print("Eixo 4",[4,data[4]])

    if(data [5]):# Botoes Primarios 1-cima  3-direita  5-baixo  7-esquerda  16-gatilho  32-lateral inferior esquerda  64-inferior central  128-meio
        ser.write([5,data[5]])
        print("Botao 1",[5,data[5]])

    if(data [6]):# Botoes Secundarios  1-centro direita
        ser.write([6,data[6]])
        print("Botao 2",[6,data[6]])
"""
