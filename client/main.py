from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import threading
import shared_queue
import receiver
import sander

class sandApp(App):
    def build(self):

        threading.Thread(target=self.itit_conn, daemon=True).start()

        self.is_connected = 0
        self.main_window = FloatLayout()
        print("created layout")
        # username window
        self.username_window = FloatLayout()
        self.username_window_username_textinput = TextInput(hint_text="username ...",
                                                            font_size=30,
                                                            size_hint=(.6, .1),
                                                            pos_hint={'x': .2, 'y': .5},
                                                            background_color=(1, 1, 1, 1),
                                                            foreground_color=(0, 0, 0, 1),
                                                            cursor_color=(0, 0, 0, 1),
                                                            multiline=False)
        self.username_window_room_name_textinput = TextInput(hint_text="room name ...",
                                                            font_size=30,
                                                            size_hint=(.6, .1),
                                                            pos_hint={'x': .2, 'y': .35},
                                                            background_color=(1, 1, 1, 1),
                                                            foreground_color=(0, 0, 0, 1),
                                                            cursor_color=(0, 0, 0, 1),
                                                            multiline=False)
        self.username_window_go_to_chat_button = Button(text="go to chat >",
                                                        font_size=25,
                                                        size_hint=(.4, .1),
                                                        pos_hint={'x': .4, 'y': .1},
                                                        color=(1, 1, 1, 1),
                                                        background_color=(1, 0, 0, .5),
                                                        on_release = self.go_to_chat)
        self.username_window.add_widget(self.username_window_username_textinput)
        self.username_window.add_widget(self.username_window_room_name_textinput)
        self.username_window.add_widget(self.username_window_go_to_chat_button)

        #chat window
        self.chat_window = FloatLayout()

        self.chat_window_scrollview = ScrollView(size_hint=(.98, .8),
                                                            pos_hint={'x': .01, 'y': .15})
        self.chat_window_scrollview_boxlayout = BoxLayout(orientation='vertical',
                                                              spacing=dp(0),
                                                              padding=dp(0),
                                                              size_hint=(1, None),
                                                              height = dp(50),
                                                              pos_hint={'x': 0, 'y': 0})
        self.chat_window_top_chat_label = Button(text='hi, here will appear new messages ....',
                                                                font_size=15,
                                                                size_hint=(1, None),
                                                                height=dp(25),
                                                                color=(1, 1, 1, 1))
        self.chat_window_msg_textinput = TextInput(hint_text="msg ...",
                                                            font_size=20,
                                                            size_hint=(.79, .1),
                                                            pos_hint={'x': .01, 'y': .0},
                                                            background_color=(1, 1, 1, 1),
                                                            foreground_color=(0, 0, 0, 1),
                                                            cursor_color=(0, 0, 0, 1),
                                                            multiline=False)
        self.chat_window_sand_button = Button(text="sand >",
                                                        font_size=20,
                                                        size_hint=(.19, .1),
                                                        pos_hint={'x': .8, 'y': .0},
                                                        color=(1, 1, 1, 1),
                                                        background_color=(1, 1, 1, .1),
                                                        on_release = self.sand_message)
        self.chat_window.add_widget(self.chat_window_scrollview)
        self.chat_window.add_widget(self.chat_window_msg_textinput)
        self.chat_window.add_widget(self.chat_window_sand_button)
        self.chat_window_scrollview.add_widget(self.chat_window_scrollview_boxlayout)
        self.chat_window_scrollview_boxlayout.add_widget(self.chat_window_top_chat_label)

        self.main_window.add_widget(self.username_window)
        return self.main_window


    def go_to_chat(self, instance):
        if str(self.username_window_username_textinput.text) != '' and str(self.username_window_room_name_textinput.text) != '':
            self.main_window.remove_widget(self.username_window)
            self.main_window.add_widget(self.chat_window)
            sander.sand_to_server(str(self.username_window_username_textinput.text), str(self.username_window_room_name_textinput.text), '[info] user connected')
            self.is_connected = 1
            receiver.room_name = str(self.username_window_room_name_textinput.text)
            self.receiver_process = threading.Thread(target=self.listening_process,  daemon=True)
            self.receiver_process.start()
            Clock.schedule_interval(self.get_msgs_from_queue, 0.1)
    def sand_message(self, instance):
        sander.sand_to_server(str(self.username_window_username_textinput.text), str(self.username_window_room_name_textinput.text), str(self.chat_window_msg_textinput.text))
        self.chat_window_msg_textinput.text = ""
    def on_stop(self):
        if self.is_connected == 1:
            sander.sand_to_server(str(self.username_window_username_textinput.text), str(self.username_window_room_name_textinput.text), '[info] user disconnected')
            #self.receiver_process.kill()
    def listening_process(self):
        receiver.start_listening_server()
    def itit_conn(self):
        receiver.initialize()




    def get_msgs_from_queue(self, instance):
        while not shared_queue.queue.empty():
            msg_to_put = shared_queue.queue.get()
            msg_to_put_label = Label(text=msg_to_put,
                                                     font_size=20,
                                                     size_hint=(1, None),
                                                     height=dp(30),
                                                     color=(1, 1, 1, 1),
                                                     halign="left",
                                                     text_size=(Window.width - 20, None))
            self.chat_window_scrollview_boxlayout.add_widget(msg_to_put_label)
            self.chat_window_scrollview_boxlayout.height += 30
            shared_queue.queue.task_done()


sandApp().run()































