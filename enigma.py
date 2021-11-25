from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix import navigationdrawer
from kivymd.uix import boxlayout
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.list import MDList
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.navigationdrawer import MDNavigationDrawer



screen_helper = """

ScreenManager:
    LoginScreen:
    MenuScreen:
    NewScreen:


<LoginScreen>:
    name: 'login'
    Image:
        source: 'logo'
        pos_hint:{"center_x":0.5,"center_y":0.83}
        size_hint:(0.5,0.3)

    MDLabel:
        text: 'Login'
        pos_hint:{"center_x": 0.5,"center_y": 0.63}
        halign: 'center'
        font_style: 'H6'
        bold:True

    MDTextField:
        hint_text:"Enter name"
        multiline: False
        halign:"left"
        pos_hint:{"center_x":0.5,"center_y":0.55}
        mode: "rectangle"
        size_hint:(0.5,0.1)

    MDTextField:
        hint_text:"Enter password"
        multiline: False
        halign:"left"
        pos_hint:{"center_x":0.5,"center_y":0.43}
        mode: "rectangle"
        size_hint:(0.5,0.1)

    MDFillRoundFlatButton:
        text:"Enter"
        pos_hint:{"center_x":0.5,"center_y":0.29}
        size_hint:(0.17,0.07)
        font_size:20
        on_press: 
            root.manager.current = 'nav'

    
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Home"
        MDBottomNavigation:



            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'hello world'
                icon: 'language-python'

                MDLabel:
                    text: "Hello there"
                    halign: "center"
            
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'hello peter'
                icon: 'youtube'

                MDLabel:
                    text: "you are not peter!"
                    halign: "center"

<NewScreen>:
    name: "nav"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Menu"
                        left_action_items: [["menu",lambda x:nav_drawer.set_state('toggle')]]
                        elevation: 10
                        
                    Widget  

                    
            
        MDNavigationDrawer:
            id: nav_drawer
"""



class LoginScreen(Screen):
    pass


class MenuScreen(Screen,BoxLayout):
    pass

class NewScreen(Screen,BoxLayout):
   pass



#screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))
sm = ScreenManager(transition=SlideTransition())






class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        screen = Builder.load_string(screen_helper)
        # screen1 = Builder.load_string(screen1)
        return screen


DemoApp().run()