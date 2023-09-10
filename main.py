from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Kivy-Flask!'

class KivyFlaskApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text=hello_world(), font_size=24)
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    app.run(debug=True)
    KivyFlaskApp().run()
