# from moviepy.editor import *

from kivy.app import App
import sys
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.lang import Builder
import speech_recognition as sr

Clock.max_iteration = 20

span_list = ['bueno', 'padre', 'yo', 'intiendo', 'tu', 'no', 'si']


class MainWindow(Screen):
    # QUIT button
    def quit(self):
        sys.exit(0)


class Window1(Screen):
    def quit(self):
        sys.exit(0)

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
        self.audio = 'dfghjk'
        self.eng_list = ['bad', 'begin', 'father', 'fine', 'good', 'i', 'like', 'mother', 'no', 'you', 'yes', 'know',
                         'understand']
        self.span_list = ['bueno', 'padre', 'yo', 'intiendo', 'tu', 'no', 'si']
        self.text = ''
        self.eng_set = {}
        self.span_set = {}

    # turn on mic and listen
    def english(self):
        with sr.Microphone() as source:
            print("say something")
            audio = self.r.listen(source)

            self.r.adjust_for_ambient_noise(source)

        print("good")

        lis = self.r.recognize_google(audio)

        print(lis)
        lis = str(lis)

        print(lis.split(" "))
        lis = lis.split()

        audio_ = set(lis)
        print(audio_)

        self.eng_set = set(self.eng_list)
        print(self.eng_set)
        if audio_.intersection(self.eng_set):
            print("done")

            self.text = str(lis)
            lbl = Label(text=self.text, font_size='20sp', pos_hint={'x': 0, 'y': .1}, size_hint=(.6, .099))
            self.add_widget(lbl)
            # audio = list(audio)

            for word in lis:
                word = word + '.mp4'
                print(word)
                vid = Video(source=word, pos_hint={'center_x': .3, 'top': 1}, size_hint=(.9, .8))
                vid.state = 'play'
                self.add_widget(vid)

        else:
            print("not done")
            lbl = Label(text="WORD NOT FOUND", font_size='20sp', pos_hint={'x': 0, 'y': .1}, size_hint=(.6, .099))
            self.add_widget(lbl)

    def spanish(self):
        with sr.Microphone() as source:
            print("say something")
            audio = self.r.listen(source)

            self.r.adjust_for_ambient_noise(source)

        print("good")

        lis = self.r.recognize_google(audio)

        print(lis)
        lis = str(lis)

        print(lis.split(" "))
        lis = lis.split()

        audio_ = set(lis)
        print(audio_)

        self.span_set = set(self.span_list)
        print(self.span_set)
        if audio_.intersection(self.span_set):
            print("done")

            self.text = str(lis)
            lbl = Label(text=self.text, font_size='20sp', pos_hint={'x': 0, 'y': .1}, size_hint=(.6, .099))
            self.add_widget(lbl)
            # audio = list(audio)

            for word in lis:
                word = word + '.mp4'
                print(word)
                vid = Video(source=word, pos_hint={'center_x': .3, 'top': 1}, size_hint=(.9, .8))
                vid.state = 'play'
                self.add_widget(vid)

        else:
            print("not done")
            lbl = Label(text="WORD NOT FOUND", font_size='20sp', pos_hint={'x': 0, 'y': .1}, size_hint=(.6, .099))
            self.add_widget(lbl)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('smain.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MainApp().run()
