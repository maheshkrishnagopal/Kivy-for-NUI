import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout


class IsilonHomeLogin(BoxLayout):
    def choice(self):
         self.ids.result.text='Please provide valid credentials'


class MyApp(App):

    def build(self):
        return IsilonHomeLogin()


if __name__ == '__main__':
    MyApp().run()