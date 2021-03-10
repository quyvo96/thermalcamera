#!/usr/bin/python3
import time
Start_time = time.time()
print('[WAIT] WAITING FOR SYSTEM....')
import wx
import numpy as np
import cv2 as cv
from datetime import datetime
import os, sys
from imutils import paths
import csv
from numpy.linalg import norm
import pygame
import socket
import math
import threading
try:
    import serial
except:
    pass
import GetPath
#############FLIR MODULES##################
from multiprocessing  import Queue
from uvctypesParabilis_v2 import *
#****************************
#           GUI
#****************************
from gui import *
#****************************
#        Application
#****************************
import General_Globals as PG
#**************************
#     INFOMATION
#**************************
BUF_SIZE = 2
q = Queue(BUF_SIZE)
Path = sys._getframe().f_code.co_filename
Path = os.path.split(Path)[0]
if not (Path in sys.path):
    sys.path.append(Path)
#*****************************
#        CLASS FOR GUI
#*****************************
class face_recognition_app(wx.App):
    """docstring for face recognition application"""
    def __init__(self, parent):
        super(face_recognition_app, self).__init__(parent)
        self.parent = parent
    def MainLoop(self):
        self.My_EventLoop = wx.GUIEventLoop()
        old = wx.EventLoop.GetActive ()
        wx.EventLoop.SetActive ( self.My_EventLoop )
        PG.App_Running = True
        Previous_Time = time.time()
        Time_fileCSV = time.time()
        timeFFC = time.time()
        timeHDMI = time.time()
        PG.data_temp = []
        PG.data_envir = [0.0, 0.0, 0.0, 0.0, 0.0]
        faceTempRaw = 0.0
        flagE100 = 0
        PG.Temp_text = 0.0
        PG.flag_get_temp = 0
        PG.data_temp = [0.0, 0.0, 0.0, 0.0, 0.0]
        PG.data_temp_raw = [0.0, 0.0, 0.0, 0.0, 0.0]
        faceTemp = 0.0
        arrayFist = []
        array2nd = []
        oldDisplayviaHDMI = False
        PG.DisplayviaHDMI = True
        valueKey = 0.0
        countFFC = 0
        face = []
        print('[OK] RUNNING')
        Previous_TimeforHDMI = time.time()
        #timeOneHours = time.time()
        while PG.App_Running:
            if ( oldDisplayviaHDMI != PG.DisplayviaHDMI):
                if(PG.DisplayviaHDMI):
                    if(PG.FFC_mode == '0'):
                        if(time.time() - timeHDMI >= 600):
                            
                            print("ffc HDMI")
                            print(time.time())
                            print("-----------")
                            perform_manual_ffc(PG.devh)
                            PG.flag_get_temp = 4
                            timeFFC = time.time()
                            time.sleep(0.2)
                    os.system('xset dpms force on')
                    #print("[PROCESS] Turn on display")
                else:
                    if(PG.FFC_mode == '0'):
                        timeHDMI = time.time()
                    os.system('xset dpms force off')
                    #print("[PROCESS] Turn off display")
                oldDisplayviaHDMI = PG.DisplayviaHDMI
            _, frame = PG.cam.read()
            frame = cv.flip(frame, 0)
            frame2, PG.data = get_thermal_image()
            
            frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            frame2 = cv.cvtColor(frame2,cv.COLOR_BGR2RGB)
            #view on interface
            PG.frame = frame
            PG.frame2 = frame2
            cv.rectangle(PG.frame2, (1,1),(1,1), PG.color_rec, 2)
            temp_environment(PG.frame, PG.frame2)
            faceTempRaw = face_recognition_name(PG.frame,PG.frame2)
            PG.faceRawShow = faceTempRaw
            if(PG.flag_get_temp != 4):
                if(len(PG.data_envir_raw) < 5):
                    PG.data_envir_raw.append(PG.TempEnvirRaw)
                elif(len(PG.data_envir_raw) == 5):
                    PG.agv_envir_raw = round_down(float(sum(PG.data_envir_raw)/5),1)
                    PG.change1 = 1
                if(faceTempRaw != 0.0 ):
                    if(PG.flag_get_temp == 1 or PG.flag_get_temp == 2):
                        if(countFFC == 0):
                            perform_manual_ffc(PG.devh)
                            time.sleep(0.2)
                        if(countFFC == 5):
                            PG.TempEnvirDefault = PG.TempEnvirRaw
                            time.sleep(0.2)
                        countFFC = countFFC + 1
                        if(countFFC >= 14):
                            #temp_environment(PG.frame, PG.frame2)
                            flagE100 = 0
                            PG.flag_get_temp = 3
                            PG.arrayEnvir100 = []
                            PG.calibEnvirAve = 0.0
                            PG.calibFaceAve = 0.0
                            PG.envirFirst25 = 0.0
                            countFFC = 0
                            PG.Previous_Time2 = time.time()
                    if(PG.flag_get_temp == 3):
                        PG.data_temp_raw.pop(0)
                        PG.data_temp_raw.append(faceTempRaw)
                        Previous_TimeforHDMI = time.time()
                        if(len(arrayFist) < 2):
                            arrayFist.append(faceTempRaw)
                        if(len(arrayFist) == 2):
                            PG.Temp_text = round(((PG.data_temp[3] + PG.data_temp[4])/2),1)
                            PG.agv_temp_raw = round(((PG.data_temp_raw[3] + PG.data_temp_raw[4])/2),1)
                            arrayFist = []
                            PG.showSquare = PG.Temp_text
                        if(PG.showSquare != 0):
                            if(len(array2nd) < 2):
                                array2nd.append(PG.showSquare)
                            elif(len(array2nd) == 2):
                                if(PG.showTopofScreen == 0.0):
                                    PG.showTopofScreen = round((PG.showSquare +array2nd[1])/2,1)
                                else:
                                    if(PG.indexStep >= 2):
                                        PG.showTopofScreen = round(((PG.showTopofScreen + PG.showSquare)/2 ),1)
                                        PG.indexStep = 0
                                PG.indexStep = PG.indexStep + 1
                                array2nd = [0.0]
                        if(PG.showTopofScreen != 0):
                            #PG.showTopofScreen = round_down((PG.showTopofScreenRaw + envir_lepton_calib() + float(PG.values1) + PG.calibFaceAve),1)
                            if(PG.Temp_text_backup <= PG.showTopofScreen):
                                PG.Temp_text_backup = PG.showTopofScreen  
                        if(valueKey == 0):
                            valueKey = faceTempRaw
                        elif(abs(valueKey-faceTempRaw) >= 1):
                            PG.showTopofScreenRaw = 0
                            PG.Temp_text_backup = 0
                            PG.indexStep = 0
                            valueKey = 0
                            PG.data_run = 0
                            PG.color_rec = (255,255,255)
                            PG.showSquare = 0
                            PG.showTopofScreen = 0
                            arrayFist = []
                            array2nd = []
                            PG.Temp_text = 0.0
                        PG.data_run = 1
                        if PG.Temp_text >= float(PG.values0):
                            PG.color_rec = (255,0,0)
                            play_beep()
                        else:
                            PG.color_rec = (255,255,255)
                elif(faceTempRaw == 0.0 ):
                    PG.showTopofScreenRaw = 0
                    PG.Temp_text_backup = 0
                    PG.indexStep = 0
                    valueKey = 0
                    PG.data_run = 0
                    PG.color_rec = (255,255,255)
                    PG.showSquare = 0
                    PG.showTopofScreen = 0
                    arrayFist = []
                    array2nd = []
                    PG.Temp_text = 0.0
                    #print(time.time() - Previous_TimeforHDMI)
                    if(time.time() - Previous_TimeforHDMI >= 59):
                        PG.DisplayviaHDMI = False
                        Previous_TimeforHDMI = time.time()

                if(PG.flag_get_temp == 3):
                    if(PG.FFC_mode == '0'):
                            if(time.time() - timeFFC >= 900):
                                print("ffc :")
                                print(time.time())
                                print("-----------")
                                perform_manual_ffc(PG.devh)
                                PG.flag_get_temp = 4
                                time.sleep(0.2)
                                timeFFC = time.time()
                    if(time.time() - PG.Previous_Time2 >= 7.2):
                        #print(time.time() - PG.Previous_Time2)
                        PG.arrayEnvir100.append(PG.TempEnvirRaw)
                        if(flagE100 == 0):
                            if(len(PG.arrayEnvir100) == 25 ):
                                flagE100 = 1
                                PG.envirFirst25 = 0
                                PG.arrayEnvir100 = []
                                #print("step1")
                        elif(flagE100 == 1):
                            if(len(PG.arrayEnvir100) == 25):
                                PG.TempEnvirDefault = round(float(sum(PG.arrayEnvir100)/25), 1)
                                PG.envirFirst25 = PG.TempEnvirDefault
                                PG.arrayEnvir100 = []
                                flagE100 = 2
                                #print("step2")
                        elif(flagE100 == 2):
                            if(len(PG.arrayEnvir100) == 25):
                                PG.TempEnvirDefault  = round(float(sum(PG.arrayEnvir100)/25), 1)
                                PG.data_envir.pop(0)
                                PG.data_envir.append(PG.TempEnvirDefault)
                                PG.calibEnvirAve = round(float(int((PG.TempEnvirDefault - PG.envirFirst25)*100)/100), 1)
                                PG.arrayEnvir100 = []
                                #print("step3")
                        PG.change2 = 1
                        PG.Previous_Time2 = time.time()
                if(faceTempRaw != 0.0 ):
                    if(PG.TempEnvirDefault <= 20 ):
                        PG.calibFaceAve = float(int(((PG.calibEnvirAve)*(-float(PG.values2)))*100)/100)
                        PG.faceChange = PG.values2
                    elif(PG.TempEnvirDefault > 20 and PG.TempEnvirDefault < 23):
                        PG.calibFaceAve = float(int(((PG.calibEnvirAve)*(-float(PG.values6)))*100)/100)
                        PG.faceChange = PG.values6
                    else:
                        PG.calibFaceAve = float(int(((PG.calibEnvirAve)*(-float(PG.values7)))*100)/100)
                        PG.faceChange = PG.values7
                        
                    faceTemp = round((faceTempRaw + envir_lepton_calib() + float(PG.values1) + PG.calibFaceAve),1)
                    
                    PG.face_c = faceTemp
                    PG.data_temp.pop(0)
                    PG.data_temp.append(faceTemp)
                if(PG.setlog == 1):
                    timedate = [datetime.now().strftime("%Y/%m/%d/%H:%M:%S")]
                    faceAve = [str(PG.Temp_text)]
                    faceRaw = [str(faceTempRaw)]
                    envirAve = [str(PG.TempEnvirDefault)]
                    envirRaw = [str(PG.TempEnvirRaw)]
                    sensor = [str(PG.TempSensor)]
                    Square = [str(PG.showSquare)]
                    TopofScreen = [str(PG.Temp_text_backup)]
                    TopofScreenReal = [str(PG.showTopofScreen)]
                    calibTemp = [str(PG.values1)]
                    envir = [str(PG.calibEnvirAve)]
                    faceTempRaw_C = [str(faceTemp)]
                    face = [str(PG.faceChange)]
                    try:
                        if(faceTempRaw != 0.0):
                            try:
                                with open(PG.filecsv, mode='a') as myfile:
                                    myfile = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                    myfile.writerow(timedate + faceAve + faceRaw + faceTempRaw_C + Square + TopofScreenReal + TopofScreen + envirAve + envirRaw + sensor + calibTemp + envir + face)
                            except:
                                print("ok")

                        if(faceTempRaw == 0.0):
                            if(time.time() - Time_fileCSV >= 2.5):
                                try:
                                    with open(PG.filecsv, mode='a') as myfile:
                                        myfile = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                        myfile.writerow(timedate + faceAve + faceRaw + faceTempRaw_C + Square + TopofScreenReal + TopofScreen + envirAve + envirRaw + sensor + calibTemp + envir + face)
                                    Time_fileCSV = time.time()
                                except:
                                    print("ok")
                    except:
                        print("error")
            PG.runSetting = PG.runSetting + 1
            if(PG.flag_get_temp == 4):
                if(time.time() - timeFFC >= 5):
                    print("ffc 2")
                    PG.flag_get_temp = 3
            PG.view  = True
            PG.Main_Frame.m_panel_video.Refresh()
            PG.Main_Frame.m_panel_video_thermography.Refresh()
            #bug in macos
            while self.My_EventLoop.Pending(): 
                self.My_EventLoop.Dispatch()
            self.My_EventLoop.ProcessIdle()          
            sec = time.time() - Previous_Time
            fps = 1 / (sec)
            str_fps = 'FPS: %2.3f' % fps
            str_fps = str_fps +"    IP: " + PG.IP_addr
            PG.Main_Frame.SetStatusText(str_fps,0)
            Previous_Time = time.time()

        time.sleep(0.1)
        libuvc.uvc_stop_streaming(PG.devh)
        time.sleep(0.1)
        libuvc.uvc_unref_device(PG.dev)
        time.sleep(0.1)
        libuvc.uvc_exit(PG.ctx)
        time.sleep(0.1)
        PG.cam.release()
        print('[INFO] GOODBYE')
        time.sleep(1)
        os.system('exit')
        os.system('xdotool search --name terminal key --window %@ alt+F4')
        os.system('killall -9 python3')
        exit(1)
        #cv.destroyAllWindows()
