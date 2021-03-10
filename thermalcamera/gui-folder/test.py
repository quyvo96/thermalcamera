from gui import *
import wx

class main_app(wx.App):
	def __int__(self):
		print("afds")
	def MainLoop(self):
		print("ok")
app = wx.App(None)
frame = frame_main1(None)
frame.Show()
app.MainLoop()
