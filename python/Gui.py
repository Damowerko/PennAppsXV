import wx
import threading

WHITE_COLOR = (255, 255, 255)


class wave():
        # 1 is up, 2 down, 3 is left, 4 is right

    def __init__(self, direction, makeable):
        self.makeable = makeable
        self.ready = False
        self.count = 0
        self.direc = direction
        self.x = 0
        self.y = 0
        self.start = 0
        self.end = 0
        self.dx = 0
        self.dy = 0
        if(self.direc == 1):
            self.y = -40
            self.x = 240
            self.start = 210
            self.end = 330
            self.dx = 0
            self.dy = 8
        if(self.direc == 2):
            self.y = 540
            self.x = 240
            self.start = 30
            self.end = 150
            self.dx = 0
            self.dy = -8
        if(self.direc == 3):
            self.y = 240
            self.x = -50
            self.start = 300
            self.end = 420
            self.dx = 8
            self.dy = 0
        if(self.direc == 4):
            self.y = 240
            self.x = 540
            self.start = 120
            self.end = 240
            self.dx = -8
            self.dy = 0

    def draw(self, dc):
        dc.DrawEllipticArc(self.x, self.y, 100, 100, self.start, self.end)

    def makeNew(self):
        temp = self.ready
        if(self.ready):
            self.ready = False
        return self.makeable and temp

    def tick(self, dc):
        self.draw(dc)
        self.y += self.dy
        self.x += self.dx

        self.count += 1

        if self.count == 5 or self.count == 10:
            self.ready = True
        if(self.direc == 1 and self.y > 40):
            return True
        if(self.direc == 2 and self.y < 463):
            return True
        if(self.direc == 3 and self.x > 36):
            return True
        if(self.direc == 4 and self.x < 460):
            return True
        return False


class SoundSource():
        # takes a direction in radians
    def __init__(self, direction):
        center_y = 250
        center_x = 240
        self.x = 200 * Math.sin(direction) + center_x
        self.y = 200 * Math.cos(direction) + center_y
        self.radius = 20
        self.dx = 0  # repeats between 0 and 5

    def draw(self, dc):
        dc.DrawEllipse(self.x - self.radius, self.y -
                       self.radius, self.radius * 2, self.radius * 2)


class AnimationPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.Colour(*WHITE_COLOR))
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.waves = []
        self.waves.append(wave(2, True))
        self.timer.Start(20)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        # dc.SetBrush(wx.Brush("blue"))
        dc.SetPen(wx.Pen('black', 30))
        dc.DrawEllipse(150, 150, 300, 300)
        dc.SetPen(wx.Pen('cyan', 8))
        for w in self.waves:
            if(w.tick(dc)):
                self.waves.remove(w)
            if(w.makeNew()):
                self.waves.append(wave(w.direc, False))
        # dc.DrawRectangle(150, 120, 100, 100)

    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_LEFT:
            self.waves.append(wave(3, True))
        if keycode == wx.WXK_DOWN:
            self.waves.append(wave(2, True))
        if keycode == wx.WXK_UP:
            self.waves.append(wave(1, True))
        if keycode == wx.WXK_RIGHT:
            self.waves.append(wave(4, True))

    def OnTimer(self, event):
        self.Refresh()
        # self.waves.append(wave(1))s
        # self.waves.append(wave(2))
        # self.waves.append(wave(3))
        # self.waves.append(wave(4))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Belt Visualization", size=(600, 600))
        AnimationPanel(self)

class Gui():
    def __init__(self):
    app = wx.App()
	   frame = MainFrame()
	   frame.Show(True)
	   app_thread = threading.Thread(target=app.MainLoop(), name='App Thread')
	   app_thread.start()


if __name__ == "__main__":
    app_thread1 = threading.Thread(target=Gui(), name='App Thread1')
    app_thread1.start()