class face_recognition_frame(frame_main1):
    """docstring for face_recognition_frame"""
    def __init__(self, parent):
        super(face_recognition_frame, self).__init__(parent)
        self.parent = parent
        self.SetIcon(wx.Icon("gui-folder/fr-arv.ico"))
        self.view = 0
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
    def frame_mainOnClose(self,event):
        #Check password
        view_login = dialog_login(None)
        view_login.ShowModal()
        if PG.login :
            PG.App_Running = False
        PG.login = False 
    def m_button_exitOnButtonClick( self, event ):
        #Check password
        view_login = dialog_login(None)
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show")
        view_login.ShowModal()
        if PG.login :
            PG.App_Running = False
        PG.login = False
    def m_panel_videoOnEraseBackground( self, event ):
        pass
    def m_panel_videoOnPaint(self,event):
        if(PG.flag_get_temp == 1 or PG.flag_get_temp == 2 or PG.flag_get_temp == 4):
            self.m_textCtrl_temp.SetValue("自動校正中")#"FFC calib"
        if(PG.flag_get_temp == 3):
            self.m_textCtrl_temp.SetForegroundColour( wx.Colour( PG.color_rec))
            if(float(PG.showTopofScreen) == 0.0):
                self.m_textCtrl_temp.SetValue(str(PG.Temp_text_on_top))
            elif(float(PG.showTopofScreen) >= 40.0):
                self.m_textCtrl_temp.SetValue("体温が高いです")#Hight temperature
            elif(float(PG.showTopofScreen) <= 35.0):
                self.m_textCtrl_temp.SetValue('Lo')
            else:
                if(PG.Temp_text_backup >= float(PG.values0)):
                    self.m_textCtrl_temp.SetValue("体温が高いです")#Hight temperature
                else:
                    self.m_textCtrl_temp.SetValue(" 体温は正常です")#Normal temperature
        if (len(PG.data_temp)== 5) and (self.view == 1):
            if( PG.data_run == 1):

                self.m_textCtrl_tempface1.SetValue(str(PG.data_temp[0]))
                self.m_textCtrl_tempface2.SetValue(str(PG.data_temp[1]))
                self.m_textCtrl_tempface3.SetValue(str(PG.data_temp[2]))
                self.m_textCtrl_tempface4.SetValue(str(PG.data_temp[3]))
                self.m_textCtrl_tempface5.SetValue(str(PG.data_temp[4]))

                self.m_textCtrl_tempfaceraw1.SetValue(str(PG.data_temp_raw[0]))
                self.m_textCtrl_tempfaceraw2.SetValue(str(PG.data_temp_raw[1]))
                self.m_textCtrl_tempfaceraw3.SetValue(str(PG.data_temp_raw[2]))
                self.m_textCtrl_tempfaceraw4.SetValue(str(PG.data_temp_raw[3]))
                self.m_textCtrl_tempfaceraw5.SetValue(str(PG.data_temp_raw[4]))

                self.m_textCtrl_tempfaceAgv.SetValue(str(PG.showSquare))

        if PG.view:
            dc = wx.BufferedPaintDC(self.m_panel_video)
            PG.frame2 = cv.resize(PG.frame2,(800,600))
            h = PG.frame2.shape[0]
            w = PG.frame2.shape[1]
            self.m_panel_video.SetSize(width =w,height=h)
            image2 = wx.Bitmap.FromBuffer(w, h, PG.frame2)
            dc.DrawBitmap(image2, 0, 0)

    def m_panel_video_thermographyOnEraseBackground( self, event ):
        pass
    def m_panel_video_thermographyOnPaint(self,event):

        if (self.view == 1):
            if( PG.change2 == 1):

                self.m_textCtrl_tempenvir1.SetValue(str(PG.data_envir[0]))
                self.m_textCtrl_tempenvir2.SetValue(str(PG.data_envir[1]))
                self.m_textCtrl_tempenvir3.SetValue(str(PG.data_envir[2]))
                self.m_textCtrl_tempenvir4.SetValue(str(PG.data_envir[3]))
                self.m_textCtrl_tempenvir5.SetValue(str(PG.data_envir[4]))

                self.m_textCtrl_tempenviragv.SetValue(str(PG.TempEnvirDefault))
                PG.change2 = 0

            if( PG.change1 == 1):

                self.m_textCtrl_tempenvirraw1.SetValue(str(PG.data_envir_raw[0]))
                self.m_textCtrl_tempenvirraw2.SetValue(str(PG.data_envir_raw[1]))
                self.m_textCtrl_tempenvirraw3.SetValue(str(PG.data_envir_raw[2]))
                self.m_textCtrl_tempenvirraw4.SetValue(str(PG.data_envir_raw[3]))
                self.m_textCtrl_tempenvirraw5.SetValue(str(PG.data_envir_raw[4]))

                self.m_textCtrl_tempenvirrawagv.SetValue(str(PG.agv_envir_raw))
                PG.change1 = 0
                PG.data_envir_raw = []
        else:
            if( PG.change1 == 1):
                PG.data_envir_raw = []
                PG.change1 = 0
        if PG.view:
            dc = wx.BufferedPaintDC(self.m_panel_video_thermography)
            
            PG.frame = cv.resize(PG.frame,(800,600))
            try:
                PG.frame = camera(PG.frame)
            except:
                pass
            h = PG.frame.shape[0]
            w = PG.frame.shape[1]
            self.m_panel_video_thermography.SetSize(width =w,height=h)
            image = wx.Bitmap.FromBuffer(w, h, PG.frame)
            dc.DrawBitmap(image, 0, 0)
    def m_button_settingOnButtonClick( self, event ):
        view_login = dialog_login(None)
        view_setting = dialog_setting(None)
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show")
        view_login.ShowModal()
        if PG.login :
            os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
            time.sleep(1)
            view_setting.Show()
        PG.login = False
    def m_button_dataOnButtonClick( self, event ):
        self.view = 1
        self.m_panel_data_view.Show()
    def m_button_clOnButtonClick( self, event ):
        self.view = 0
        self.m_panel_data_view.Hide()
