# Các biến toàn cục của chương trình
App_Running     = False
App_Recogniting = True
VM_Delay        = 19 / 1000.0
Main_Frame      = None
Show_Data       = None
Main_App        = None
add_del = 0
frame           = None # Biến lưu frame của camera
frame2          = None # Biến lưu frame của camera
data            = None # Biến lưu frame của camera
frame_cut		= None # Biến lưu frame cuted when recognition
frame_env		= None
frame_add_face  = None # Biến lưu frame cho add face
view            = False # biến cho phép hiển thị
time_clear = None
cam             = None # Đối tượng camera
cam2             = None # Đối tượng camera
error = 0
login           = False
#******************************************
values0 = "0" #fevertemp
values1 = "0" #valuektoc
values2 = "0" #color_mode
values3 = "0" #move_topbottom
values4 = "0" #move_leftright
values5 = "0" #zoom
values6 = "0" #move_topbottom
values7 = "0" #move_leftright
values8 = "0" #zoom
setting = 0
net = None
ln = None
COLORS = None
IP_addr = None
dev = None
ctx = None
devh = None
ctrl = None
FFC_mode = '0'
Temp_text = 0.0
Temp_text_backup = 0.0
color_rec = (255,255,255)
color_rec2 = (0,0,255)
#********
data_run = 0
agv_envir = 0.0
DS18B20_ser = None
TempEnvirRaw = 0.0
TempSensor = 0.0
auto_calib_temp = 0.0
##########################
data_temp = []
data_envir = []
data_temp_raw = []
data_envir_raw = []
agv_temp_raw = 0.0
agv_envir_raw = 0.0
########
flag_get_temp = 0
##########################
TempEnvirDefault = 0.0
TempSensorDefault = 0.0
arrayEnvir100 = []
Previous_Time2 = 0.0
TempE = 0.0
TempF = 0.0
TempG = 0.0
change1 = 0
change2 = 0
############
filecsv = ""
setlog = 0
setSensor = 0
valueG = 0
valueF = 0
calibFaceAve = 0.0
calibEnvirAve = 0.0

##########
showSquare = 0.0
showTopofScreen = 0.0
showTopofScreenRaw = 0.0
indexStep = 0
DisplayviaHDMI = True
file_path = ""
Temp_text_on_top = "カメラに近づいて下さい"#Come up to the camera

faceChange = ""
envirFirst25 = 0.0
face_c = 0.0
faceRawShow = 0.0
runSetting = 0

#################
TempLevelLow = 20
TempLevelHigh = 23

normalTemp = 0
timeNormalTemp = 0