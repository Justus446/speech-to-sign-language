from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.video import Video
from kivy.clock import Clock
from kivy.uix.label import Label
import speech_recognition as sr
import os

Clock.max_iteration = 20

Builder.load_file('smain.kv')

class MainWindow(Screen):
    def quit(self):
        App.get_running_app().stop()

    def speak(self):
        self.ids.output_label.text = "Listening..."
        self.listen(self.ids.lang_spinner.text)

    def translate(self):
        lang = self.ids.lang_spinner.text
        self.ids.output_label.text = f"Translating from {lang}..."
        self.ids.video_display.source = 'sample_video.mp4'
        self.ids.video_display.state = 'play'

    def listen(self, language):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something")
            audio = recognizer.listen(source)
            recognizer.adjust_for_ambient_noise(source)

        print("Processing")
        try:
            recognized_text = recognizer.recognize_google(audio)
            print(recognized_text)
            recognized_words = set(recognized_text.lower().split())
            if language == 'English':
                known_words = {'bad', 'begin', 'father', 'fine', 'good', 'i', 'like', 'mother', 'no', 'you', 'yes', 'know', 'understand'}
            else:
                known_words = {'bueno', 'padre', 'yo', 'intiendo', 'tu', 'no', 'si'}

            if recognized_words.intersection(known_words):
                self.ids.output_label.text = recognized_text
                for word in recognized_text.split():
                    video_file = f'{word}.mp4'
                    if os.path.exists(video_file):
                        vid = Video(source=video_file, pos_hint={'center_x': .3, 'top': 1}, size_hint=(.9, .8))
                        vid.state = 'play'
                        self.add_widget(vid)
            else:
                self.ids.output_label.text = "WORD NOT FOUND"
        except sr.UnknownValueError:
            self.ids.output_label.text = "Sorry, I did not understand that."
        except sr.RequestError:
            self.ids.output_label.text = "Sorry, there was an error with the request."

class Window1(Screen):
    def quit(self):
        App.get_running_app().stop()

    def help(self):
        vid = Video(source='justus.mp4', pos_hint={'center_x': .3, 'top': 1}, size_hint=(.9, .8))
        vid.state = 'play'
        self.add_widget(vid)
        lbl = Label(
            text="TO Translate : press English/Spanish \n TO Quit: press Quit \n [for more info visit www.translator.com]",
            font_size='14sp', pos_hint={'x': 0, 'y': .1}, size_hint=(.6, .099))
        self.add_widget(lbl)

    def about(self):
        lbl = Label(text=" [for more info visit www.translator.com]", font_size='14sp', pos_hint={'x': 0, 'y': .1},
                    size_hint=(.6, .099))
        self.add_widget(lbl)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.r = sr.Recognizer()
        self.eng_list = ['bad', 'begin', 'father', 'fine', 'good', 'i', 'like', 'mother', 'no', 'you', 'yes', 'know',
                         'understand']
        self.span_list = ['bueno', 'padre', 'yo', 'intiendo', 'tu', 'no', 'si']
        self.text = ''
        self.eng_set = {}
        self.span_set = {}

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return WindowManager()

if __name__ == "__main__":
    MainApp().run()