def Average(List):
    agv = sum(List) - max(List) - min(List)
    agv = agv/3
    return agv

def play_beep():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def get_thermal_image():
    
    data = q.get(True, 500)
    data = cv.flip(data, 0)
    data2 = data
    data = cv.resize(data[:,:], (640, 480))
    frame2 = cv.LUT(raw_to_8bit(data2), generate_colour_map())
    frame2 = cv.resize(frame2[:,:], (640, 480))
    
    PG.data = data
    return frame2, data
def camera(frame):
    img = PG.file_path + "/long_circle.png"
    img_fg = cv.imread(img)
    frame = cv.bitwise_or(frame, img_fg, mask = None)
    return frame
def face_recognition_name(frame, frame2):
    value_temp = 0.0
    (H, W) = frame.shape[:2]
    blob = cv.dnn.blobFromImage(frame, 1 / 255.0, (192, 192),swapRB=False, crop=False)
    PG.net.setInput(blob)
    layerOutputs = PG.net.forward(PG.ln)
    boxes = []
    confidences = []
    classIDs = []
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.6:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    idxs = cv.dnn.NMSBoxes(boxes, confidences, 0.5,0.3)
    if len(idxs) > 0:
        for i in idxs.flatten():
            # extract the bounding box coordinates
            (x1, y1) = (boxes[i][0], boxes[i][1])
            (w1, h1) = (boxes[i][2], boxes[i][3])
            x = x1
            y = y1
            w = w1
            h = h1
            if(PG.flag_get_temp == 0):
                #perform_manual_ffc(PG.devh)
                #time.sleep(1)
                PG.flag_get_temp = 1
            #********************
            PG.DisplayviaHDMI = True
            if(w1 > 230 or h1 > 300):
                PG.Temp_text_on_top = "カメラから離れて下さい"#"Too close"
            elif(y1 > 150 and h1 < 300):
                PG.Temp_text_on_top = "顔を楕円に合わせて下さい"#"Fit the circle"
            elif((x1 <= 260 and x1 >= 190) and (y1 >= 80 and y1 <= 150)and(w1 <= 230 and w1 >= 150) and (h1 >= 190 and h1 <= 300)):
                frame2, value_temp = get_temp(frame2, x ,y ,w ,h)
                if(value_temp != 0):
                    #cv.rectangle(frame, (int(x) - int(PG.values5), int(y) - int(PG.values5)), (int(x+w)+ int(PG.values5), int(y+h)+ int(PG.values5)), PG.color_rec, 2)
                    cv.rectangle(frame2, (int(x) - int(PG.values5), int(y) - int(PG.values5)), (int(x+w)+ int(PG.values5), int(y+h)+ int(PG.values5)), PG.color_rec, 2)
                    cv.rectangle(frame, (int(x+w/2) - 20 - int(PG.values5), int(y+h/4) -20 - int(PG.values5)), (int(x+w/2) + 20  + int(PG.values5), int(y+h/4) + 20 + int(PG.values5)), PG.color_rec, 2)
                    if(PG.showSquare != 0 and PG.flag_get_temp == 3 and PG.showTopofScreen != 0):
                        cv.putText(frame,str(PG.showTopofScreen),(int(x+w) + 2- int(PG.values5),int(y+20)- int(PG.values5)), cv.FONT_HERSHEY_SIMPLEX,1.3,PG.color_rec,2,cv.FILLED)
                        cv.putText(frame2,str(PG.showTopofScreen),(int(x+w) + 2- int(PG.values5),int(y+20)- int(PG.values5)), cv.FONT_HERSHEY_SIMPLEX,1.3,PG.color_rec,2,cv.FILLED)
                else:
                    value_temp = 0
            else:
                PG.Temp_text_on_top = "カメラに近づいて下さい"#Come up to the camera
    PG.frame = frame
    PG.frame2 = frame2
    return value_temp

def get_temp(frame2, x ,y ,w ,h):
    #_, PG.data = get_thermal_image()
    left1 = int(int(x+w/2) - 30 -int(PG.values4)-int(PG.values5))
    top1 = int(int(y+h/4) -20 - int(PG.values5) -int(PG.values3))
    right1 = int(int(x+w/2) + 10 -int(PG.values4)+int(PG.values5))
    bottom1 = int(int(y+h/4) + 20 -int(PG.values3)+int(PG.values5))
    if ((bottom1-top1) <= 10):
        PG.values5 = int(PG.values5) + 1
    #***************************************
    PG.frame_cut = PG.data[top1:bottom1,left1:right1]
    _, maxVal, _, _ = cv.minMaxLoc(PG.frame_cut)
    val = ktoc(maxVal)
    value_temp = float(format(val))
    value_temp = round_down((value_temp),1)
    if(value_temp>=0):
        #faceTemp = round_down((value_temp  + envir_lepton_calib() + float(PG.values1) + PG.calibFaceAve),1)
        frame2 = cv.rectangle(frame2, (left1,top1),(right1,bottom1), PG.color_rec, 2)
    return frame2 , value_temp
def envir_lepton_calib():
    return float(PG.TempEnvirDefault - PG.agv_envir_raw)

