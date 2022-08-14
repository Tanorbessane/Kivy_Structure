from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class WidgetsExemple(GridLayout):

    compteur = 1
    mon_texte = StringProperty("1")
    #slider_value_txt = StringProperty("50")
    compteur_actif = BooleanProperty(False)
    text_input_str = StringProperty("toto")
    def on_button_click(self):
        print("Buntton Click")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte= str(self.compteur)
    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
    #def on_slider_value(self,widget):
       # print("Slider: "+ str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self,widget):
        self.text_input_str = widget.text

class MainWidget(Widget):
    pass

class BoxLayoutExemple(BoxLayout):
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.orientation="vertical"
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""
    pass
class AnchorLayoutExemple(AnchorLayout):
    pass
class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
class GridLayoutExemple(GridLayout):
    pass
class LeLabApp(App):
    pass


LeLabApp().run()

