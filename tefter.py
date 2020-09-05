from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

blue =  [0,0,1,1]

class TefterApp(App):
   
    def build(self):
        
        layout = BoxLayout(orientation='horizontal')
        
        txt_put = TextInput(multiline=True, size_hint=(.7, .1), pos_hint={'center_x': .1, 'center_y': .9})
        txt_put1 = TextInput(multiline=True, size_hint=(.3, .1), pos_hint={'center_x': .1, 'center_y': .9})
        
        
        layout.add_widget(txt_put)
        layout.add_widget(txt_put1)
            
        return layout    
        
    
            
  
if __name__ == '__main__':
    app = TefterApp()
    app.run()    
    