def temp_environment(frame, frame2):

    if(PG.flag_get_temp == 1 or PG.flag_get_temp == 2 or PG.flag_get_temp == 0):
        cv.putText(PG.frame, "FFC", (350,27), cv.FONT_HERSHEY_SIMPLEX, 1, PG.color_rec2, 2)
    left2 = int(1)
    top2 = int(1)
    right2 = int(36)
    bottom2 = int(36)
    PG.frame = cv.rectangle(PG.frame, (left2,top2),(right2,bottom2), PG.color_rec, 2)
    PG.frame2 = cv.rectangle(PG.frame2, (left2,top2),(right2,bottom2), PG.color_rec, 2)
    PG.frame_env = PG.data[top2:bottom2,left2:right2]
    _, maxVal1, _, _ = cv.minMaxLoc(PG.frame_env)
    val1 = round(((maxVal1 - 27315) / 100.0), 1)
    PG.TempEnvirRaw = float(format(val1))
#********change1*******
class dialog_login(MyDialog_Login):
    """docstring for dialog_login"""
    def __init__(self, parent):
        super(dialog_login, self).__init__(parent)
        self.parent = parent
        self.SetPosition(wx.Point(10,10))
    def m_button_cancelOnButtonClick( self, event ):
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
        self.Destroy()
    def m_button_confirmOnButtonClick( self, event ):
        if self.m_textCtrl_password.GetValue() == "asti":
            os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
            PG.login = True
            self.Destroy()
        else:
            PG.login = False
            answer = wx.MessageBox("Wrong password ?", "ERROR",wx.OK_DEFAULT, self)
            self.m_textCtrl_password.SetValue("")
    def MyDialog_LoginOnClose( self, event ):
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
        self.Destroy()
    def Enter_2_confirm( self, event ):
        if event.GetKeyCode() ==13:
            self.m_button_confirmOnButtonClick(event=None)
        else:
            event.Skip()
class dialog_setting(MyDialog_setting):
    """docstring for dialog_login"""
    def __init__(self, parent):
        super(dialog_setting, self).__init__(parent)
        self.parent = parent
        self.SetPosition(wx.Point(1700,10))
        self.set = 0
        self.numlog = 0
        PG.setting = 1
        self.m_textCtrl_fever.SetValue(PG.values0)
        self.m_textCtrl_ktoc.SetValue(PG.values1)
        self.m_textCtrl_envirLepton.SetValue(str(PG.TempEnvirDefault))
        self.m_textCtrl_show_sensor.SetValue(str(PG.TempSensor))
        self.m_textCtrl_facechange.SetValue(str(PG.values2))
        self.m_textCtrl_facechange1.SetValue(str(PG.values6))
        self.m_textCtrl_facechange2.SetValue(str(PG.values7))
        if(PG.setlog== 1):
            self.m_textCtrl_log.SetValue("SAVE FILE")
        else:
            self.m_textCtrl_log.SetValue("CREATE FILE")
        if(PG.setSensor == 1):
            self.m_textCtrl_onSenser.SetValue("ON")
        else:
            self.m_textCtrl_onSenser.SetValue("OFF")
        if(PG.FFC_mode == '1'):
            self.m_textCtrl_ffc.SetValue("Normal")
        else:
            self.m_textCtrl_ffc.SetValue("Auto")
    def m_panel_settingOnEraseBackground( self, event ):
        pass

    def m_panel_settingOnPaint( self, event ):
        self.m_textCtrl_runSetting.SetValue(str(PG.runSetting))

        self.m_textCtrl_FistEnvirAve.SetValue(str(PG.envirFirst25))
        self.m_textCtrl_EnvirAve.SetValue(str(PG.TempEnvirDefault))
        self.m_textCtrl_A.SetValue(str(PG.calibEnvirAve))

        self.m_textCtrl_Face_c.SetValue(str(PG.face_c))
        self.m_textCtrl_FaceRaw1.SetValue(str(PG.faceRawShow))
        self.m_textCtrl_CalibTemp.SetValue(str(PG.values1))
        self.m_textCtrl_EnvirAve1.SetValue(str(PG.TempEnvirDefault))
        self.m_textCtrl_EnvirRaw.SetValue(str(PG.agv_envir_raw))
        self.m_textCtrl_A1.SetValue(str(PG.calibEnvirAve))
        self.m_textCtrl_FaceChange.SetValue(str(PG.faceChange)) 
        if(PG.runSetting >= 2):
            PG.runSetting = 0
    def MyDialog_settingOnClose( self, event ):
        if (self.set == 1):
            PG.setting = 0
            self.set = 0
            self.Destroy()
        else:
            answer3 = wx.MessageBox("Close without saving?", "Confirm",wx.OK | wx.CANCEL, self)
            if answer3 == wx.OK:
                PG.setting = 0
                self.set = 0
                getValue()
                self.Destroy()
            else:
                self.set = 0
    def m_button_closeOnButtonClick( self, event ):
        if (self.set == 1):
            PG.setting = 0
            self.set = 0
            self.Destroy()
        else:
            answer6 = wx.MessageBox("Close without saving?", "Confirm",wx.OK | wx.CANCEL, self)
            if answer6 == wx.OK:
                PG.setting = 0
                self.set = 0
                getValue()
                self.Destroy()
            else:
                self.set = 0
    def m_button_fever_downOnButtonClick( self, event ):
        PG.values0 = str(round(float(PG.values0) - 0.1, 2))
        self.m_textCtrl_fever.SetValue((PG.values0))

    def m_button_fever_upOnButtonClick( self, event ):
        PG.values0 = str(round(float(PG.values0) + 0.1,2) )
        self.m_textCtrl_fever.SetValue(PG.values0)

    def m_button_tempktoc_downOnButtonClick( self, event ):
        PG.values1 = str(round(float(PG.values1) - 0.1, 2))
        self.m_textCtrl_ktoc.SetValue(PG.values1)

    def m_button_tempktoc_upOnButtonClick( self, event ):
        PG.values1 = str(round(float(PG.values1) + 0.1,2))
        self.m_textCtrl_ktoc.SetValue(PG.values1)

    def m_button_moveupOnButtonClick( self, event ):
        PG.values3 = int(PG.values3) + 1

    def m_button_moveleftOnButtonClick( self, event ):
        PG.values4 = int(PG.values4) + 1

    def m_button_moverightOnButtonClick( self, event ):
        PG.values4 = int(PG.values4) - 1

    def m_button_movebottomOnButtonClick( self, event ):
        PG.values3 = int(PG.values3) - 1

    def m_button_zoomOnButtonClick( self, event ):
        PG.values5 = int(PG.values5) + 1

    def m_button_zoomoutOnButtonClick( self, event ):
        PG.values5 = int(PG.values5) - 1

    def m_button_temp_envirLeptonOnButtonClick( self, event ):
        self.m_textCtrl_envirLepton.SetValue(str(PG.TempEnvirDefault))
        self.m_textCtrl_show_sensor.SetValue(str(PG.TempSensor))
    def m_button_saveOnButtonClick( self, event ):
        answer7 = wx.MessageBox("SAVE?", "Confirm",wx.OK | wx.CANCEL, self)
        if answer7 == wx.OK:
            try:
                PG.values1 = float(self.m_textCtrl_ktoc.GetValue())
                PG.values0 = float(self.m_textCtrl_fever.GetValue())
            except:
                PG.error = 1
            if (PG.error == 0):
                PG.values0 = self.m_textCtrl_fever.GetValue() #fevertemp
                PG.values1 = self.m_textCtrl_ktoc.GetValue() #valuektoc
                PG.values2 = str(PG.values2) #color_mode
                PG.values3 = str(PG.values3) #move_leftright
                PG.values4 = str(PG.values4) #move_topbottom
                PG.values5 = str(PG.values5) #zoom
                PG.values6 = str(PG.values6) #move_leftright
                PG.values7 = str(PG.values7) #move_topbottom
                PG.values8 = str(PG.values8) #zoom
                saveValue()
                self.set = 1
            else:
                answer2 = wx.MessageBox("You need to fill in Value!", "ERROR", wx.OK, self)
                PG.error = 0
    def m_button_resetOnButtonClick( self, event ):
        answer4 = wx.MessageBox("Reset setting?", "Confirm",wx.OK | wx.CANCEL, self)
        if answer4 == wx.OK:
            PG.setting = 0
            self.set = 0
            getValueReset()
            time.sleep(0.5)
            saveValue()
            time.sleep(0.5)
            getValue()
            self.Destroy()
        else:
            self.set = 0

    def m_button_ffcManualOnButtonClick( self, event ):
        PG.FFC_mode = '1'
        self.m_textCtrl_ffc.SetValue("Normal")
        #set_manual_ffc(PG.devh)

    def m_button_ffcAutoOnButtonClick( self, event ):
        PG.FFC_mode = '0'
        self.m_textCtrl_ffc.SetValue("Auto")
        #set_manual_ffc(PG.devh)

    def m_button_ffcTestOnButtonClick( self, event ):
        PG.data_envir = [0.0, 0.0, 0.0, 0.0, 0.0]
        time.sleep(0.5)
        PG.flag_get_temp = 2
        
    def m_button_logcsvOnButtonClick( self, event ):
        global fcsv
        if(PG.setlog == 0):
            self.m_textCtrl_log.SetValue("SAVE FILE")
            a = self.m_dirPicker_csv.GetPath()
            PG.filecsv = a + "/FileData" + datetime.now().strftime("%d%H%M") + "_"+str(self.numlog) + ".csv"
            self.numlog = self.numlog + 1
            PG.setlog = 1
            try:
                fcsv = open(PG.filecsv, "x")
            except:
                print("PG.filecsv error")
            face = ["Timestamp", "FACE_AVE", "FACE_RAW", "FACE_RAW_C", "Square Shoulder", "Top of the Screen Raw","Top of the Screen Peak_Hold", "ENVIR_AVE", "ENVIR_RAW", "SENSOR" , "Calib_Temp" , "Envir" , "Face"]
            with open(PG.filecsv, mode='w') as myfile:
                myfile = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                myfile.writerow(face)
        else:
            self.m_textCtrl_log.SetValue("CREATE FILE")
            PG.setlog = 0
    def m_button_onSensorOnButtonClick( self, event ):
        if(PG.setSensor == 0):
            PG.setSensor = 1
            self.m_textCtrl_onSenser.SetValue("ON")
        else:
            PG.setSensor = 0
            self.m_textCtrl_onSenser.SetValue("OFF")

    def m_button_temp_envirFaceChangeDownOnButtonClick( self, event ):
        PG.values2 = round(float(PG.values2) - 0.01, 2)
        self.m_textCtrl_facechange.SetValue(str(PG.values2))

    def m_button_temp_envirFaceChangeUpOnButtonClick( self, event ):
        PG.values2 = round(float(PG.values2) + 0.01, 2)
        self.m_textCtrl_facechange.SetValue(str(PG.values2))

    def m_button_temp_envirFaceChangeDown1OnButtonClick( self, event ):
        PG.values6 = round(float(PG.values6) - 0.01, 2)
        self.m_textCtrl_facechange1.SetValue(str(PG.values6))

    def m_button_temp_envirFaceChangeUp1OnButtonClick( self, event ):
        PG.values6 = round(float(PG.values6) + 0.01, 2)
        self.m_textCtrl_facechange1.SetValue(str(PG.values6))

    def m_button_temp_envirFaceChangeDown2OnButtonClick( self, event ):
        PG.values7 = round(float(PG.values7) - 0.01, 2)
        self.m_textCtrl_facechange2.SetValue(str(PG.values7))

    def m_button_temp_envirFaceChangeUp2OnButtonClick( self, event ):
        PG.values7 = round(float(PG.values7) + 0.01, 2)
        self.m_textCtrl_facechange2.SetValue(str(PG.values7))

    def m_textCtrl_facechangeOnLeftDClick( self, event ):
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show")

    def m_textCtrl_facechange1OnLeftDClick( self, event ):
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show")

    def m_textCtrl_facechange2OnLeftDClick( self, event ):
        os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show")

    def m_textCtrl_facechangeOnCharHook( self, event ):
        if event.GetKeyCode() ==13:
            try:
               PG.values2 = float(self.m_textCtrl_facechange.GetValue())
            except:
                self.m_textCtrl_facechange.SetValue(str(PG.values6))
            os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
        else:
            event.Skip()
    def m_textCtrl_facechange1OnCharHook( self, event ):
        if event.GetKeyCode() ==13:
            try:
               PG.values6 = float(self.m_textCtrl_facechange1.GetValue())
            except:
                self.m_textCtrl_facechange1.SetValue(str(PG.values6))
            
            os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
        else:
            event.Skip()

    def m_textCtrl_facechange2OnCharHook( self, event ):
        if event.GetKeyCode() ==13:
            try:
               PG.values7 = float(self.m_textCtrl_facechange2.GetValue())
            except:
                self.m_textCtrl_facechange2.SetValue(str(PG.values7))
            
            os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
        else:
            event.Skip()

