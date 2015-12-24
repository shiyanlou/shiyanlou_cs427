#
import wx

class Example(wx.Frame):
    def __init__(self,title):
        super(Example,self).__init__(None,title=title,size=(250,150))
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Centre()
        self.Show()
    def OnPaint(self,e):
        dc=wx.PaintDC(self)
        dc.DrawLine(50,60,190,60)

if __name__=="__main__":
    app=wx.App()
    Example('line')
    app.MainLoop()
