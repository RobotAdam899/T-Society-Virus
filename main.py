from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.image import Image

class VirusApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='📛 T-SOCIETY UYARISI\nVeriler Siliniyor...', font_size='20sp', color=(1, 0, 0, 1))
        self.cpu = Label(text='CPU: 98% 🔥🔥🔥', font_size='18sp', color=(1, 0, 0, 1))
        image = Image(source='icon.png')

        layout.add_widget(self.label)
        layout.add_widget(self.cpu)
        layout.add_widget(image)

        Clock.schedule_interval(self.update_cpu, 0.7)
        Clock.schedule_once(self.play_siren, 1)
        return layout

    def update_cpu(self, dt):
        import random
        self.cpu.text = f'CPU: {random.randint(95, 110)}% 🔥🔥🔥'

    def play_siren(self, dt):
        sound = SoundLoader.load('siren.mp3')
        if sound:
            sound.play()

VirusApp().run()
