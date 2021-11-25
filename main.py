#using the kivymd lib
#Note: we cannot use a seperate kv file as they want submissions in .py or .exe
#Note: I doubt if we can use inline KV Language as we chose Python, so i doubt this


from kivymd.uix import textfield
from kivymd.uix.screen import MDScreen
from kivy.config import Config
from kivy.lang import Builder, builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextFieldRound
from kivy.uix.screenmanager import ScreenManager,Screen



screenn = """
ScreenManager:
   app:
   mainn:

<app>:
    name: 'login'
    MDRectangleFLatButton:
        text: 'Enter'
        pos_hint={"center_x":0.5,"center_y":0.16} 


<mainn>:
    name: 'home'
    MDLabel:
        text: "welcome"
        halign: "center"
    
"""




# Config.set('kivy','keyboard_mode','systemanddock')  # to enable the virtual keyboard
class mainn(MDApp,Screen):
    pass


class app(MDApp,Screen):


    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.login1 = MDLabel(text="Login",font_style="H6",size_hint=(0.5,0.35),bold=True)
        self.login1.pos_hint = {"center_x": 0.71,"center_y": 0.51}
        


        self.logo = Image(source="background.jpg",)
        self.logo = Image(source='logo',size_hint=(0.5,0.3))
        self.logo.pos_hint = {"center_x":0.5,"center_y":0.75}


        self.uname = MDTextField(hint_text="Enter name", halign="left",mode='rectangle',size_hint=(0.65,1))
        self.uname.pos_hint = {"center_x":0.5,"center_y":0.45}


        self.email = MDTextField(hint_text="Enter email",halign="left",mode='rectangle',size_hint=(0.65,1))
        self.email.pos_hint = {"center_x":0.5,"center_y":0.34}


        self.paswd = MDTextField(hint_text="Enter password",halign="left",mode='rectangle',size_hint=(0.65,1))
        self.paswd.pos_hint = {"center_x":0.5,"center_y":0.25}

    
        self.enterb = MDFillRoundFlatButton(text="enter",font_size=18,font_style="Button", pos_hint={"center_x":0.5,"center_y":0.16})




        screen.add_widget(self.logo)
        screen.add_widget(self.uname)
        screen.add_widget(self.email)
        screen.add_widget(self.paswd)
        screen.add_widget(self.login1)
        # screen.add_widget(self.enterb)
        return screen


sm = ScreenManager()
sm.add_widget(app(name='login'))
sm.add_widget(mainn(name='home'))


if __name__ == '__main__':
    app().run()