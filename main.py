from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size=(800,600)
Window.minimum_width, Window.minimum_height=Window.size


class FirstWindow(Screen):
    pass
class SearchInConstitution(Screen):
    pass
class SearchInCriminalCode(Screen):
    pass
class SearchInAdminCode(Screen):
    pass
class ResultsInConst(Screen):
    pass
class ResultInCriminalCode(Screen):
    pass
class ResultInAdminCode(Screen):
    pass



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my1kv.kv')

class LegRefRFApp(App):
    def build(self):
        return kv


if __name__=='__main__':
    LegRefRFApp().run()