from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
          
class TefterApp(App):
      
    def build(self):
                
        layout = FloatLayout(size=(540,490))
                     
        txt_put = TextInput(multiline=True, size_hint=(.4, .1), pos_hint={'x': .0, 'y': .89})
        txt_put1 = TextInput(multiline=True, size_hint=(.1, .1), pos_hint={'x': .45, 'y': .89})
        
     
        but_eql = Button(text=' = ', size_hint=(.05, .05), pos_hint={'x': .55, 'y': .915})
        
        layout.add_widget(but_eql)
      
        layout.add_widget(txt_put)
        layout.add_widget(txt_put1)
            
        return layout    
        
    
            
  
if __name__ == '__main__':
    app = TefterApp()
    app.run()   
