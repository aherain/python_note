# -*- coding: utf-8 -*-
from cefpython3 import cefpython
import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title='wx', size=(800,600))
        mainPanel = wx.Panel(self)
        windowInfo = cefpython.WindowInfo()
        windowInfo.SetAsChild(mainPanel.GetGtkWidget())
        br = cefpython.CreateBrowserSync(windowInfo,
                                         browserSettings={},
                                         navigateUrl='http://www.zouyesheng.com')

class App(wx.App):
    timer = None

    def OnInit(self):
        self.timer = wx.Timer(self, 1)
        self.timer.Start(10)
        wx.EVT_TIMER(self, 1, lambda e: cefpython.MessageLoopWork())
        frame = MainFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    settings = {
        "locales_dir_path": cefpython.GetModuleDirectory() + "/locales",
        "browser_subprocess_path": cefpython.GetModuleDirectory() + "/subprocess",
    }
    cefpython.Initialize(settings)
    app = App(False)
    app.MainLoop()