"""
Grupo de Automação e Robótica aplicada - GARRA

Spear Manual Control V2.2

"""

import time
from msvcrt import kbhit
import pywinusb.hid as hid
import serial

globals()['XDATA_TO_ARDUINO'] = None
globals()['XDATA_TO_ARDUINO_ANT'] = None
globals()['YDATA_TO_ARDUINO'] = None
globals()['YDATA_TO_ARDUINO_ANT'] = None


#ser = serial.Serial('COM3', 19200, serial.EIGHTBITS) #porta do arduino

def sample_handler(data):
    # TALVEZ POSSA REMOVER
    global XDATA_TO_ARDUINO # Utilizando a variavel global
    global YDATA_TO_ARDUINO # Utilizando a variavel global
    global XDATA_TO_ARDUINO_ANT # Utilizando a variavel global
    global YDATA_TO_ARDUINO_ANT # Utilizando a variavel global
    #############

    if(( data [1] > 128) or ( data [1] < 128)):# Eixo X 0-255

        XDATA_TO_ARDUINO = data [1] ## Tentando resolver
        if (XDATA_TO_ARDUINO != XDATA_TO_ARDUINO_ANT) : XDATA_TO_ARDUINO_ANT = XDATA_TO_ARDUINO # Caso os dados forem diferentes atualiza

    if(( data [2] > 128) or ( data [2] < 128)):# Eixo Y 0-255

        YDATA_TO_ARDUINO = data [2] ## Tentando resolver
        if (YDATA_TO_ARDUINO != YDATA_TO_ARDUINO_ANT) : YDATA_TO_ARDUINO_ANT = YDATA_TO_ARDUINO # Caso os dados forem diferentes atualiza
    
        """
        try:  # Na primeira iteração os valores serao None, por isso o Try Except
            if(DATA_TO_ARDUINO != DATA_TO_ARDUINO_ANT) : DATA_TO_ARDUINO_ANT = DATA_TO_ARDUINO # Caso os dados forem diferentes atualiza
        except:
            pass
            #DATA_TO_ARDUINO = data[1] # atualiza o valor a ser escrito como o eixo x

        """
        #ser.write([1,data[1]]) # Removido para a função de loop
        #print("Eixo X",[1,data[1]]) # Removido para a função de loop

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

def raw_test():
    all_hids = hid.find_all_hid_devices()
    if all_hids:
        while True:
            for index, device in enumerate(all_hids):
                if(device.product_id==0xb011): #id do joystick a ser usado
                    try:
                        device.open()

                        #set custom raw data handler
                        device.set_raw_data_handler(sample_handler)

                        print("\nRecebendo Dados...Pressione qualquer tecla pra sair ")
                        while not kbhit() and device.is_plugged():

                            try: # Nas primeiras iterações a data vai ser None, por isso o try except
                                #print("Eixo X", XDATA_TO_ARDUINO) # Só pra debug
                                #print("Eixo Y", YDATA_TO_ARDUINO) # Só pra debug
                                ser.write([1, XDATA_TO_ARDUINO]) # Data a ser enviada
                                ser.write([2, YDATA_TO_ARDUINO]) # Data a ser enviada

                                """
                                Na versao final o PRINT tem que voltar pra o tratamento dos eixos
                                """

                            except:
                                #print("Eixo X DEBUGGING ERROR", XDATA_TO_ARDUINO) # Só pra debug
                                #print("Eixo Y DEBUGGING ERROR", YDATA_TO_ARDUINO) # Só pra debug
                                pass # Se não conseguir escrever vai para a proxima interaçãoptimize

                            #MANDA DADO A CADA .5 seg
                            time.sleep(0.04) #RETIRAR VERSÃO FINAL PARA MELHOR DESEMPENHO

                        return
                    finally:
                        device.close()
        else:
            print("Joystick não conectado!!")
#
if __name__ == '__main__':
    # first be kind with local encodings
    import sys
    if sys.version_info >= (3,):
        # as is, don't handle unicodes
        unicode = str
        raw_input = input
    else:
        # allow to show encoded strings
        import codecs
        sys.stdout = codecs.getwriter('mbcs')(sys.stdout)
    print("\nReconhecendo Dispositivo e iniciado calibragem... ")
    raw_test()
