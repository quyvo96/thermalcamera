# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frame_main1
###########################################################################

class frame_main1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ASTI@ARV - THERMOGRAPHY FACIAL RECOGNITION SYSTEM", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"gui-folder/Logo-Arv.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_bitmap_logo.SetMinSize( wx.Size( 220,90 ) )
		self.m_bitmap_logo.SetMaxSize( wx.Size( 220,90 ) )

		bSizer53.Add( self.m_bitmap_logo, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer53, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"THERMOGRAPHY FACIAL RECOGNITION SYSTEM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		self.m_staticText_info.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_info.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer54.Add( self.m_staticText_info, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.EXPAND, 5 )


		bSizer4.Add( bSizer54, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer32.SetMinSize( wx.Size( -1,60 ) )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_setting = wx.Button( self, wx.ID_ANY, u"SETTING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_setting.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_button_setting.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer33.Add( self.m_button_setting, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		bSizer34.SetMinSize( wx.Size( 50,-1 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer34.Add( self.m_staticText11, 0, wx.ALL, 5 )


		bSizer32.Add( bSizer34, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2.SetMinSize( wx.Size( -1,550 ) )
		bSizer69 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_video = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 640,480 ), wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )
		self.m_panel_video.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel_video.SetMinSize( wx.Size( 640,480 ) )

		bSizer69.Add( self.m_panel_video, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer69, 0, 0, 5 )

		bSizer691 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_video_thermography = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 640,480 ), wx.TAB_TRAVERSAL )
		self.m_panel_video_thermography.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel_video_thermography.SetMinSize( wx.Size( 640,480 ) )

		bSizer691.Add( self.m_panel_video_thermography, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer691, 0, 0, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_setting = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_setting.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
		self.m_panel_setting.Hide()

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Fever Temperature:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer20.Add( self.m_staticText7, 0, wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_fever = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl_fever, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer27.Add( self.m_button14, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer27, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Calib Tem Calcualator :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer21.Add( self.m_staticText6, 0, wx.ALL, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_ktoc = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_textCtrl_ktoc, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer26.Add( self.m_button13, 0, wx.ALL, 5 )


		bSizer21.Add( bSizer26, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Thermal dispaly mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer28.Add( self.m_staticText9, 0, wx.ALL, 5 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_mode0 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer29.Add( self.m_button_mode0, 0, wx.ALL, 5 )

		self.m_button_mode1 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer29.Add( self.m_button_mode1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_mode2 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer29.Add( self.m_button_mode2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer28.Add( bSizer29, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer25.Add( bSizer28, 0, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText71 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Calib camera :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		bSizer22.Add( self.m_staticText71, 0, wx.ALL, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_moveup = wx.Button( self.m_panel_setting, wx.ID_ANY, u"▲", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_button_moveup, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( bSizer23, 0, wx.EXPAND, 5 )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_moveleft = wx.Button( self.m_panel_setting, wx.ID_ANY, u"◄", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.m_button_moveleft, 0, wx.ALL, 5 )

		self.m_button_moveright = wx.Button( self.m_panel_setting, wx.ID_ANY, u"►", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.m_button_moveright, 0, wx.ALL, 5 )


		bSizer22.Add( bSizer241, 0, wx.EXPAND, 5 )

		bSizer251 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_movebottom = wx.Button( self.m_panel_setting, wx.ID_ANY, u"▼", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer251.Add( self.m_button_movebottom, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( bSizer251, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer25.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer261 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Change detect size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer261.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer271 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_room = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.m_button_room, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button_roomout = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.m_button_roomout, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer261.Add( bSizer271, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer25.Add( bSizer261, 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer41.Add( self.m_staticText12, 0, wx.ALL, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_save = wx.Button( self.m_panel_setting, wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_button_save, 0, wx.ALL, 5 )

		self.m_button_out = wx.Button( self.m_panel_setting, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_button_out, 0, wx.ALL, 5 )


		bSizer41.Add( bSizer37, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer25.Add( bSizer41, 1, wx.EXPAND, 5 )


		self.m_panel_setting.SetSizer( bSizer25 )
		self.m_panel_setting.Layout()
		bSizer25.Fit( self.m_panel_setting )
		bSizer24.Add( self.m_panel_setting, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer24, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_statusBar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.frame_mainOnClose )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.m_button_settingOnButtonClick )
		self.m_panel_video.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_videoOnEraseBackground )
		self.m_panel_video.Bind( wx.EVT_PAINT, self.m_panel_videoOnPaint )
		self.m_panel_video_thermography.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_video_thermographyOnEraseBackground )
		self.m_panel_video_thermography.Bind( wx.EVT_PAINT, self.m_panel_video_thermographyOnPaint )
		self.m_button14.Bind( wx.EVT_BUTTON, self.m_button14OnButtonClick )
		self.m_button13.Bind( wx.EVT_BUTTON, self.m_button13OnButtonClick )
		self.m_button_mode0.Bind( wx.EVT_BUTTON, self.m_button_mode0OnButtonClick )
		self.m_button_mode1.Bind( wx.EVT_BUTTON, self.m_button_mode1OnButtonClick )
		self.m_button_mode2.Bind( wx.EVT_BUTTON, self.m_button_mode2OnButtonClick )
		self.m_button_moveup.Bind( wx.EVT_BUTTON, self.m_button_moveupOnButtonClick )
		self.m_button_moveleft.Bind( wx.EVT_BUTTON, self.m_button_moveleftOnButtonClick )
		self.m_button_moveright.Bind( wx.EVT_BUTTON, self.m_button_moverightOnButtonClick )
		self.m_button_movebottom.Bind( wx.EVT_BUTTON, self.m_button_movebottomOnButtonClick )
		self.m_button_room.Bind( wx.EVT_BUTTON, self.m_button_roomOnButtonClick )
		self.m_button_roomout.Bind( wx.EVT_BUTTON, self.m_button_roomoutOnButtonClick )
		self.m_button_save.Bind( wx.EVT_BUTTON, self.m_button_saveOnButtonClick )
		self.m_button_out.Bind( wx.EVT_BUTTON, self.m_button_outOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def frame_mainOnClose( self, event ):
		event.Skip()

	def m_button_settingOnButtonClick( self, event ):
		event.Skip()

	def m_panel_videoOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_videoOnPaint( self, event ):
		event.Skip()

	def m_panel_video_thermographyOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_video_thermographyOnPaint( self, event ):
		event.Skip()

	def m_button14OnButtonClick( self, event ):
		event.Skip()

	def m_button13OnButtonClick( self, event ):
		event.Skip()

	def m_button_mode0OnButtonClick( self, event ):
		event.Skip()

	def m_button_mode1OnButtonClick( self, event ):
		event.Skip()

	def m_button_mode2OnButtonClick( self, event ):
		event.Skip()

	def m_button_moveupOnButtonClick( self, event ):
		event.Skip()

	def m_button_moveleftOnButtonClick( self, event ):
		event.Skip()

	def m_button_moverightOnButtonClick( self, event ):
		event.Skip()

	def m_button_movebottomOnButtonClick( self, event ):
		event.Skip()

	def m_button_roomOnButtonClick( self, event ):
		event.Skip()

	def m_button_roomoutOnButtonClick( self, event ):
		event.Skip()

	def m_button_saveOnButtonClick( self, event ):
		event.Skip()

	def m_button_outOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_Delete_Face
###########################################################################

class MyDialog_Delete_Face ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SETTING", pos = wx.DefaultPosition, size = wx.Size( 640,380 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 640,380 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyDialog_Delete_FaceOnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyDialog_Delete_FaceOnClose( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_Login
###########################################################################

class MyDialog_Login ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"CONFIRM", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText = wx.StaticText( self, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText.Wrap( -1 )

		bSizer9.Add( self.m_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,50 ), wx.TE_PASSWORD )
		self.m_textCtrl_password.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer9.Add( self.m_textCtrl_password, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		self.m_button_cancel.SetMinSize( wx.Size( 50,50 ) )

		bSizer7.Add( self.m_button_cancel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_confirm = wx.Button( self, wx.ID_ANY, u"CONFIRM", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
		self.m_button_confirm.SetMinSize( wx.Size( 50,50 ) )

		bSizer7.Add( self.m_button_confirm, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6.Add( bSizer7, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyDialog_LoginOnClose )
		self.m_textCtrl_password.Bind( wx.EVT_CHAR_HOOK, self.Enter_2_confirm )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.m_button_cancelOnButtonClick )
		self.m_button_confirm.Bind( wx.EVT_BUTTON, self.m_button_confirmOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyDialog_LoginOnClose( self, event ):
		event.Skip()

	def Enter_2_confirm( self, event ):
		event.Skip()

	def m_button_cancelOnButtonClick( self, event ):
		event.Skip()

	def m_button_confirmOnButtonClick( self, event ):
		event.Skip()