#*******change1*******
def getValue():
    global f0
    f0 = open(PG.file_path + "/folderSetting/setting","r")
    setting = f0.readlines()
    PG.values0 = setting[0].strip('\n') #fevertemp
    PG.values1 = setting[1].strip('\n') #valuektoc
    PG.values2 = setting[2].strip('\n') #color_mode
    PG.values3 = setting[3].strip('\n') #move_leftright
    PG.values4 = setting[4].strip('\n') #move_topbottom
    PG.values5 = setting[5].strip('\n') #zoom
    PG.FFC_mode = setting[6].strip('\n') #zoom
    PG.values6 = setting[7].strip('\n') 
    PG.values7 = setting[8].strip('\n') 
    PG.values8 = setting[9].strip('\n') 
    f0.close()
def saveValue():
    global f1
    f1 = open(PG.file_path + "/folderSetting/setting","w")
    f1.write(PG.values0 + "\n")
    f1.write(PG.values1 + "\n")
    f1.write(PG.values2 + "\n")
    f1.write(PG.values3 + "\n")
    f1.write(PG.values4 + "\n")
    f1.write(PG.values5 + "\n")
    f1.write(PG.FFC_mode + "\n")
    f1.write(PG.values6 + "\n")
    f1.write(PG.values7 + "\n")
    f1.write(PG.values8 + "\n")
    f1.close()
def getValueReset():
    global f2
    f2 = open(PG.file_path + "/folderSetting/reset","r")
    reset = f2.readlines()
    PG.values0 = reset[0].strip('\n') #fevertemp
    PG.values1 = reset[1].strip('\n') #valuektoc
    PG.values2 = reset[2].strip('\n') #color_mode
    PG.values3 = reset[3].strip('\n') #move_leftright
    PG.values4 = reset[4].strip('\n') #move_topbottom
    PG.values5 = reset[5].strip('\n') #zoom
    PG.FFC_mode = reset[6].strip('\n') #zoom
    PG.values6 = reset[7].strip('\n') 
    PG.values7 = reset[8].strip('\n') 
    PG.values8 = reset[9].strip('\n') 
    f2.close()
def py_frame_callback(frame, userptr):
    array_pointer = cast(frame.contents.data, POINTER(c_uint16 * (frame.contents.width * frame.contents.height)))
    data = np.frombuffer(
        array_pointer.contents, dtype=np.dtype(np.uint16)).reshape(frame.contents.height, frame.contents.width)
    if frame.contents.data_bytes != (2 * frame.contents.width * frame.contents.height):
        return
    if not q.full():
        q.put(data)
