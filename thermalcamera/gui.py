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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ASTI@ARV - THERMOGRAPHY FACIAL RECOGNITION SYSTEM Ver 1.1.6", pos = wx.DefaultPosition, size = wx.Size( 1920,1050 ), style = wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1920,1050 ), wx.Size( 1920,1050 ) )
		self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer53.SetMinSize( wx.Size( -1,150 ) )
		self.m_bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"gui-folder/gui-folder/Logo-Arv.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_bitmap_logo.Hide()
		self.m_bitmap_logo.SetMinSize( wx.Size( 220,90 ) )
		self.m_bitmap_logo.SetMaxSize( wx.Size( 220,90 ) )

		bSizer53.Add( self.m_bitmap_logo, 1, wx.ALL, 5 )


		bSizer4.Add( bSizer53, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"THERMOGRAPHY FACIAL RECOGNITION SYSTEM Ver1.0.3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		self.m_staticText_info.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_info.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText_info.Hide()

		bSizer54.Add( self.m_staticText_info, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer54, 1, wx.EXPAND, 5 )

		self.m_panel37 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,40 ), wx.TAB_TRAVERSAL )
		self.m_panel37.SetMinSize( wx.Size( -1,40 ) )
		self.m_panel37.SetMaxSize( wx.Size( -1,40 ) )

		bSizer4.Add( self.m_panel37, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Temperature:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 40, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText14.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText14.Hide()

		bSizer35.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl_temp = wx.TextCtrl( self, wx.ID_ANY, u"カメラに近づいて下さい", wx.DefaultPosition, wx.Size( 850,90 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_temp.SetFont( wx.Font( 50, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_textCtrl_temp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_textCtrl_temp.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_textCtrl_temp.SetMinSize( wx.Size( 850,90 ) )
		self.m_textCtrl_temp.SetMaxSize( wx.Size( 850,90 ) )

		bSizer35.Add( self.m_textCtrl_temp, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 28, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer35.Add( self.m_staticText13, 0, wx.ALL, 5 )


		bSizer34.Add( bSizer35, 0, 0, 5 )

		self.m_panel38 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,35 ), wx.TAB_TRAVERSAL )
		self.m_panel38.SetMinSize( wx.Size( -1,35 ) )
		self.m_panel38.SetMaxSize( wx.Size( -1,35 ) )

		bSizer34.Add( self.m_panel38, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer34, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2.SetMinSize( wx.Size( -1,650 ) )
		bSizer69 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_video = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,600 ), wx.BORDER_SUNKEN|wx.TAB_TRAVERSAL )
		self.m_panel_video.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_panel_video.SetMinSize( wx.Size( 800,600 ) )

		bSizer69.Add( self.m_panel_video, 0, wx.EXPAND, 5 )


		bSizer2.Add( bSizer69, 0, 0, 5 )

		bSizer691 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_video_thermography = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,600 ), wx.TAB_TRAVERSAL )
		self.m_panel_video_thermography.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_panel_video_thermography.SetMinSize( wx.Size( 800,600 ) )

		bSizer691.Add( self.m_panel_video_thermography, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer691, 0, 0, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer32.SetMinSize( wx.Size( -1,60 ) )
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer33.Add( ( 150, 0), 0, 0, 5 )

		self.m_button_exit = wx.Button( self, wx.ID_ANY, u"EXIT", wx.DefaultPosition, wx.Size( 120,60 ), 0 )
		self.m_button_exit.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button_exit.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_button_exit.SetMinSize( wx.Size( 120,60 ) )
		self.m_button_exit.SetMaxSize( wx.Size( 120,60 ) )

		bSizer33.Add( self.m_button_exit, 0, wx.ALL, 5 )

		self.m_button_setting = wx.Button( self, wx.ID_ANY, u"SETTING", wx.DefaultPosition, wx.Size( 120,60 ), 0 )
		self.m_button_setting.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_button_setting.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_button_setting.SetMinSize( wx.Size( 120,60 ) )

		bSizer33.Add( self.m_button_setting, 0, wx.ALL, 5 )

		self.m_button_data = wx.Button( self, wx.ID_ANY, u"SHOW DATA", wx.DefaultPosition, wx.Size( 120,60 ), 0 )
		self.m_button_data.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button_data.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_button_data.SetMinSize( wx.Size( 120,60 ) )
		self.m_button_data.SetMaxSize( wx.Size( 120,60 ) )

		bSizer33.Add( self.m_button_data, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer33, 0, 0, 5 )


		bSizer32.Add( bSizer30, 0, 0, 5 )


		bSizer32.Add( ( 30, 0), 1, wx.EXPAND, 5 )

		bSizer341 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_data = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1100,130 ), wx.TAB_TRAVERSAL )
		self.m_panel_data.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel_data.SetMinSize( wx.Size( 1100,130 ) )
		self.m_panel_data.SetMaxSize( wx.Size( 1100,130 ) )

		bSizer351 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_data_view = wx.Panel( self.m_panel_data, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1100,130 ), wx.TAB_TRAVERSAL )
		self.m_panel_data_view.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
		self.m_panel_data_view.Hide()
		self.m_panel_data_view.SetMinSize( wx.Size( 1100,130 ) )
		self.m_panel_data_view.SetMaxSize( wx.Size( 1100,130 ) )

		bSizer89 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer92.SetMinSize( wx.Size( 515,130 ) )
		bSizer575 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer365 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel125 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,17 ), wx.TAB_TRAVERSAL )
		self.m_panel125.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
		self.m_panel125.SetMinSize( wx.Size( 1,17 ) )
		self.m_panel125.SetMaxSize( wx.Size( 1,17 ) )

		bSizer365.Add( self.m_panel125, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText13101 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Face:", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_staticText13101.Wrap( -1 )

		self.m_staticText13101.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText13101.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_staticText13101.SetMinSize( wx.Size( -1,40 ) )
		self.m_staticText13101.SetMaxSize( wx.Size( -1,40 ) )

		bSizer365.Add( self.m_staticText13101, 0, wx.ALL, 5 )

		self.m_panel396 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel396.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel396.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel396.SetMaxSize( wx.Size( -1,2 ) )

		bSizer365.Add( self.m_panel396, 0, wx.EXPAND, 5 )

		self.m_staticText131011 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Raw", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_staticText131011.Wrap( -1 )

		self.m_staticText131011.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText131011.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_staticText131011.SetMinSize( wx.Size( -1,40 ) )
		self.m_staticText131011.SetMaxSize( wx.Size( -1,40 ) )

		bSizer365.Add( self.m_staticText131011, 0, wx.ALL, 5 )


		bSizer575.Add( bSizer365, 0, 0, 5 )

		self.m_panel124 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel124.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel124.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel124.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer575.Add( self.m_panel124, 0, wx.EXPAND, 5 )


		bSizer92.Add( bSizer575, 0, wx.EXPAND, 5 )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1310 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 1 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1310.Wrap( -1 )

		bSizer36.Add( self.m_staticText1310, 0, wx.ALL, 5 )

		self.m_textCtrl_tempface1 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempface1.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempface1.SetMaxSize( wx.Size( 60,40 ) )

		bSizer36.Add( self.m_textCtrl_tempface1, 0, wx.ALL, 5 )

		self.m_panel39 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel39.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel39.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel39.SetMaxSize( wx.Size( -1,2 ) )

		bSizer36.Add( self.m_panel39, 0, wx.EXPAND, 5 )

		self.m_textCtrl_tempfaceraw1 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfaceraw1.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempfaceraw1.SetMaxSize( wx.Size( 60,40 ) )

		bSizer36.Add( self.m_textCtrl_tempfaceraw1, 0, wx.ALL, 5 )


		bSizer57.Add( bSizer36, 0, 0, 5 )

		self.m_panel12 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel12.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel12.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel12.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer57.Add( self.m_panel12, 0, wx.EXPAND, 5 )


		bSizer92.Add( bSizer57, 0, wx.EXPAND, 5 )

		bSizer571 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer361 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText131 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 2 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		bSizer361.Add( self.m_staticText131, 0, wx.ALL, 5 )

		self.m_textCtrl_tempface2 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempface2.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempface2.SetMaxSize( wx.Size( 60,40 ) )

		bSizer361.Add( self.m_textCtrl_tempface2, 0, wx.ALL, 5 )

		self.m_panel391 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel391.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel391.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel391.SetMaxSize( wx.Size( -1,2 ) )

		bSizer361.Add( self.m_panel391, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempfaceraw2 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfaceraw2.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempfaceraw2.SetMaxSize( wx.Size( 60,40 ) )

		bSizer361.Add( self.m_textCtrl_tempfaceraw2, 0, wx.ALL, 5 )


		bSizer571.Add( bSizer361, 0, 0, 5 )

		self.m_panel121 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel121.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel121.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel121.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer571.Add( self.m_panel121, 1, wx.EXPAND, 5 )


		bSizer92.Add( bSizer571, 0, wx.EXPAND, 5 )

		bSizer572 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer362 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText132 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 3 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		bSizer362.Add( self.m_staticText132, 0, wx.ALL, 5 )

		self.m_textCtrl_tempface3 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempface3.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempface3.SetMaxSize( wx.Size( 60,40 ) )

		bSizer362.Add( self.m_textCtrl_tempface3, 0, wx.ALL, 5 )

		self.m_panel392 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel392.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel392.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel392.SetMaxSize( wx.Size( -1,2 ) )

		bSizer362.Add( self.m_panel392, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempfaceraw3 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfaceraw3.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempfaceraw3.SetMaxSize( wx.Size( 60,40 ) )

		bSizer362.Add( self.m_textCtrl_tempfaceraw3, 0, wx.ALL, 5 )


		bSizer572.Add( bSizer362, 0, 0, 5 )

		self.m_panel1211 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1211.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel1211.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel1211.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer572.Add( self.m_panel1211, 1, wx.EXPAND, 5 )


		bSizer92.Add( bSizer572, 0, wx.EXPAND, 5 )

		bSizer573 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer363 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText133 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 4 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133.Wrap( -1 )

		bSizer363.Add( self.m_staticText133, 0, wx.ALL, 5 )

		self.m_textCtrl_tempface4 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempface4.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempface4.SetMaxSize( wx.Size( 60,40 ) )

		bSizer363.Add( self.m_textCtrl_tempface4, 0, wx.ALL, 5 )

		self.m_panel393 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel393.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel393.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel393.SetMaxSize( wx.Size( -1,2 ) )

		bSizer363.Add( self.m_panel393, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempfaceraw4 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfaceraw4.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempfaceraw4.SetMaxSize( wx.Size( 60,40 ) )

		bSizer363.Add( self.m_textCtrl_tempfaceraw4, 0, wx.ALL, 5 )


		bSizer573.Add( bSizer363, 0, 0, 5 )

		self.m_panel122 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel122.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel122.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel122.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer573.Add( self.m_panel122, 1, wx.EXPAND, 5 )


		bSizer92.Add( bSizer573, 0, wx.EXPAND, 5 )

		bSizer574 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer364 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText134 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 5 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		bSizer364.Add( self.m_staticText134, 0, wx.ALL, 5 )

		self.m_textCtrl_tempface5 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempface5.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempface5.SetMaxSize( wx.Size( 60,40 ) )

		bSizer364.Add( self.m_textCtrl_tempface5, 0, wx.ALL, 5 )

		self.m_panel394 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel394.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel394.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel394.SetMaxSize( wx.Size( -1,2 ) )

		bSizer364.Add( self.m_panel394, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempfaceraw5 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfaceraw5.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempfaceraw5.SetMaxSize( wx.Size( 60,40 ) )

		bSizer364.Add( self.m_textCtrl_tempfaceraw5, 0, wx.ALL, 5 )


		bSizer574.Add( bSizer364, 0, 0, 5 )

		self.m_panel123 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel123.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel123.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel123.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer574.Add( self.m_panel123, 1, wx.EXPAND, 5 )


		bSizer92.Add( bSizer574, 0, wx.EXPAND, 5 )

		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer116 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText36 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Average :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText36.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer116.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl_tempfaceAgv = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfaceAgv.SetMinSize( wx.Size( 80,40 ) )
		self.m_textCtrl_tempfaceAgv.SetMaxSize( wx.Size( 80,40 ) )

		bSizer116.Add( self.m_textCtrl_tempfaceAgv, 0, wx.ALL, 5 )

		self.m_panel395 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel395.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel395.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel395.SetMaxSize( wx.Size( -1,2 ) )

		bSizer116.Add( self.m_panel395, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempfacerawagv = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,39 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempfacerawagv.SetMinSize( wx.Size( 80,39 ) )
		self.m_textCtrl_tempfacerawagv.SetMaxSize( wx.Size( 80,39 ) )

		bSizer116.Add( self.m_textCtrl_tempfacerawagv, 0, wx.ALL, 5 )


		bSizer94.Add( bSizer116, 0, wx.EXPAND, 5 )

		self.m_panel129 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel129.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel129.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel129.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer94.Add( self.m_panel129, 1, wx.EXPAND, 5 )


		bSizer92.Add( bSizer94, 0, wx.EXPAND, 5 )


		bSizer89.Add( bSizer92, 0, 0, 5 )

		self.m_panel74 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 8,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel74.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel74.SetMinSize( wx.Size( 8,-1 ) )
		self.m_panel74.SetMaxSize( wx.Size( 8,-1 ) )

		bSizer89.Add( self.m_panel74, 1, wx.EXPAND, 5 )

		bSizer921 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer921.SetMinSize( wx.Size( 100,130 ) )
		bSizer5751 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3651 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1251 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,17 ), wx.TAB_TRAVERSAL )
		self.m_panel1251.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
		self.m_panel1251.SetMinSize( wx.Size( 1,17 ) )
		self.m_panel1251.SetMaxSize( wx.Size( 1,17 ) )

		bSizer3651.Add( self.m_panel1251, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText131012 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Envir:", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_staticText131012.Wrap( -1 )

		self.m_staticText131012.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText131012.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_staticText131012.SetMinSize( wx.Size( -1,40 ) )
		self.m_staticText131012.SetMaxSize( wx.Size( -1,40 ) )

		bSizer3651.Add( self.m_staticText131012, 0, wx.ALL, 5 )

		self.m_panel3961 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel3961.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel3961.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel3961.SetMaxSize( wx.Size( -1,2 ) )

		bSizer3651.Add( self.m_panel3961, 0, wx.EXPAND, 5 )

		self.m_staticText1310111 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Raw:", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_staticText1310111.Wrap( -1 )

		self.m_staticText1310111.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText1310111.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_staticText1310111.SetMinSize( wx.Size( -1,40 ) )
		self.m_staticText1310111.SetMaxSize( wx.Size( -1,40 ) )

		bSizer3651.Add( self.m_staticText1310111, 0, wx.ALL, 5 )


		bSizer5751.Add( bSizer3651, 0, 0, 5 )

		self.m_panel1241 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1241.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel1241.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel1241.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer5751.Add( self.m_panel1241, 0, wx.EXPAND, 5 )


		bSizer921.Add( bSizer5751, 0, 0, 5 )

		bSizer576 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer366 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13102 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 1 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13102.Wrap( -1 )

		bSizer366.Add( self.m_staticText13102, 0, wx.ALL, 5 )

		self.m_textCtrl_tempenvir1 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvir1.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvir1.SetMaxSize( wx.Size( 60,40 ) )

		bSizer366.Add( self.m_textCtrl_tempenvir1, 0, wx.ALL, 5 )

		self.m_panel397 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel397.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel397.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel397.SetMaxSize( wx.Size( -1,2 ) )

		bSizer366.Add( self.m_panel397, 0, wx.EXPAND, 5 )

		self.m_textCtrl_tempenvirraw1 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvirraw1.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvirraw1.SetMaxSize( wx.Size( 60,40 ) )

		bSizer366.Add( self.m_textCtrl_tempenvirraw1, 0, wx.ALL, 5 )


		bSizer576.Add( bSizer366, 0, 0, 5 )

		self.m_panel126 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel126.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel126.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel126.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer576.Add( self.m_panel126, 0, wx.EXPAND, 5 )


		bSizer921.Add( bSizer576, 0, wx.EXPAND, 5 )

		bSizer5711 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3611 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1311 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 2 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1311.Wrap( -1 )

		bSizer3611.Add( self.m_staticText1311, 0, wx.ALL, 5 )

		self.m_textCtrl_tempenvir2 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvir2.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvir2.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3611.Add( self.m_textCtrl_tempenvir2, 0, wx.ALL, 5 )

		self.m_panel3911 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel3911.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel3911.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel3911.SetMaxSize( wx.Size( -1,2 ) )

		bSizer3611.Add( self.m_panel3911, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempenvirraw2 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvirraw2.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvirraw2.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3611.Add( self.m_textCtrl_tempenvirraw2, 0, wx.ALL, 5 )


		bSizer5711.Add( bSizer3611, 0, 0, 5 )

		self.m_panel1212 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1212.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel1212.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel1212.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer5711.Add( self.m_panel1212, 1, wx.EXPAND, 5 )


		bSizer921.Add( bSizer5711, 0, wx.EXPAND, 5 )

		bSizer5721 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3621 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1321 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 3 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1321.Wrap( -1 )

		bSizer3621.Add( self.m_staticText1321, 0, wx.ALL, 5 )

		self.m_textCtrl_tempenvir3 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvir3.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvir3.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3621.Add( self.m_textCtrl_tempenvir3, 0, wx.ALL, 5 )

		self.m_panel3921 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel3921.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel3921.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel3921.SetMaxSize( wx.Size( -1,2 ) )

		bSizer3621.Add( self.m_panel3921, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempenvirraw3 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvirraw3.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvirraw3.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3621.Add( self.m_textCtrl_tempenvirraw3, 0, wx.ALL, 5 )


		bSizer5721.Add( bSizer3621, 0, 0, 5 )

		self.m_panel12111 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel12111.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel12111.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel12111.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer5721.Add( self.m_panel12111, 1, wx.EXPAND, 5 )


		bSizer921.Add( bSizer5721, 0, wx.EXPAND, 5 )

		bSizer5731 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3631 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1331 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 4 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1331.Wrap( -1 )

		bSizer3631.Add( self.m_staticText1331, 0, wx.ALL, 5 )

		self.m_textCtrl_tempenvir4 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvir4.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvir4.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3631.Add( self.m_textCtrl_tempenvir4, 0, wx.ALL, 5 )

		self.m_panel3931 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel3931.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel3931.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel3931.SetMaxSize( wx.Size( -1,2 ) )

		bSizer3631.Add( self.m_panel3931, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempenvirraw4 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvirraw4.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvirraw4.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3631.Add( self.m_textCtrl_tempenvirraw4, 0, wx.ALL, 5 )


		bSizer5731.Add( bSizer3631, 0, 0, 5 )

		self.m_panel1221 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1221.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel1221.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel1221.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer5731.Add( self.m_panel1221, 1, wx.EXPAND, 5 )


		bSizer921.Add( bSizer5731, 0, wx.EXPAND, 5 )

		bSizer5741 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3641 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1341 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Temp 5 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1341.Wrap( -1 )

		bSizer3641.Add( self.m_staticText1341, 0, wx.ALL, 5 )

		self.m_textCtrl_tempenvir5 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvir5.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvir5.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3641.Add( self.m_textCtrl_tempenvir5, 0, wx.ALL, 5 )

		self.m_panel3941 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel3941.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel3941.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel3941.SetMaxSize( wx.Size( -1,2 ) )

		bSizer3641.Add( self.m_panel3941, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempenvirraw5 = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvirraw5.SetMinSize( wx.Size( 60,40 ) )
		self.m_textCtrl_tempenvirraw5.SetMaxSize( wx.Size( 60,40 ) )

		bSizer3641.Add( self.m_textCtrl_tempenvirraw5, 0, wx.ALL, 5 )


		bSizer5741.Add( bSizer3641, 0, 0, 5 )

		self.m_panel1231 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1231.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel1231.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel1231.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer5741.Add( self.m_panel1231, 1, wx.EXPAND, 5 )


		bSizer921.Add( bSizer5741, 0, wx.EXPAND, 5 )

		bSizer941 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer1161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText361 = wx.StaticText( self.m_panel_data_view, wx.ID_ANY, u"Average :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )

		self.m_staticText361.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText361.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer1161.Add( self.m_staticText361, 0, wx.ALL, 5 )

		self.m_textCtrl_tempenviragv = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,40 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenviragv.SetMinSize( wx.Size( 80,40 ) )
		self.m_textCtrl_tempenviragv.SetMaxSize( wx.Size( 80,40 ) )

		bSizer1161.Add( self.m_textCtrl_tempenviragv, 0, wx.ALL, 5 )

		self.m_panel3951 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.TAB_TRAVERSAL )
		self.m_panel3951.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_panel3951.SetMinSize( wx.Size( -1,2 ) )
		self.m_panel3951.SetMaxSize( wx.Size( -1,2 ) )

		bSizer1161.Add( self.m_panel3951, 1, wx.EXPAND, 5 )

		self.m_textCtrl_tempenvirrawagv = wx.TextCtrl( self.m_panel_data_view, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,39 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_tempenvirrawagv.SetMinSize( wx.Size( 80,39 ) )
		self.m_textCtrl_tempenvirrawagv.SetMaxSize( wx.Size( 80,39 ) )

		bSizer1161.Add( self.m_textCtrl_tempenvirrawagv, 0, wx.ALL, 5 )


		bSizer941.Add( bSizer1161, 0, 0, 5 )

		self.m_panel1291 = wx.Panel( self.m_panel_data_view, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1291.SetBackgroundColour( wx.Colour( 116, 130, 188 ) )
		self.m_panel1291.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel1291.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer941.Add( self.m_panel1291, 1, wx.EXPAND, 5 )


		bSizer921.Add( bSizer941, 0, 0, 5 )


		bSizer89.Add( bSizer921, 0, 0, 5 )

		self.m_button_cl = wx.Button( self.m_panel_data_view, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 42,42 ), 0 )
		self.m_button_cl.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button_cl.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_button_cl.SetMinSize( wx.Size( 42,42 ) )
		self.m_button_cl.SetMaxSize( wx.Size( 42,42 ) )

		bSizer89.Add( self.m_button_cl, 0, 0, 5 )


		self.m_panel_data_view.SetSizer( bSizer89 )
		self.m_panel_data_view.Layout()
		bSizer351.Add( self.m_panel_data_view, 0, 0, 5 )


		self.m_panel_data.SetSizer( bSizer351 )
		self.m_panel_data.Layout()
		bSizer341.Add( self.m_panel_data, 0, 0, 5 )


		bSizer32.Add( bSizer341, 0, 0, 5 )


		bSizer1.Add( bSizer32, 0, 0, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_statusBar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.frame_mainOnClose )
		self.m_panel_video.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_videoOnEraseBackground )
		self.m_panel_video.Bind( wx.EVT_PAINT, self.m_panel_videoOnPaint )
		self.m_panel_video_thermography.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_video_thermographyOnEraseBackground )
		self.m_panel_video_thermography.Bind( wx.EVT_PAINT, self.m_panel_video_thermographyOnPaint )
		self.m_button_exit.Bind( wx.EVT_BUTTON, self.m_button_exitOnButtonClick )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.m_button_settingOnButtonClick )
		self.m_button_data.Bind( wx.EVT_BUTTON, self.m_button_dataOnButtonClick )
		self.m_panel_data.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_dataOnEraseBackground )
		self.m_panel_data.Bind( wx.EVT_PAINT, self.m_panel_dataOnPaint )
		self.m_button_cl.Bind( wx.EVT_BUTTON, self.m_button_clOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def frame_mainOnClose( self, event ):
		event.Skip()

	def m_panel_videoOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_videoOnPaint( self, event ):
		event.Skip()

	def m_panel_video_thermographyOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_video_thermographyOnPaint( self, event ):
		event.Skip()

	def m_button_exitOnButtonClick( self, event ):
		event.Skip()

	def m_button_settingOnButtonClick( self, event ):
		event.Skip()

	def m_button_dataOnButtonClick( self, event ):
		event.Skip()

	def m_panel_dataOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_dataOnPaint( self, event ):
		event.Skip()

	def m_button_clOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_setting
###########################################################################

class MyDialog_setting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SETTING", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_panel6.SetMinSize( wx.Size( -1,50 ) )
		self.m_panel6.SetMaxSize( wx.Size( -1,50 ) )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_save = wx.Button( self.m_panel6, wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_save.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_save.SetMaxSize( wx.Size( 70,40 ) )

		bSizer32.Add( self.m_button_save, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 15,50 ), 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetMinSize( wx.Size( 15,50 ) )
		self.m_staticText14.SetMaxSize( wx.Size( 15,50 ) )

		bSizer32.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_button_reset = wx.Button( self.m_panel6, wx.ID_ANY, u"RESET", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_reset.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_reset.SetMaxSize( wx.Size( 70,40 ) )

		bSizer32.Add( self.m_button_reset, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 15,50 ), 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetMinSize( wx.Size( 15,50 ) )
		self.m_staticText141.SetMaxSize( wx.Size( 15,50 ) )

		bSizer32.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_button_close = wx.Button( self.m_panel6, wx.ID_ANY, u"CLOSE", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_close.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_close.SetMaxSize( wx.Size( 70,40 ) )

		bSizer32.Add( self.m_button_close, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer32 )
		self.m_panel6.Layout()
		bSizer24.Add( self.m_panel6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel_setting = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_setting.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer88 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText111 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Perform FFC :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		bSizer88.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl_ffc = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer88.Add( self.m_textCtrl_ffc, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer88, 1, wx.EXPAND, 5 )

		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_ffcManual = wx.Button( self.m_panel_setting, wx.ID_ANY, u"Normal", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_ffcManual.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_ffcManual.SetMaxSize( wx.Size( 70,40 ) )

		bSizer321.Add( self.m_button_ffcManual, 0, wx.ALL, 5 )

		self.m_button_ffcAuto = wx.Button( self.m_panel_setting, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_ffcAuto.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_ffcAuto.SetMaxSize( wx.Size( 70,40 ) )

		bSizer321.Add( self.m_button_ffcAuto, 0, wx.ALL, 5 )

		self.m_button_ffcTest = wx.Button( self.m_panel_setting, wx.ID_ANY, u"FFC Calib", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_ffcTest.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_ffcTest.SetMaxSize( wx.Size( 70,40 ) )

		bSizer321.Add( self.m_button_ffcTest, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer321, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer25.Add( bSizer31, 0, wx.EXPAND, 5 )

		self.m_panel612 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel612.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel612.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel612.SetMaxSize( wx.Size( -1,1 ) )

		bSizer25.Add( self.m_panel612, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Fever Temperature:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer20.Add( self.m_staticText7, 0, wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_fever = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"37.5", wx.DefaultPosition, wx.Size( -1,37 ), 0 )
		self.m_textCtrl_fever.SetMinSize( wx.Size( -1,37 ) )
		self.m_textCtrl_fever.SetMaxSize( wx.Size( -1,37 ) )

		bSizer27.Add( self.m_textCtrl_fever, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_fever_down = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 70,37 ), 0 )
		self.m_button_fever_down.SetMinSize( wx.Size( 70,37 ) )
		self.m_button_fever_down.SetMaxSize( wx.Size( 70,37 ) )

		bSizer27.Add( self.m_button_fever_down, 0, wx.ALL, 5 )

		self.m_button_fever_up = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 70,37 ), 0 )
		self.m_button_fever_up.SetMinSize( wx.Size( 70,37 ) )
		self.m_button_fever_up.SetMaxSize( wx.Size( 70,37 ) )

		bSizer27.Add( self.m_button_fever_up, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer27, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer20, 0, wx.EXPAND, 5 )

		self.m_panel61 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel61.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel61.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel61.SetMaxSize( wx.Size( -1,1 ) )

		bSizer25.Add( self.m_panel61, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Calib Temp Calcualator :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer21.Add( self.m_staticText6, 0, wx.ALL, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_ktoc = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( -1,37 ), 0 )
		self.m_textCtrl_ktoc.SetMinSize( wx.Size( -1,37 ) )
		self.m_textCtrl_ktoc.SetMaxSize( wx.Size( -1,37 ) )

		bSizer26.Add( self.m_textCtrl_ktoc, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_tempktoc_down = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 70,37 ), 0 )
		self.m_button_tempktoc_down.SetMinSize( wx.Size( 70,37 ) )
		self.m_button_tempktoc_down.SetMaxSize( wx.Size( 70,37 ) )

		bSizer26.Add( self.m_button_tempktoc_down, 0, wx.ALL, 5 )

		self.m_button_tempktoc_up = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 70,37 ), 0 )
		self.m_button_tempktoc_up.SetMinSize( wx.Size( 70,37 ) )
		self.m_button_tempktoc_up.SetMaxSize( wx.Size( 70,37 ) )

		bSizer26.Add( self.m_button_tempktoc_up, 0, wx.ALL, 5 )


		bSizer21.Add( bSizer26, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer21, 0, wx.EXPAND, 5 )

		self.m_panel611 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel611.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel611.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel611.SetMaxSize( wx.Size( -1,1 ) )

		bSizer25.Add( self.m_panel611, 1, wx.EXPAND, 5 )

		bSizer2111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText611 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Calib Value :    Sensor Value :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611.Wrap( -1 )

		bSizer2111.Add( self.m_staticText611, 0, wx.ALL, 5 )

		bSizer2621 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_envirLepton = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 90,30 ), 0 )
		self.m_textCtrl_envirLepton.SetMinSize( wx.Size( 90,30 ) )
		self.m_textCtrl_envirLepton.SetMaxSize( wx.Size( 90,30 ) )

		bSizer2621.Add( self.m_textCtrl_envirLepton, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_show_sensor = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 90,30 ), 0 )
		self.m_textCtrl_show_sensor.SetMinSize( wx.Size( 90,30 ) )
		self.m_textCtrl_show_sensor.SetMaxSize( wx.Size( 90,30 ) )

		bSizer2621.Add( self.m_textCtrl_show_sensor, 0, wx.ALL, 5 )


		bSizer2621.Add( ( 5, 0), 0, 0, 5 )

		self.m_button_temp_envirLepton = wx.Button( self.m_panel_setting, wx.ID_ANY, u"Get Value", wx.DefaultPosition, wx.Size( 70,30 ), 0 )
		self.m_button_temp_envirLepton.SetMinSize( wx.Size( 70,30 ) )
		self.m_button_temp_envirLepton.SetMaxSize( wx.Size( 70,30 ) )

		bSizer2621.Add( self.m_button_temp_envirLepton, 0, wx.ALL, 5 )


		bSizer2111.Add( bSizer2621, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer2111, 0, wx.EXPAND, 5 )

		self.m_panel6121 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel6121.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel6121.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel6121.SetMaxSize( wx.Size( -1,1 ) )

		bSizer25.Add( self.m_panel6121, 1, wx.EXPAND, 5 )

		bSizer21112 = wx.BoxSizer( wx.VERTICAL )

		bSizer89 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer84 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6112 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Fist Envir Ave -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6112.Wrap( -1 )

		bSizer84.Add( self.m_staticText6112, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl_FistEnvirAve = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_FistEnvirAve.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_FistEnvirAve.SetMaxSize( wx.Size( 50,30 ) )

		bSizer84.Add( self.m_textCtrl_FistEnvirAve, 0, wx.ALL, 5 )


		bSizer89.Add( bSizer84, 0, 0, 5 )

		bSizer85 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61122 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Envir Ave  =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61122.Wrap( -1 )

		bSizer85.Add( self.m_staticText61122, 0, wx.ALL, 5 )

		self.m_textCtrl_EnvirAve = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_EnvirAve.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_EnvirAve.SetMaxSize( wx.Size( 50,30 ) )

		bSizer85.Add( self.m_textCtrl_EnvirAve, 0, wx.ALL, 5 )


		bSizer89.Add( bSizer85, 1, wx.EXPAND, 5 )

		bSizer86 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText611221 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"( A )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611221.Wrap( -1 )

		bSizer86.Add( self.m_staticText611221, 0, wx.ALL, 5 )

		self.m_textCtrl_A = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_A.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_A.SetMaxSize( wx.Size( 50,30 ) )

		bSizer86.Add( self.m_textCtrl_A, 0, wx.ALL, 5 )


		bSizer89.Add( bSizer86, 1, wx.EXPAND, 5 )


		bSizer21112.Add( bSizer89, 0, wx.EXPAND, 5 )

		self.m_panel61211 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel61211.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel61211.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel61211.SetMaxSize( wx.Size( -1,1 ) )

		bSizer21112.Add( self.m_panel61211, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer26212 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_levelLow = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"°C ", wx.DefaultPosition, wx.Size( 73,37 ), wx.TE_READONLY )
		self.m_textCtrl_levelLow.SetMinSize( wx.Size( 73,37 ) )
		self.m_textCtrl_levelLow.SetMaxSize( wx.Size( 73,37 ) )

		bSizer26212.Add( self.m_textCtrl_levelLow, 0, wx.ALL, 5 )

		self.m_textCtrl_facechange = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_textCtrl_facechange.SetMinSize( wx.Size( 50,37 ) )
		self.m_textCtrl_facechange.SetMaxSize( wx.Size( 50,37 ) )

		bSizer26212.Add( self.m_textCtrl_facechange, 0, wx.ALL, 5 )


		bSizer26212.Add( ( 5, 0), 0, 0, 5 )

		self.m_button_temp_envirFaceChangeDown = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_button_temp_envirFaceChangeDown.SetMinSize( wx.Size( 50,37 ) )
		self.m_button_temp_envirFaceChangeDown.SetMaxSize( wx.Size( 50,37 ) )

		bSizer26212.Add( self.m_button_temp_envirFaceChangeDown, 0, wx.ALL, 5 )

		self.m_button_temp_envirFaceChangeUp = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_button_temp_envirFaceChangeUp.SetMinSize( wx.Size( 50,37 ) )
		self.m_button_temp_envirFaceChangeUp.SetMaxSize( wx.Size( 50,37 ) )

		bSizer26212.Add( self.m_button_temp_envirFaceChangeUp, 0, wx.ALL, 5 )


		bSizer21112.Add( bSizer26212, 0, wx.EXPAND, 5 )

		bSizer262122 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_levelMid = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 73,37 ), wx.TE_READONLY )
		self.m_textCtrl_levelMid.SetMinSize( wx.Size( 73,37 ) )
		self.m_textCtrl_levelMid.SetMaxSize( wx.Size( 73,37 ) )

		bSizer262122.Add( self.m_textCtrl_levelMid, 0, wx.ALL, 5 )

		self.m_textCtrl_facechange1 = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_textCtrl_facechange1.SetMinSize( wx.Size( 50,37 ) )
		self.m_textCtrl_facechange1.SetMaxSize( wx.Size( 50,37 ) )

		bSizer262122.Add( self.m_textCtrl_facechange1, 0, wx.ALL, 5 )


		bSizer262122.Add( ( 5, 0), 0, 0, 5 )

		self.m_button_temp_envirFaceChangeDown1 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_button_temp_envirFaceChangeDown1.SetMinSize( wx.Size( 50,37 ) )
		self.m_button_temp_envirFaceChangeDown1.SetMaxSize( wx.Size( 50,37 ) )

		bSizer262122.Add( self.m_button_temp_envirFaceChangeDown1, 0, wx.ALL, 5 )

		self.m_button_temp_envirFaceChangeUp1 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_button_temp_envirFaceChangeUp1.SetMinSize( wx.Size( 50,37 ) )
		self.m_button_temp_envirFaceChangeUp1.SetMaxSize( wx.Size( 50,37 ) )

		bSizer262122.Add( self.m_button_temp_envirFaceChangeUp1, 0, wx.ALL, 5 )


		bSizer21112.Add( bSizer262122, 0, wx.EXPAND, 5 )

		bSizer2621221 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_levelHigh = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 73,37 ), wx.TE_READONLY )
		self.m_textCtrl_levelHigh.SetMinSize( wx.Size( 73,37 ) )
		self.m_textCtrl_levelHigh.SetMaxSize( wx.Size( 73,37 ) )

		bSizer2621221.Add( self.m_textCtrl_levelHigh, 0, wx.ALL, 5 )

		self.m_textCtrl_facechange2 = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_textCtrl_facechange2.SetMinSize( wx.Size( 50,37 ) )
		self.m_textCtrl_facechange2.SetMaxSize( wx.Size( 50,37 ) )

		bSizer2621221.Add( self.m_textCtrl_facechange2, 0, wx.ALL, 5 )


		bSizer2621221.Add( ( 5, 0), 0, 0, 5 )

		self.m_button_temp_envirFaceChangeDown2 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_button_temp_envirFaceChangeDown2.SetMinSize( wx.Size( 50,37 ) )
		self.m_button_temp_envirFaceChangeDown2.SetMaxSize( wx.Size( 50,37 ) )

		bSizer2621221.Add( self.m_button_temp_envirFaceChangeDown2, 0, wx.ALL, 5 )

		self.m_button_temp_envirFaceChangeUp2 = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,37 ), 0 )
		self.m_button_temp_envirFaceChangeUp2.SetMinSize( wx.Size( 50,37 ) )
		self.m_button_temp_envirFaceChangeUp2.SetMaxSize( wx.Size( 50,37 ) )

		bSizer2621221.Add( self.m_button_temp_envirFaceChangeUp2, 0, wx.ALL, 5 )


		bSizer21112.Add( bSizer2621221, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer21112, 0, wx.EXPAND, 5 )

		self.m_panel6122 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel6122.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel6122.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel6122.SetMaxSize( wx.Size( -1,1 ) )

		bSizer25.Add( self.m_panel6122, 1, wx.EXPAND, 5 )

		bSizer891 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer841 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61123 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Face_c =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61123.Wrap( -1 )

		bSizer841.Add( self.m_staticText61123, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl_Face_c = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_Face_c.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_Face_c.SetMaxSize( wx.Size( 50,30 ) )

		bSizer841.Add( self.m_textCtrl_Face_c, 0, wx.ALL, 5 )


		bSizer891.Add( bSizer841, 0, 0, 5 )

		bSizer851 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText611222 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"FaceRaw+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611222.Wrap( -1 )

		bSizer851.Add( self.m_staticText611222, 0, wx.ALL, 5 )

		self.m_textCtrl_FaceRaw1 = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_FaceRaw1.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_FaceRaw1.SetMaxSize( wx.Size( 50,30 ) )

		bSizer851.Add( self.m_textCtrl_FaceRaw1, 0, wx.ALL, 5 )


		bSizer891.Add( bSizer851, 0, 0, 5 )

		bSizer861 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6112211 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"CalibTemp+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6112211.Wrap( -1 )

		bSizer861.Add( self.m_staticText6112211, 0, wx.ALL, 5 )

		self.m_textCtrl_CalibTemp = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_CalibTemp.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_CalibTemp.SetMaxSize( wx.Size( 50,30 ) )

		bSizer861.Add( self.m_textCtrl_CalibTemp, 0, wx.ALL, 5 )


		bSizer891.Add( bSizer861, 0, wx.EXPAND, 5 )

		bSizer8611 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61122111 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"( EnvirAve-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61122111.Wrap( -1 )

		bSizer8611.Add( self.m_staticText61122111, 0, wx.ALL, 5 )

		self.m_textCtrl_EnvirAve1 = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_EnvirAve1.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_EnvirAve1.SetMaxSize( wx.Size( 50,30 ) )

		bSizer8611.Add( self.m_textCtrl_EnvirAve1, 0, wx.ALL, 5 )


		bSizer891.Add( bSizer8611, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer891, 0, 0, 5 )

		bSizer8911 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer8411 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText611231 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611231.Wrap( -1 )

		bSizer8411.Add( self.m_staticText611231, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer8911.Add( bSizer8411, 0, 0, 5 )

		bSizer8511 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6112221 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6112221.Wrap( -1 )

		bSizer8511.Add( self.m_staticText6112221, 0, wx.ALL, 5 )


		bSizer8911.Add( bSizer8511, 0, wx.EXPAND, 5 )

		bSizer8612 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61122112 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"EnvirRaw) +", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61122112.Wrap( -1 )

		bSizer8612.Add( self.m_staticText61122112, 0, wx.ALL, 5 )

		self.m_textCtrl_EnvirRaw = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_EnvirRaw.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_EnvirRaw.SetMaxSize( wx.Size( 50,30 ) )

		bSizer8612.Add( self.m_textCtrl_EnvirRaw, 0, wx.ALL, 5 )


		bSizer8911.Add( bSizer8612, 0, wx.EXPAND, 5 )

		bSizer86111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText611221111 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"(    A   )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611221111.Wrap( -1 )

		bSizer86111.Add( self.m_staticText611221111, 0, wx.ALL, 5 )

		self.m_textCtrl_A1 = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_textCtrl_A1.SetMinSize( wx.Size( 50,30 ) )
		self.m_textCtrl_A1.SetMaxSize( wx.Size( 50,30 ) )

		bSizer86111.Add( self.m_textCtrl_A1, 0, wx.ALL, 5 )


		bSizer8911.Add( bSizer86111, 0, wx.EXPAND, 5 )

		bSizer861111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6112211111 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"* Face (change)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6112211111.Wrap( -1 )

		bSizer861111.Add( self.m_staticText6112211111, 0, wx.ALL, 5 )

		self.m_textCtrl_FaceChange = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 70,30 ), 0 )
		self.m_textCtrl_FaceChange.SetMinSize( wx.Size( 70,30 ) )
		self.m_textCtrl_FaceChange.SetMaxSize( wx.Size( 70,30 ) )

		bSizer861111.Add( self.m_textCtrl_FaceChange, 0, wx.ALL, 5 )


		bSizer8911.Add( bSizer861111, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer8911, 0, 0, 5 )

		self.m_panel6123 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.TAB_TRAVERSAL )
		self.m_panel6123.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel6123.SetMinSize( wx.Size( -1,1 ) )
		self.m_panel6123.SetMaxSize( wx.Size( -1,1 ) )

		bSizer25.Add( self.m_panel6123, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer21111 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer1091 = wx.BoxSizer( wx.VERTICAL )

		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText61111 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Senser:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61111.Wrap( -1 )

		bSizer112.Add( self.m_staticText61111, 0, wx.ALL, 5 )

		self.m_textCtrl_onSenser = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.Size( 60,22 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_onSenser.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_textCtrl_onSenser.SetMinSize( wx.Size( 60,22 ) )
		self.m_textCtrl_onSenser.SetMaxSize( wx.Size( 60,22 ) )

		bSizer112.Add( self.m_textCtrl_onSenser, 1, 0, 5 )


		bSizer1091.Add( bSizer112, 1, 0, 5 )

		bSizer262111 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_onSensor = wx.Button( self.m_panel_setting, wx.ID_ANY, u"ON_OFF", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_onSensor.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_onSensor.SetMaxSize( wx.Size( 70,40 ) )

		bSizer262111.Add( self.m_button_onSensor, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1091.Add( bSizer262111, 0, wx.EXPAND, 5 )


		bSizer21111.Add( bSizer1091, 0, wx.EXPAND, 5 )


		bSizer21111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel511 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel511.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel511.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel511.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer21111.Add( self.m_panel511, 0, wx.EXPAND, 5 )


		bSizer21111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer109 = wx.BoxSizer( wx.VERTICAL )

		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6111 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"FIle CSV:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6111.Wrap( -1 )

		bSizer113.Add( self.m_staticText6111, 0, wx.ALL, 5 )

		self.m_textCtrl_log = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"CREATE FILE", wx.DefaultPosition, wx.Size( 100,22 ), wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl_log.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_textCtrl_log.SetMinSize( wx.Size( 100,22 ) )
		self.m_textCtrl_log.SetMaxSize( wx.Size( 100,22 ) )

		bSizer113.Add( self.m_textCtrl_log, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer109.Add( bSizer113, 1, wx.EXPAND, 5 )

		bSizer26211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_dirPicker_csv = wx.DirPickerCtrl( self.m_panel_setting, wx.ID_ANY, u"fileDataCSV", u"Select a folder", wx.DefaultPosition, wx.Size( 70,40 ), wx.DIRP_CHANGE_DIR )
		self.m_dirPicker_csv.SetMinSize( wx.Size( 70,40 ) )
		self.m_dirPicker_csv.SetMaxSize( wx.Size( 70,40 ) )

		bSizer26211.Add( self.m_dirPicker_csv, 0, wx.ALL, 5 )

		self.m_button_logcsv = wx.Button( self.m_panel_setting, wx.ID_ANY, u"LOG", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_logcsv.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_logcsv.SetMaxSize( wx.Size( 70,40 ) )

		bSizer26211.Add( self.m_button_logcsv, 0, wx.ALL, 5 )


		bSizer109.Add( bSizer26211, 0, wx.EXPAND, 5 )


		bSizer21111.Add( bSizer109, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer21111, 0, wx.EXPAND, 5 )

		bSizer211121 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61121 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Temp G Ave(E6 ... E10) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61121.Wrap( -1 )

		self.m_staticText61121.Hide()

		bSizer211121.Add( self.m_staticText61121, 0, wx.ALL, 5 )

		bSizer262121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_envirG = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 160,40 ), 0 )
		self.m_textCtrl_envirG.Hide()
		self.m_textCtrl_envirG.SetMinSize( wx.Size( 160,40 ) )
		self.m_textCtrl_envirG.SetMaxSize( wx.Size( 160,40 ) )

		bSizer262121.Add( self.m_textCtrl_envirG, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer262121.Add( ( 27, 0), 0, 0, 5 )

		self.m_button_temp_envirG = wx.Button( self.m_panel_setting, wx.ID_ANY, u"Get Value", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_temp_envirG.Hide()
		self.m_button_temp_envirG.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_temp_envirG.SetMaxSize( wx.Size( 70,40 ) )

		bSizer262121.Add( self.m_button_temp_envirG, 0, wx.ALL, 5 )


		bSizer211121.Add( bSizer262121, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer211121, 0, wx.EXPAND, 5 )

		self.m_panel613 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel613.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText39 = wx.StaticText( self.m_panel613, wx.ID_ANY, u"Set Detect Face:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer101.Add( self.m_staticText39, 0, wx.ALL, 5 )


		self.m_panel613.SetSizer( bSizer101 )
		self.m_panel613.Layout()
		bSizer101.Fit( self.m_panel613 )
		bSizer25.Add( self.m_panel613, 0, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText71 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Calib camera :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		bSizer22.Add( self.m_staticText71, 0, wx.ALL, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_moveup = wx.Button( self.m_panel_setting, wx.ID_ANY, u"▲", wx.DefaultPosition, wx.Size( 40,50 ), 0 )
		self.m_button_moveup.SetMinSize( wx.Size( 40,50 ) )
		self.m_button_moveup.SetMaxSize( wx.Size( 40,50 ) )

		bSizer23.Add( self.m_button_moveup, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( bSizer23, 0, wx.EXPAND, 5 )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_moveleft = wx.Button( self.m_panel_setting, wx.ID_ANY, u"◄", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_moveleft.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_moveleft.SetMaxSize( wx.Size( 70,40 ) )

		bSizer241.Add( self.m_button_moveleft, 0, wx.ALL, 5 )


		bSizer241.Add( ( 2, 0), 1, wx.EXPAND, 5 )

		self.m_button_moveright = wx.Button( self.m_panel_setting, wx.ID_ANY, u"►", wx.DefaultPosition, wx.Size( 70,40 ), 0 )
		self.m_button_moveright.SetMinSize( wx.Size( 70,40 ) )
		self.m_button_moveright.SetMaxSize( wx.Size( 70,40 ) )

		bSizer241.Add( self.m_button_moveright, 0, wx.ALL, 5 )


		bSizer22.Add( bSizer241, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer251 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_movebottom = wx.Button( self.m_panel_setting, wx.ID_ANY, u"▼", wx.DefaultPosition, wx.Size( 40,50 ), 0 )
		self.m_button_movebottom.SetMinSize( wx.Size( 40,50 ) )
		self.m_button_movebottom.SetMaxSize( wx.Size( 40,50 ) )

		bSizer251.Add( self.m_button_movebottom, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( bSizer251, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer34.Add( bSizer22, 0, wx.EXPAND, 5 )

		self.m_panel5 = wx.Panel( self.m_panel_setting, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )
		self.m_panel5.SetMinSize( wx.Size( 1,-1 ) )
		self.m_panel5.SetMaxSize( wx.Size( 1,-1 ) )

		bSizer34.Add( self.m_panel5, 0, wx.EXPAND, 5 )

		bSizer261 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel_setting, wx.ID_ANY, u"Change size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer261.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer271 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_zoom = wx.Button( self.m_panel_setting, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,50 ), 0 )
		self.m_button_zoom.SetMinSize( wx.Size( 40,50 ) )
		self.m_button_zoom.SetMaxSize( wx.Size( 40,50 ) )

		bSizer271.Add( self.m_button_zoom, 0, wx.ALL, 5 )


		bSizer271.Add( ( 20, 30), 1, wx.EXPAND, 5 )

		self.m_button_zoomout = wx.Button( self.m_panel_setting, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 40,50 ), 0 )
		self.m_button_zoomout.SetMinSize( wx.Size( 40,50 ) )
		self.m_button_zoomout.SetMaxSize( wx.Size( 40,50 ) )

		bSizer271.Add( self.m_button_zoomout, 0, wx.ALL, 5 )


		bSizer261.Add( bSizer271, 0, wx.ALIGN_RIGHT, 5 )


		bSizer34.Add( bSizer261, 0, 0, 5 )


		bSizer25.Add( bSizer34, 0, 0, 5 )

		self.m_textCtrl_runSetting = wx.TextCtrl( self.m_panel_setting, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 1,1 ), 0 )
		self.m_textCtrl_runSetting.SetMinSize( wx.Size( 1,1 ) )
		self.m_textCtrl_runSetting.SetMaxSize( wx.Size( 1,1 ) )

		bSizer25.Add( self.m_textCtrl_runSetting, 0, wx.ALL, 5 )


		self.m_panel_setting.SetSizer( bSizer25 )
		self.m_panel_setting.Layout()
		bSizer25.Fit( self.m_panel_setting )
		bSizer24.Add( self.m_panel_setting, 0, wx.EXPAND, 5 )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,10 ), wx.TAB_TRAVERSAL )
		self.m_panel16.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		self.m_panel16.SetMinSize( wx.Size( -1,10 ) )
		self.m_panel16.SetMaxSize( wx.Size( -1,10 ) )

		bSizer24.Add( self.m_panel16, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer24 )
		self.Layout()
		bSizer24.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyDialog_settingOnClose )
		self.m_button_save.Bind( wx.EVT_BUTTON, self.m_button_saveOnButtonClick )
		self.m_button_reset.Bind( wx.EVT_BUTTON, self.m_button_resetOnButtonClick )
		self.m_button_close.Bind( wx.EVT_BUTTON, self.m_button_closeOnButtonClick )
		self.m_panel_setting.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_settingOnEraseBackground )
		self.m_panel_setting.Bind( wx.EVT_PAINT, self.m_panel_settingOnPaint )
		self.m_button_ffcManual.Bind( wx.EVT_BUTTON, self.m_button_ffcManualOnButtonClick )
		self.m_button_ffcAuto.Bind( wx.EVT_BUTTON, self.m_button_ffcAutoOnButtonClick )
		self.m_button_ffcTest.Bind( wx.EVT_BUTTON, self.m_button_ffcTestOnButtonClick )
		self.m_button_fever_down.Bind( wx.EVT_BUTTON, self.m_button_fever_downOnButtonClick )
		self.m_button_fever_up.Bind( wx.EVT_BUTTON, self.m_button_fever_upOnButtonClick )
		self.m_button_tempktoc_down.Bind( wx.EVT_BUTTON, self.m_button_tempktoc_downOnButtonClick )
		self.m_button_tempktoc_up.Bind( wx.EVT_BUTTON, self.m_button_tempktoc_upOnButtonClick )
		self.m_button_temp_envirLepton.Bind( wx.EVT_BUTTON, self.m_button_temp_envirLeptonOnButtonClick )
		self.m_textCtrl_levelLow.Bind( wx.EVT_CHAR_HOOK, self.m_textCtrl_facechangeOnCharHook )
		self.m_textCtrl_levelLow.Bind( wx.EVT_LEFT_DCLICK, self.m_textCtrl_facechangeOnLeftDClick )
		self.m_textCtrl_facechange.Bind( wx.EVT_CHAR_HOOK, self.m_textCtrl_facechangeOnCharHook )
		self.m_textCtrl_facechange.Bind( wx.EVT_LEFT_DCLICK, self.m_textCtrl_facechangeOnLeftDClick )
		self.m_button_temp_envirFaceChangeDown.Bind( wx.EVT_BUTTON, self.m_button_temp_envirFaceChangeDownOnButtonClick )
		self.m_button_temp_envirFaceChangeUp.Bind( wx.EVT_BUTTON, self.m_button_temp_envirFaceChangeUpOnButtonClick )
		self.m_textCtrl_levelMid.Bind( wx.EVT_CHAR_HOOK, self.m_textCtrl_facechangeOnCharHook )
		self.m_textCtrl_levelMid.Bind( wx.EVT_LEFT_DCLICK, self.m_textCtrl_facechangeOnLeftDClick )
		self.m_textCtrl_facechange1.Bind( wx.EVT_CHAR_HOOK, self.m_textCtrl_facechange1OnCharHook )
		self.m_textCtrl_facechange1.Bind( wx.EVT_LEFT_DCLICK, self.m_textCtrl_facechange1OnLeftDClick )
		self.m_button_temp_envirFaceChangeDown1.Bind( wx.EVT_BUTTON, self.m_button_temp_envirFaceChangeDown1OnButtonClick )
		self.m_button_temp_envirFaceChangeUp1.Bind( wx.EVT_BUTTON, self.m_button_temp_envirFaceChangeUp1OnButtonClick )
		self.m_textCtrl_levelHigh.Bind( wx.EVT_CHAR_HOOK, self.m_textCtrl_facechangeOnCharHook )
		self.m_textCtrl_levelHigh.Bind( wx.EVT_LEFT_DCLICK, self.m_textCtrl_facechangeOnLeftDClick )
		self.m_textCtrl_facechange2.Bind( wx.EVT_CHAR_HOOK, self.m_textCtrl_facechange2OnCharHook )
		self.m_textCtrl_facechange2.Bind( wx.EVT_LEFT_DCLICK, self.m_textCtrl_facechange2OnLeftDClick )
		self.m_button_temp_envirFaceChangeDown2.Bind( wx.EVT_BUTTON, self.m_button_temp_envirFaceChangeDown2OnButtonClick )
		self.m_button_temp_envirFaceChangeUp2.Bind( wx.EVT_BUTTON, self.m_button_temp_envirFaceChangeUp2OnButtonClick )
		self.m_button_onSensor.Bind( wx.EVT_BUTTON, self.m_button_onSensorOnButtonClick )
		self.m_button_logcsv.Bind( wx.EVT_BUTTON, self.m_button_logcsvOnButtonClick )
		self.m_button_temp_envirG.Bind( wx.EVT_BUTTON, self.m_button_temp_envirGOnButtonClick )
		self.m_button_moveup.Bind( wx.EVT_BUTTON, self.m_button_moveupOnButtonClick )
		self.m_button_moveleft.Bind( wx.EVT_BUTTON, self.m_button_moveleftOnButtonClick )
		self.m_button_moveright.Bind( wx.EVT_BUTTON, self.m_button_moverightOnButtonClick )
		self.m_button_movebottom.Bind( wx.EVT_BUTTON, self.m_button_movebottomOnButtonClick )
		self.m_button_zoom.Bind( wx.EVT_BUTTON, self.m_button_zoomOnButtonClick )
		self.m_button_zoomout.Bind( wx.EVT_BUTTON, self.m_button_zoomoutOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyDialog_settingOnClose( self, event ):
		event.Skip()

	def m_button_saveOnButtonClick( self, event ):
		event.Skip()

	def m_button_resetOnButtonClick( self, event ):
		event.Skip()

	def m_button_closeOnButtonClick( self, event ):
		event.Skip()

	def m_panel_settingOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_settingOnPaint( self, event ):
		event.Skip()

	def m_button_ffcManualOnButtonClick( self, event ):
		event.Skip()

	def m_button_ffcAutoOnButtonClick( self, event ):
		event.Skip()

	def m_button_ffcTestOnButtonClick( self, event ):
		event.Skip()

	def m_button_fever_downOnButtonClick( self, event ):
		event.Skip()

	def m_button_fever_upOnButtonClick( self, event ):
		event.Skip()

	def m_button_tempktoc_downOnButtonClick( self, event ):
		event.Skip()

	def m_button_tempktoc_upOnButtonClick( self, event ):
		event.Skip()

	def m_button_temp_envirLeptonOnButtonClick( self, event ):
		event.Skip()

	def m_textCtrl_facechangeOnCharHook( self, event ):
		event.Skip()

	def m_textCtrl_facechangeOnLeftDClick( self, event ):
		event.Skip()



	def m_button_temp_envirFaceChangeDownOnButtonClick( self, event ):
		event.Skip()

	def m_button_temp_envirFaceChangeUpOnButtonClick( self, event ):
		event.Skip()



	def m_textCtrl_facechange1OnCharHook( self, event ):
		event.Skip()

	def m_textCtrl_facechange1OnLeftDClick( self, event ):
		event.Skip()

	def m_button_temp_envirFaceChangeDown1OnButtonClick( self, event ):
		event.Skip()

	def m_button_temp_envirFaceChangeUp1OnButtonClick( self, event ):
		event.Skip()



	def m_textCtrl_facechange2OnCharHook( self, event ):
		event.Skip()

	def m_textCtrl_facechange2OnLeftDClick( self, event ):
		event.Skip()

	def m_button_temp_envirFaceChangeDown2OnButtonClick( self, event ):
		event.Skip()

	def m_button_temp_envirFaceChangeUp2OnButtonClick( self, event ):
		event.Skip()

	def m_button_onSensorOnButtonClick( self, event ):
		event.Skip()

	def m_button_logcsvOnButtonClick( self, event ):
		event.Skip()

	def m_button_temp_envirGOnButtonClick( self, event ):
		event.Skip()

	def m_button_moveupOnButtonClick( self, event ):
		event.Skip()

	def m_button_moveleftOnButtonClick( self, event ):
		event.Skip()

	def m_button_moverightOnButtonClick( self, event ):
		event.Skip()

	def m_button_movebottomOnButtonClick( self, event ):
		event.Skip()

	def m_button_zoomOnButtonClick( self, event ):
		event.Skip()

	def m_button_zoomoutOnButtonClick( self, event ):
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


		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )


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


###########################################################################
## Class MyData
###########################################################################

class MyData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data", pos = wx.DefaultPosition, size = wx.Size( 719,200 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, u"C:\\Users\\Admin\\Desktop\\fileJP\\thermalcamera", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR )
		bSizer34.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_buttonok = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_buttonok, 0, wx.ALL, 5 )


		self.SetSizer( bSizer34 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker1OnDirChanged )
		self.m_buttonok.Bind( wx.EVT_BUTTON, self.m_buttonokOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_dirPicker1OnDirChanged( self, event ):
		event.Skip()

	def m_buttonokOnButtonClick( self, event ):
		event.Skip()


