from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import *
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.uix.label import *
from kivy.utils import *


Window.clearcolor = (0,0,0,0)


class colors1:
    Ppink = (1,.6,1)
    Ppurple= (1,0,1)
    Pyellow= (255,236,139)
    Pgreen= (0,255,127)
    Pblue = (176,224,230)
    Porange= (255,165,79)
    Pteal = (.25098,.87843,.815686)
    Rred = (1,0,0)
    Rorange = (1,.3922,0)
    Ryellow = (1,1,0)
    Rgreen = (0,1,0)
    Rblue = (0,0,1)
    Rindigo = (.29411765,0,.509804)
    Rviolet = (.93333,.5098,.93333)
    Nblack = (0,0,0)
    Nwhite = (1,1,1)
    Ngray = (.7177,.7177,.7177)
    Npeach = (255,218,185)
    Nbrown = (.54509,.27843,.14902)
    Nlightbrown = (.80392,.40784,.22353)

    
class MyPaintWidget1(Widget):

    def on_touch_down(self, touch): 
        print(self.parent.parent.color)
        print(self.parent.parent.brush)
        with self.canvas:
            wid = 1
            color= colors1.Rindigo
            Color(*(self.parent.parent.color))
            d = 30.
            touch.ud['line'] = Line(points=(touch.x, touch.y), width = self.parent.parent.brush)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    def set_color(self, c):
        print(c)
    pass


class ThirdWindow(Screen):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.painter = MyPaintWidget1()

            self.add_widget(self.painter)


class ForthWindow(Screen):
    pass


class FifthWindow(Screen):
        
    def fill_page(self, f):
        print(f) 


class WindowManager(ScreenManager):


    # Creates funtion inside the screen manager so that they are accessible 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = colors1.Rred
        self.brush = 1
        self.width = 10000

    def set_color(self, c):
        self.color = c
        print(c)

    def set_width(self, wid):
        self.brush = wid
        print(wid)

    def fill_page(self, f):
        self.width = f

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        
        return kv
    

if __name__ == "__main__":
    MyMainApp().run()