PTR_PY_FRAME_CALLBACK = CFUNCTYPE(None, POINTER(uvc_frame), c_void_p)(py_frame_callback)
#**********************
def generate_colour_map():
    colorMapType = 0 #change
    """
    Conversion of the colour map from GetThermal to a numpy LUT:
        https://github.com/groupgets/GetThermal/blob/bb467924750a686cc3930f7e3a253818b755a2c0/src/dataformatter.cpp#L6
    """

    lut = np.zeros((256, 1, 3), dtype=np.uint8)

    #colorMaps 
    colormap_grayscale = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34, 34, 34, 35, 35, 35, 36, 36, 36, 37, 37, 37, 38, 38, 38, 39, 39, 39, 40, 40, 40, 41, 41, 41, 42, 42, 42, 43, 43, 43, 44, 44, 44, 45, 45, 45, 46, 46, 46, 47, 47, 47, 48, 48, 48, 49, 49, 49, 50, 50, 50, 51, 51, 51, 52, 52, 52, 53, 53, 53, 54, 54, 54, 55, 55, 55, 56, 56, 56, 57, 57, 57, 58, 58, 58, 59, 59, 59, 60, 60, 60, 61, 61, 61, 62, 62, 62, 63, 63, 63, 64, 64, 64, 65, 65, 65, 66, 66, 66, 67, 67, 67, 68, 68, 68, 69, 69, 69, 70, 70, 70, 71, 71, 71, 72, 72, 72, 73, 73, 73, 74, 74, 74, 75, 75, 75, 76, 76, 76, 77, 77, 77, 78, 78, 78, 79, 79, 79, 80, 80, 80, 81, 81, 81, 82, 82, 82, 83, 83, 83, 84, 84, 84, 85, 85, 85, 86, 86, 86, 87, 87, 87, 88, 88, 88, 89, 89, 89, 90, 90, 90, 91, 91, 91, 92, 92, 92, 93, 93, 93, 94, 94, 94, 95, 95, 95, 96, 96, 96, 97, 97, 97, 98, 98, 98, 99, 99, 99, 100, 100, 100, 101, 101, 101, 102, 102, 102, 103, 103, 103, 104, 104, 104, 105, 105, 105, 106, 106, 106, 107, 107, 107, 108, 108, 108, 109, 109, 109, 110, 110, 110, 111, 111, 111, 112, 112, 112, 113, 113, 113, 114, 114, 114, 115, 115, 115, 116, 116, 116, 117, 117, 117, 118, 118, 118, 119, 119, 119, 120, 120, 120, 121, 121, 121, 122, 122, 122, 123, 123, 123, 124, 124, 124, 125, 125, 125, 126, 126, 126, 127, 127, 127, 128, 128, 128, 129, 129, 129, 130, 130, 130, 131, 131, 131, 132, 132, 132, 133, 133, 133, 134, 134, 134, 135, 135, 135, 136, 136, 136, 137, 137, 137, 138, 138, 138, 139, 139, 139, 140, 140, 140, 141, 141, 141, 142, 142, 142, 143, 143, 143, 144, 144, 144, 145, 145, 145, 146, 146, 146, 147, 147, 147, 148, 148, 148, 149, 149, 149, 150, 150, 150, 151, 151, 151, 152, 152, 152, 153, 153, 153, 154, 154, 154, 155, 155, 155, 156, 156, 156, 157, 157, 157, 158, 158, 158, 159, 159, 159, 160, 160, 160, 161, 161, 161, 162, 162, 162, 163, 163, 163, 164, 164, 164, 165, 165, 165, 166, 166, 166, 167, 167, 167, 168, 168, 168, 169, 169, 169, 170, 170, 170, 171, 171, 171, 172, 172, 172, 173, 173, 173, 174, 174, 174, 175, 175, 175, 176, 176, 176, 177, 177, 177, 178, 178, 178, 179, 179, 179, 180, 180, 180, 181, 181, 181, 182, 182, 182, 183, 183, 183, 184, 184, 184, 185, 185, 185, 186, 186, 186, 187, 187, 187, 188, 188, 188, 189, 189, 189, 190, 190, 190, 191, 191, 191, 192, 192, 192, 193, 193, 193, 194, 194, 194, 195, 195, 195, 196, 196, 196, 197, 197, 197, 198, 198, 198, 199, 199, 199, 200, 200, 200, 201, 201, 201, 202, 202, 202, 203, 203, 203, 204, 204, 204, 205, 205, 205, 206, 206, 206, 207, 207, 207, 208, 208, 208, 209, 209, 209, 210, 210, 210, 211, 211, 211, 212, 212, 212, 213, 213, 213, 214, 214, 214, 215, 215, 215, 216, 216, 216, 217, 217, 217, 218, 218, 218, 219, 219, 219, 220, 220, 220, 221, 221, 221, 222, 222, 222, 223, 223, 223, 224, 224, 224, 225, 225, 225, 226, 226, 226, 227, 227, 227, 228, 228, 228, 229, 229, 229, 230, 230, 230, 231, 231, 231, 232, 232, 232, 233, 233, 233, 234, 234, 234, 235, 235, 235, 236, 236, 236, 237, 237, 237, 238, 238, 238, 239, 239, 239, 240, 240, 240, 241, 241, 241, 242, 242, 242, 243, 243, 243, 244, 244, 244, 245, 245, 245, 246, 246, 246, 247, 247, 247, 248, 248, 248, 249, 249, 249, 250, 250, 250, 251, 251, 251, 252, 252, 252, 253, 253, 253, 254, 254, 254, 255, 255, 255];

    colormap_rainbow = [1, 3, 74, 0, 3, 74, 0, 3, 75, 0, 3, 75, 0, 3, 76, 0, 3, 76, 0, 3, 77, 0, 3, 79, 0, 3, 82, 0, 5, 85, 0, 7, 88, 0, 10, 91, 0, 14, 94, 0, 19, 98, 0, 22, 100, 0, 25, 103, 0, 28, 106, 0, 32, 109, 0, 35, 112, 0, 38, 116, 0, 40, 119, 0, 42, 123, 0, 45, 128, 0, 49, 133, 0, 50, 134, 0, 51, 136, 0, 52, 137, 0, 53, 139, 0, 54, 142, 0, 55, 144, 0, 56, 145, 0, 58, 149, 0, 61, 154, 0, 63, 156, 0, 65, 159, 0, 66, 161, 0, 68, 164, 0, 69, 167, 0, 71, 170, 0, 73, 174, 0, 75, 179, 0, 76, 181, 0, 78, 184, 0, 79, 187, 0, 80, 188, 0, 81, 190, 0, 84, 194, 0, 87, 198, 0, 88, 200, 0, 90, 203, 0, 92, 205, 0, 94, 207, 0, 94, 208, 0, 95, 209, 0, 96, 210, 0, 97, 211, 0, 99, 214, 0, 102, 217, 0, 103, 218, 0, 104, 219, 0, 105, 220, 0, 107, 221, 0, 109, 223, 0, 111, 223, 0, 113, 223, 0, 115, 222, 0, 117, 221, 0, 118, 220, 1, 120, 219, 1, 122, 217, 2, 124, 216, 2, 126, 214, 3, 129, 212, 3, 131, 207, 4, 132, 205, 4, 133, 202, 4, 134, 197, 5, 136, 192, 6, 138, 185, 7, 141, 178, 8, 142, 172, 10, 144, 166, 10, 144, 162, 11, 145, 158, 12, 146, 153, 13, 147, 149, 15, 149, 140, 17, 151, 132, 22, 153, 120, 25, 154, 115, 28, 156, 109, 34, 158, 101, 40, 160, 94, 45, 162, 86, 51, 164, 79, 59, 167, 69, 67, 171, 60, 72, 173, 54, 78, 175, 48, 83, 177, 43, 89, 179, 39, 93, 181, 35, 98, 183, 31, 105, 185, 26, 109, 187, 23, 113, 188, 21, 118, 189, 19, 123, 191, 17, 128, 193, 14, 134, 195, 12, 138, 196, 10, 142, 197, 8, 146, 198, 6, 151, 200, 5, 155, 201, 4, 160, 203, 3, 164, 204, 2, 169, 205, 2, 173, 206, 1, 175, 207, 1, 178, 207, 1, 184, 208, 0, 190, 210, 0, 193, 211, 0, 196, 212, 0, 199, 212, 0, 202, 213, 1, 207, 214, 2, 212, 215, 3, 215, 214, 3, 218, 214, 3, 220, 213, 3, 222, 213, 4, 224, 212, 4, 225, 212, 5, 226, 212, 5, 229, 211, 5, 232, 211, 6, 232, 211, 6, 233, 211, 6, 234, 210, 6, 235, 210, 7, 236, 209, 7, 237, 208, 8, 239, 206, 8, 241, 204, 9, 242, 203, 9, 244, 202, 10, 244, 201, 10, 245, 200, 10, 245, 199, 11, 246, 198, 11, 247, 197, 12, 248, 194, 13, 249, 191, 14, 250, 189, 14, 251, 187, 15, 251, 185, 16, 252, 183, 17, 252, 178, 18, 253, 174, 19, 253, 171, 19, 254, 168, 20, 254, 165, 21, 254, 164, 21, 255, 163, 22, 255, 161, 22, 255, 159, 23, 255, 157, 23, 255, 155, 24, 255, 149, 25, 255, 143, 27, 255, 139, 28, 255, 135, 30, 255, 131, 31, 255, 127, 32, 255, 118, 34, 255, 110, 36, 255, 104, 37, 255, 101, 38, 255, 99, 39, 255, 93, 40, 255, 88, 42, 254, 82, 43, 254, 77, 45, 254, 69, 47, 254, 62, 49, 253, 57, 50, 253, 53, 52, 252, 49, 53, 252, 45, 55, 251, 39, 57, 251, 33, 59, 251, 32, 60, 251, 31, 60, 251, 30, 61, 251, 29, 61, 251, 28, 62, 250, 27, 63, 250, 27, 65, 249, 26, 66, 249, 26, 68, 248, 25, 70, 248, 24, 73, 247, 24, 75, 247, 25, 77, 247, 25, 79, 247, 26, 81, 247, 32, 83, 247, 35, 85, 247, 38, 86, 247, 42, 88, 247, 46, 90, 247, 50, 92, 248, 55, 94, 248, 59, 96, 248, 64, 98, 248, 72, 101, 249, 81, 104, 249, 87, 106, 250, 93, 108, 250, 95, 109, 250, 98, 110, 250, 100, 111, 251, 101, 112, 251, 102, 113, 251, 109, 117, 252, 116, 121, 252, 121, 123, 253, 126, 126, 253, 130, 128, 254, 135, 131, 254, 139, 133, 254, 144, 136, 254, 151, 140, 255, 158, 144, 255, 163, 146, 255, 168, 149, 255, 173, 152, 255, 176, 153, 255, 178, 155, 255, 184, 160, 255, 191, 165, 255, 195, 168, 255, 199, 172, 255, 203, 175, 255, 207, 179, 255, 211, 182, 255, 216, 185, 255, 218, 190, 255, 220, 196, 255, 222, 200, 255, 225, 202, 255, 227, 204, 255, 230, 206, 255, 233, 208]

    colourmap_ironblack = [
        255, 255, 255, 253, 253, 253, 251, 251, 251, 249, 249, 249, 247, 247,
        247, 245, 245, 245, 243, 243, 243, 241, 241, 241, 239, 239, 239, 237,
        237, 237, 235, 235, 235, 233, 233, 233, 231, 231, 231, 229, 229, 229,
        227, 227, 227, 225, 225, 225, 223, 223, 223, 221, 221, 221, 219, 219,
        219, 217, 217, 217, 215, 215, 215, 213, 213, 213, 211, 211, 211, 209,
        209, 209, 207, 207, 207, 205, 205, 205, 203, 203, 203, 201, 201, 201,
        199, 199, 199, 197, 197, 197, 195, 195, 195, 193, 193, 193, 191, 191,
        191, 189, 189, 189, 187, 187, 187, 185, 185, 185, 183, 183, 183, 181,
        181, 181, 179, 179, 179, 177, 177, 177, 175, 175, 175, 173, 173, 173,
        171, 171, 171, 169, 169, 169, 167, 167, 167, 165, 165, 165, 163, 163,
        163, 161, 161, 161, 159, 159, 159, 157, 157, 157, 155, 155, 155, 153,
        153, 153, 151, 151, 151, 149, 149, 149, 147, 147, 147, 145, 145, 145,
        143, 143, 143, 141, 141, 141, 139, 139, 139, 137, 137, 137, 135, 135,
        135, 133, 133, 133, 131, 131, 131, 129, 129, 129, 126, 126, 126, 124,
        124, 124, 122, 122, 122, 120, 120, 120, 118, 118, 118, 116, 116, 116,
        114, 114, 114, 112, 112, 112, 110, 110, 110, 108, 108, 108, 106, 106,
        106, 104, 104, 104, 102, 102, 102, 100, 100, 100, 98, 98, 98, 96, 96,
        96, 94, 94, 94, 92, 92, 92, 90, 90, 90, 88, 88, 88, 86, 86, 86, 84, 84,
        84, 82, 82, 82, 80, 80, 80, 78, 78, 78, 76, 76, 76, 74, 74, 74, 72, 72,
        72, 70, 70, 70, 68, 68, 68, 66, 66, 66, 64, 64, 64, 62, 62, 62, 60, 60,
        60, 58, 58, 58, 56, 56, 56, 54, 54, 54, 52, 52, 52, 50, 50, 50, 48, 48,
        48, 46, 46, 46, 44, 44, 44, 42, 42, 42, 40, 40, 40, 38, 38, 38, 36, 36,
        36, 34, 34, 34, 32, 32, 32, 30, 30, 30, 28, 28, 28, 26, 26, 26, 24, 24,
        24, 22, 22, 22, 20, 20, 20, 18, 18, 18, 16, 16, 16, 14, 14, 14, 12, 12,
        12, 10, 10, 10, 8, 8, 8, 6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 0, 0, 9,
        2, 0, 16, 4, 0, 24, 6, 0, 31, 8, 0, 38, 10, 0, 45, 12, 0, 53, 14, 0,
        60, 17, 0, 67, 19, 0, 74, 21, 0, 82, 23, 0, 89, 25, 0, 96, 27, 0, 103,
        29, 0, 111, 31, 0, 118, 36, 0, 120, 41, 0, 121, 46, 0, 122, 51, 0, 123,
        56, 0, 124, 61, 0, 125, 66, 0, 126, 71, 0, 127, 76, 1, 128, 81, 1, 129,
        86, 1, 130, 91, 1, 131, 96, 1, 132, 101, 1, 133, 106, 1, 134, 111, 1,
        135, 116, 1, 136, 121, 1, 136, 125, 2, 137, 130, 2, 137, 135, 3, 137,
        139, 3, 138, 144, 3, 138, 149, 4, 138, 153, 4, 139, 158, 5, 139, 163,
        5, 139, 167, 5, 140, 172, 6, 140, 177, 6, 140, 181, 7, 141, 186, 7,
        141, 189, 10, 137, 191, 13, 132, 194, 16, 127, 196, 19, 121, 198, 22,
        116, 200, 25, 111, 203, 28, 106, 205, 31, 101, 207, 34, 95, 209, 37,
        90, 212, 40, 85, 214, 43, 80, 216, 46, 75, 218, 49, 69, 221, 52, 64,
        223, 55, 59, 224, 57, 49, 225, 60, 47, 226, 64, 44, 227, 67, 42, 228,
        71, 39, 229, 74, 37, 230, 78, 34, 231, 81, 32, 231, 85, 29, 232, 88,
        27, 233, 92, 24, 234, 95, 22, 235, 99, 19, 236, 102, 17, 237, 106, 14,
        238, 109, 12, 239, 112, 12, 240, 116, 12, 240, 119, 12, 241, 123, 12,
        241, 127, 12, 242, 130, 12, 242, 134, 12, 243, 138, 12, 243, 141, 13,
        244, 145, 13, 244, 149, 13, 245, 152, 13, 245, 156, 13, 246, 160, 13,
        246, 163, 13, 247, 167, 13, 247, 171, 13, 248, 175, 14, 248, 178, 15,
        249, 182, 16, 249, 185, 18, 250, 189, 19, 250, 192, 20, 251, 196, 21,
        251, 199, 22, 252, 203, 23, 252, 206, 24, 253, 210, 25, 253, 213, 27,
        254, 217, 28, 254, 220, 29, 255, 224, 30, 255, 227, 39, 255, 229, 53,
        255, 231, 67, 255, 233, 81, 255, 234, 95, 255, 236, 109, 255, 238, 123,
        255, 240, 137, 255, 242, 151, 255, 244, 165, 255, 246, 179, 255, 248,
        193, 255, 249, 207, 255, 251, 221, 255, 253, 235, 255, 255, 24]

    def chunk(ulist, step):
        return map(lambda i: ulist[i: i + step], range(0, len(ulist), step))

    if (colorMapType == 1):
        chunks = chunk(colormap_rainbow, 3)
    elif (colorMapType == 2):
        chunks = chunk(colormap_grayscale, 3)
    else:
        chunks = chunk(colourmap_ironblack, 3)

    red = []
    green = []
    blue = []

    for chunk in chunks:
        red.append(chunk[0])
        green.append(chunk[1])
        blue.append(chunk[2])

    lut[:, 0, 0] = blue

    lut[:, 0, 1] = green

    lut[:, 0, 2] = red

    return lut
