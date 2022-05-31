'''

Codigo de visao computacional utilizado no Mockup do projeto SPEAR
utilizando como base o Camshift do OpenCV

Vinicius H. Schreiner - Grupo de Automacao e Robotica Aplicada/UFSM

V 1.2

*Resolucao minha webcam = 640x480

'''

import numpy as np
import cv2
import serial
import time

#comport = serial.Serial('COM3',19200) # porta serial

#resolucao da camera
horizontalRes = 640
verticalRes = 480

#função map original do Arduino implementada em py
def Alema1map(valor, in_min, in_max, out_min, out_max):
    return int((valor-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

class App(object):
    def __init__(self, video_src):
        #self.cam = video.create_capture(video_src, presets['cube'])
        #cv2.VideoCaptude(X) altera a camera a ser utilizada
        self.cam = cv2.VideoCapture(0)
        _ret, self.frame = self.cam.read()
        cv2.namedWindow('SPEAR Eye')
        cv2.setMouseCallback('SPEAR Eye', self.onmouse)
        self.selection = None
        self.drag_start = None
        self.show_backproj = False
        self.track_window = None

    def onmouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
            self.track_window = None
        if self.drag_start:
            xmin = min(x, self.drag_start[0])
            ymin = min(y, self.drag_start[1])
            xmax = max(x, self.drag_start[0])
            ymax = max(y, self.drag_start[1])
            self.selection = (xmin, ymin, xmax, ymax)
        if event == cv2.EVENT_LBUTTONUP:
            self.drag_start = None
            self.track_window = (xmin, ymin, xmax - xmin, ymax - ymin)

    def show_hist(self):
        bin_count = self.hist.shape[0]
        bin_w = 24
        img = np.zeros((256, bin_count*bin_w, 3), np.uint8)
        for i in range(bin_count):
            h = int(self.hist[i])
            cv2.rectangle(img, (i*bin_w+2, 255), ((i+1)*bin_w-2, 255-h), (int(180.0*i/bin_count), 255, 255), -1)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        cv2.imshow('hist', img)

    def run(self):
        while True:
            _ret, self.frame = self.cam.read()
            vis = self.frame.copy()
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

            if self.selection:
                x0, y0, x1, y1 = self.selection
                hsv_roi = hsv[y0:y1, x0:x1]
                mask_roi = mask[y0:y1, x0:x1]
                hist = cv2.calcHist( [hsv_roi], [0], mask_roi, [16], [0, 180] )
                cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
                self.hist = hist.reshape(-1)
                self.show_hist()


                vis_roi = vis[y0:y1, x0:x1]
                cv2.bitwise_not(vis_roi, vis_roi)
                vis[mask == 0] = 0

            if self.track_window and self.track_window[2] > 0 and self.track_window[3] > 0:
                self.selection = None
                prob = cv2.calcBackProject([hsv], [0], self.hist, [0, 180], 1)
                prob &= mask
                term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
                track_box, self.track_window = cv2.CamShift(prob, self.track_window, term_crit)

                if self.show_backproj:
                    vis[:] = prob[...,np.newaxis]
                try:
                # Magica                    
                    cv2.ellipse(vis, track_box, (0, 0, 255), 2)
                    #Envio e impressão dos dados do rastreamento
                    X = Alema1map(track_box[0][0],0,horizontalRes,0,255) #X convertido pra int variando de 0 a 640px
                    Y = Alema1map(track_box[0][1],0,verticalRes,0,255) #Y convertido pra int variando de 0 a 480px          
                    #comport.write([3,X])#envia no serial a coordenada X
                    #comport.write([4,Y])#envia no serial a coordenada Y
                    print(X)
                    print(Y)
                    time.sleep(0.05)
                    #comport.write(track_box [0][1])#coordenada Y         
                    #print("Coordenada X")
                    #print(track_box [0][0])#coordenada X
                    #a= comport.Read()
                    #print("Coordenada Y")
                    #print(track_box [0][1])#coordenada Y
                    

                except:
                   print('Excecao!')

            cv2.imshow('SPEAR Eye', vis)
            ch = cv2.waitKey(5)
            if ch == 27:
                break
            if ch == ord('b'):
                self.show_backproj = not self.show_backproj
        cv2.destroyAllWindows()
