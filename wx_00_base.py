#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

import wx

# 每个wxPython的程序必须有一个wx.App对象.
app = wx.App() 

frame = wx.Frame(None, -1, title='wx_00_base.py', pos=(300,400), size=(200,150))
#frame.Centre()
frame.Show()
print "hello world"
print "fff"
# 进入循环，等待响应
app.MainLoop()