#*****************************
def startStream():
  PG.ctx = POINTER(uvc_context)()
  PG.dev = POINTER(uvc_device)()
  PG.devh = POINTER(uvc_device_handle)()
  PG.ctrl = uvc_stream_ctrl()
  res = libuvc.uvc_init(byref(PG.ctx), 0)
  if res < 0:
    print("[ERR] uvc_init error")
    #exit(1)

  try:
    res = libuvc.uvc_find_device(PG.ctx, byref(PG.dev), PT_USB_VID, PT_USB_PID, 0)
    if res < 0:
      print("[ERR] uvc_find_device error")
      exit(1)

    try:
      res = libuvc.uvc_open(PG.dev, byref(PG.devh))
      if res < 0:
        print("[ERR] uvc_open error")
        exit(1)

      print("[INFO] Thermal camera opened!")

      #print_device_info(PG.devh)
      #print_device_formats(PG.devh)

      frame_formats = uvc_get_frame_formats_by_guid(PG.devh, VS_FMT_GUID_Y16)
      if len(frame_formats) == 0:
        print("[ERR] device does not support Y16")
        exit(1)

      libuvc.uvc_get_stream_ctrl_format_size(PG.devh, byref(PG.ctrl), UVC_FRAME_FORMAT_Y16,
        frame_formats[0].wWidth, frame_formats[0].wHeight, int(1e7 / frame_formats[0].dwDefaultFrameInterval)
      )

      res = libuvc.uvc_start_streaming(PG.devh, byref(PG.ctrl), PTR_PY_FRAME_CALLBACK, None, 0)
      if res < 0:
        print("[ERR] uvc_start_streaming failed: {0}".format(res))
        exit(1)

      #print("done starting stream, displaying settings")
      #      #print("resetting settings to default")

      set_manual_ffc(PG.devh)
      set_gain_high(PG.devh)
      #print("current settings")
      #print_shutter_info(PG.devh)

    except:
      #libuvc.uvc_unref_device(dev)
      print('[ERR] Failed to Open Device')
  except:
    #libuvc.uvc_exit(PG.ctx)
    print('[ERR] Failed to Find Device')

