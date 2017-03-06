from kivy.app import App
from kivy.uix.button import Button

class abu(App):
	def build(self):
		return Button(text="hello world", font_size=40)

a=abu()
a.run()

