import pyowm
from pyowm.utils.config import get_default_config
from kivy.uix.label import Label

from kivy.uix.textinput import TextInput


import kivy
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.0.7')

from kivy.app import App

from kivy.uix.button import Button

class TestApp(App):

    twxtinput1 = None
    button1 = None
    button2 = None
    button3 = None
    button4 = None

    def on_enter(self, value):
        print('User pressed enter in', self, value.text)
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = pyowm.OWM ('8669c31fbc7d53c8606c30b75dadc6a1', config_dict)
        mgr = owm.weather_manager()
        message_text = self.textinput1.text
        observation = mgr.weather_at_place(message_text)
        w = observation.weather
        weather_info1 = "В городе " + message_text + "\n Сейчас " + w.detailed_status
        weather_info2 = "Тепература :" + str(w.temperature('celsius')['temp'])
        weather_info3 = "Скорость ветра:" + str(w.wind()["speed"]) + "м/с"
        self.button1.text = weather_info1
        self.button2.text = weather_info2
        self.button3.text = weather_info3


    def build(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = pyowm.OWM ('8669c31fbc7d53c8606c30b75dadc6a1', config_dict)
        mgr = owm.weather_manager()
        message_text = "Самара"
        observation = mgr.weather_at_place(message_text)
        w = observation.weather
        weather_info1 = "В городе " + message_text + "\n Сейчас " + w.detailed_status
        weather_info2 = "Тепература :" + str(w.temperature('celsius')['temp'])
        weather_info3 = "Скорость ветра:" + str(w.wind()["speed"]) + "м/с"



        layout = BoxLayout(orientation="vertical")


        self.textinput1  = TextInput(text=message_text, multiline=False, font_size=40, halign='center', size_hint=(1,0.6))
        self.textinput1.bind(on_validate=self.on_enter)


        self.button1 = Button(text=weather_info1, font_size=40)
        self.button2 = Label(text=weather_info2, font_size=40)
        self.button3 = Button(text=weather_info3, font_size=40)
        self.button4 = Button(text='ПОКАЗАТЬ', font_size=40)
        self.button4.bind(on_press=self.on_enter)

        layout2 = BoxLayout(orientation="horizontal")
        layout2.add_widget(self.textinput1)
        layout2.add_widget(self.button4)

        layout.add_widget(layout2)
        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)

        return layout
if __name__== '__main__':
    TestApp().run()