def raw_to_8bit(data):
  cv.normalize(data, data, 0, 65535, cv.NORM_MINMAX)
  np.right_shift(data, 8, data)
  return cv.cvtColor(np.uint8(data), cv.COLOR_GRAY2RGB)
  
def ktoc(val):
    val = round(((val - 27315) / 100.0), 2)
    #val = round( 0.026 * (val - 8192) + 40.6,2)
    return val#change
    
def calib_ktoc(val):
    return val + float(PG.values1)

def Check_camera_index():
    index_camera_thermal = '1'
    index_normal_camera = '0'
    try:
        os.system('rm camera_id.txt')
    except:
        pass
    os.system('v4l2-ctl --list-devices >> camera_id.txt')

    camedid_from_file = open("camera_id.txt","r")
    camera_id = camedid_from_file.readlines()
    #print(camedid_from_file)
    print(camera_id)
    
    camera_id1 = camera_id[0]
    if camera_id1.find('PureThermal') == -1:
        camera_thermal = 3
        camera_webcam = 0
    else:
        camera_thermal = 0
        camera_webcam = 3
    try:
        index_normal_camera = camera_id[camera_webcam+1].replace('\t', '')
        index_normal_camera = index_normal_camera.replace('\n', '')
    except:
        print('[ERR] Can not find webcam')
    try:
        index_camera_thermal = camera_id[camera_thermal+1].replace('\t', '')
        index_camera_thermal = index_camera_thermal.replace('\n', '')
    except:
        print('[ERR] Can not find Tcameras')
    return index_camera_thermal, index_normal_camera

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def Load_model():
    sub_folder = "model_face_detect"
    print('[INFO] LOADING MASKED FACE DATA')
    labelsPath = os.path.sep.join([sub_folder, "coco.names"])
    weightsPath = os.path.sep.join([sub_folder, "yolov3.weights"])
    configPath = os.path.sep.join([sub_folder, "yolov3.cfg"])
    LABELS = open(labelsPath).read().strip().split("\n")
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
        dtype="uint8")
    try:
        net = cv.dnn.readNetFromDarknet(configPath, weightsPath)

        net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        print("[INFO] USING GPU CUDA...")
    except:
        print("[INFO] NO GPU support...")
        
    return net, ln, COLORS

def get_ip_address():
    try :
        socket.gethostbyname(socket.gethostname())
        return socket.gethostbyname(socket.gethostname())
    except:
        return 'NULL'
          
def ctok(val):
    return (val * 100.0) + 27315

def init_parameter():
    PG.net, PG.ln, PG.COLORS = Load_model()
    pygame.mixer.init()
    pygame.mixer.music.load("gui-folder/beep-08b.mp3")
    getValue()
    PG.IP_addr = get_ip_address()

def pre_init_Tcamera(index):
    try:
        import run1
        run1.main()
        print('[INFO] Pre init Tcamera')
    except:
        print('[WARN] Can not pre init Tcamera')
    


#*****************************
#       Main program
#*****************************
def main():
    #run1.main()
    PG.file_path = str(GetPath.get_path())
    print('='*20)
    #time.sleep(10)
    print(datetime.now())
    print('[INFO] Checking camera ....')
    index_Tcamera, index_Ncamera = Check_camera_index()
    pre_init_Tcamera(index_Tcamera)
    print(' Index_Tcamera = ',index_Tcamera, end =' ')
    print('Index_Ncamera = ',index_Ncamera)
    PG.cam = cv.VideoCapture(index_Ncamera, cv.CAP_V4L)
    print('[INFO] Webcam openned!')
    PG.cam.set(cv.CAP_PROP_BUFFERSIZE, 1)
    PG.cam.set(cv.CAP_PROP_FRAME_WIDTH,640)
    PG.cam.set(cv.CAP_PROP_FRAME_HEIGHT,480)
    print("[FEVER DETECTOR] STARTING PROGRAM")
    time.sleep(3)
    init_parameter()
    startStream()
    PG.Main_App =  face_recognition_app(None)
    PG.Main_Frame = face_recognition_frame(None)
    PG.Main_Frame.Show()
    PG.Main_App.MainLoop()
#*****************************  
def open_serial_port():
    try:
        ser = serial.Serial('/dev/ttyUSB0',19200, timeout=10)
        print('[INFO] CONNECTED TO ARDUINO/DS18B20 SENSOR....')
        return ser
    except:
        ser = serial.Serial('/dev/ttyACM0',19200, timeout=10)
        print('[ERR] CAN NOT CONNECT TO ARDUINO/DS18B20 SENSOR....')
        return ser
def read_ds18b20(DS18B20_ser):
    DS18B20_bytes = DS18B20_ser.readline()
    DS18B20_str = DS18B20_bytes.decode("utf-8") 
    DS18B20_float = float(DS18B20_str)
    return DS18B20_float
def main2():
    time.sleep(10)
    os.system("dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide")
    PG.App_Running = True
    try:
        PG.DS18B20_ser = open_serial_port()
    except:
        pass
    
    while PG.App_Running:
        if(PG.setSensor == 0):
            time.sleep(5)
            PG.TempSensor = 0
        else:
            try:
                if(PG.DS18B20_ser is not None):
                    PG.TempSensor = read_ds18b20(PG.DS18B20_ser)
                    PG.TempSensor = round_down(PG.TempSensor, 1)
            except:
                PG.TempSensor = 0

d = threading.Thread(name='main', target=main)
d.setDaemon(True)
t = threading.Thread(name='main2', target=main2)
d.start()
t.start()
