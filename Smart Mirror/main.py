from __future__ import print_function
#python imports
from calendar import monthrange
import datetime
import requests
import json
import math
from time import sleep
import time
#kivy imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import Color
from kivy.animation import Animation
#google api
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.current = 'main_screen'
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # main screen
        if self.current == 'main_screen':
            if keycode[1] == 'down':
                self.transition.direction = 'up'
                self.current = 'news_screen'
            elif keycode[1] == 'left':
                self.transition.direction = 'right'
                self.current = 'calendar_screen'
            elif keycode[1] == 'right':
                self.transition.direction = 'left'
                self.current = 'weather_screen'
            elif keycode[1] == 'escape':
                keyboard.release()



        # news screen
        elif self.current == 'news_screen':
            if keycode[1] == 'up':
                self.transition.direction = 'down'
                self.current = 'main_screen'



        # calendar screen
        elif self.current == 'calendar_screen':
            if keycode[1] == 'right':
                self.transition.direction = 'left'
                self.current = 'main_screen'


        # weather screen
        elif self.current == 'weather_screen':
            if keycode[1] == 'left':
                self.transition.direction = 'right'
                self.current = 'main_screen'
        return True

def to_seconds(date):
    return time.mktime(date.timetuple())# + date.microsecond/1e6


class WeatherWindow(Screen):
    def __init__(self, **kwargs):
        super(WeatherWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.update_weather)
        Clock.schedule_interval(self.update_weather, 3600)
    # on enter event activates
    #def on_enter(self, *args):
    #    print('IM HERE')
    def update_weather(self, *args):


        week = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().weekday())
        monday = week

        week = week.isoformat() + 'Z'
        #print('Getting the upcoming 10 events')
        tuesday = monday + datetime.timedelta(days=1)
        #tuesday = tuesday.isoformat() + 'Z'
        wednesday = monday + datetime.timedelta(days=2)
        #wednesday = wednesday.isoformat() + 'Z'
        thursday = monday + datetime.timedelta(days=3)
        #thursday = thursday.isoformat() + 'Z'
        friday = monday + datetime.timedelta(days=4)
        #friday = friday.isoformat() + 'Z'
        saturday = monday + datetime.timedelta(days=5)
        #saturday = saturday.isoformat() + 'Z'
        sunday = monday + datetime.timedelta(days=6)


        print((int)(to_seconds(monday)))
        #timestamp = timestamp(now)
        #print('Timestamp monday is : ', timestamp)
        #print(timestamp)

        self.url_monday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(monday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_monday = requests.get(self.url_monday)
        self.weather_monday = json.loads(self.json_data_monday.text)

        self.url_tuesday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(tuesday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_tuesday = requests.get(self.url_tuesday)
        self.weather_tuesday = json.loads(self.json_data_tuesday.text)

        self.url_wednesday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(wednesday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_wednesday = requests.get(self.url_wednesday)
        self.weather_wednesday = json.loads(self.json_data_wednesday.text)

        self.url_thursday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(thursday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_thursday = requests.get(self.url_thursday)
        self.weather_thursday = json.loads(self.json_data_thursday.text)

        self.url_friday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(friday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_friday = requests.get(self.url_friday)
        self.weather_friday = json.loads(self.json_data_friday.text)

        self.url_saturday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(saturday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_saturday = requests.get(self.url_saturday)
        self.weather_saturday = json.loads(self.json_data_saturday.text)

        self.url_sunday = 'https://api.darksky.net/forecast/cda4e85d15ffeefbb971fa805d87d1be/59.8586,17.6389,' + str((int)(to_seconds(sunday))) + '?exclude=[minutely,hourly,alerts,flags]&lang=en'
        self.json_data_sunday = requests.get(self.url_sunday)
        self.weather_sunday = json.loads(self.json_data_sunday.text)


        self.ids.monday_weather_label.text = 'High: ' + str(math.ceil((self.weather_monday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.monday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_monday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.monday_weather_description_label.text = str(self.weather_monday['daily']['data'][0]['summary'])

        self.ids.tuesday_weather_label.text = 'High: ' + str(math.ceil((self.weather_tuesday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.tuesday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_tuesday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.tuesday_weather_description_label.text = str(self.weather_tuesday['daily']['data'][0]['summary'])

        self.ids.wednesday_weather_label.text = 'High: ' + str(math.ceil((self.weather_wednesday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.wednesday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_wednesday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.wednesday_weather_description_label.text = str(self.weather_wednesday['daily']['data'][0]['summary'])

        self.ids.thursday_weather_label.text = 'High: ' + str(math.ceil((self.weather_thursday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.thursday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_thursday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.thursday_weather_description_label.text = str(self.weather_thursday['daily']['data'][0]['summary'])

        self.ids.friday_weather_label.text = 'High: ' + str(math.ceil((self.weather_friday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.friday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_friday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.friday_weather_description_label.text = str(self.weather_friday['daily']['data'][0]['summary'])

        self.ids.saturday_weather_label.text = 'High: ' + str(math.ceil((self.weather_saturday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.saturday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_saturday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.saturday_weather_description_label.text = str(self.weather_saturday['daily']['data'][0]['summary'])

        self.ids.sunday_weather_label.text = 'High: ' + str(math.ceil((self.weather_sunday['daily']['data'][0]['temperatureHigh']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C\n'
        self.ids.sunday_weather_label.text += 'Low: ' + str(math.ceil((self.weather_sunday['daily']['data'][0]['temperatureLow']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        self.ids.sunday_weather_description_label.text = str(self.weather_sunday['daily']['data'][0]['summary'])
        #self.ids.saturday_event_label.text = 'No upcoming events found.'
        #sunday = sunday.isoformat() + 'Z'
        #self.label_weather_description = self.ids['label9']
        #print (str(((self.weather['currently']['temperature']-32)*(999999/1000000))))#(5/9))))
        #self.label_weather_description.text = self.weather['currently']['summary']
        #self.label_weather = self.ids['label10']
        #self.label_weather.text = 'WEATHER MOSTLY CLOUDY YOU KNOW!!!!'
        #self.label_weather.text = str(math.ceil((self.weather['currently']['temperature']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        #now = datetime.datetime.now().isoformat() + 'Z'



class CalendarWindow(Screen):
    def __init__(self, **kwargs):
        super(CalendarWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.update_calendar)
        Clock.schedule_interval(self.update_calendar, 5)

    def update_calendar(self, *args):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
        week = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().weekday())
        monday = week

        week = week.isoformat() + 'Z'
        #print('Getting the upcoming 10 events')
        tuesday = monday + datetime.timedelta(days=1)
        #tuesday = tuesday.isoformat() + 'Z'
        wednesday = monday + datetime.timedelta(days=2)
        #wednesday = wednesday.isoformat() + 'Z'
        thursday = monday + datetime.timedelta(days=3)
        #thursday = thursday.isoformat() + 'Z'
        friday = monday + datetime.timedelta(days=4)
        #friday = friday.isoformat() + 'Z'
        saturday = monday + datetime.timedelta(days=5)
        #saturday = saturday.isoformat() + 'Z'
        sunday = monday + datetime.timedelta(days=6)
        #sunday = sunday.isoformat() + 'Z'

        #self.ids.monday_labelaha.text = 'asasdasd'#monday.strftime('20%y-%m-%d')
        #self.ids.tuesday_label.text = tuesday.strftime('20%y-%m-%d')
        #self.ids.wednesday_label.text = wednesday.strftime('20%y-%m-%d')
        #self.ids.thursday_label.text = thursday.strftime('20%y-%m-%d')
        #self.ids.friday_label.text = friday.strftime('20%y-%m-%d')
        #self.ids.saturday_label.text = saturday.strftime('20%y-%m-%d')
        #self.ids.sunday_label.text = sunday.strftime('20%y-%m-%d')


        events_result = service.events().list(calendarId='primary', timeMin=week,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        #eventsJSON = json.json.loads(events)
        self.ids.monday_event_label.text = 'Upcoming events:\n'
        self.ids.tuesday_event_label.text = 'Upcoming events:\n'
        self.ids.wednesday_event_label.text = 'Upcoming events:\n'
        self.ids.thursday_event_label.text = 'Upcoming events:\n'
        self.ids.friday_event_label.text = 'Upcoming events:\n'
        self.ids.saturday_event_label.text = 'Upcoming events:\n'
        self.ids.sunday_event_label.text = 'Upcoming events:\n'


        if not events:
            self.ids.monday_event_label.text = 'No upcoming events found.'
            self.ids.tuesday_event_label.text = 'No upcoming events found.'
            self.ids.wednesday_event_label.text = 'No upcoming events found.'
            self.ids.thursday_event_label.text = 'No upcoming events found.'
            self.ids.friday_event_label.text = 'No upcoming events found.'
            self.ids.saturday_event_label.text = 'No upcoming events found.'
            self.ids.sunday_event_label.text = 'No upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))

            if convert_start_getdate(start) == monday.strftime('20%y-%m-%d'):
                self.ids.monday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')
            elif convert_start_getdate(start) == tuesday.strftime('20%y-%m-%d'):
                self.ids.tuesday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')
            elif convert_start_getdate(start) == wednesday.strftime('20%y-%m-%d'):
                self.ids.wednesday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')
            elif convert_start_getdate(start) == thursday.strftime('20%y-%m-%d'):
                self.ids.thursday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')
            elif convert_start_getdate(start) == friday.strftime('20%y-%m-%d'):
                self.ids.friday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')
            elif convert_start_getdate(start) == saturday.strftime('20%y-%m-%d'):
                self.ids.saturday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')
            elif convert_start_getdate(start) == sunday.strftime('20%y-%m-%d'):
                self.ids.sunday_event_label.text +=  str(convert_start_getdate(start) + '\n' + convert_start_gettime(start)[: -3] + '\n' +  event['summary'] + '\n')


def convert_start_getdate(args):
    getdate = ''
    for str in args:
        if str != 'T':
            getdate += str
        else:
            break
    return getdate

def convert_start_gettime(args):
    getTime = ''
    flag = False
    for str in args:
        if str == '+':
            break
        if flag == True:
            getTime += str
        if str == 'T':
            flag = True

    return getTime

class NewsWindow(Screen):
    def __init__(self, **kwargs):
        super(NewsWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.update_news)
        Clock.schedule_interval(self.update_news, 3600)

    def update_news(self, *args):
        self.url = 'ADD URL HERE'
        #self.url = 'https://newsapi.org/v2/top-headlines?country=se&apiKey=f85b5e6aef924d8b8f87c27adde953e2'
        #self.ids.saturday_event_label.text
        self.json_data = requests.get(self.url)
        self.news = json.loads(self.json_data.text)
        self.ids.author.text = 'Author: '
        self.ids.author.text += self.news['articles'][1]['author']
        self.ids.title.text = 'Title: '
        self.ids.title.text += self.news['articles'][1]['title']
        self.ids.description.text = 'Description: '
        self.ids.description.text += self.news['articles'][1]['description']
        self.ids.url.text = 'Url: '
        self.ids.url.text += self.news['articles'][1]['url']
        self.ids.content.text = 'Content: '
        self.ids.content.text += self.news['articles'][1]['content']
        #self.label_news = self.ids['label7']
        #self.label_news.text = 'Science News: '  + self.news['articles'][1]['title'] +'\n'


class MainWindow(Screen):

    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    intro = BooleanProperty(False)


    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.entrance)
        Clock.schedule_once(self.entrance, 7)
        Clock.schedule_interval(self.update_time, 0.5)
        Clock.schedule_once(self.update_weather)
        Clock.schedule_interval(self.update_weather, 3600)
        Clock.schedule_once(self.update_calendar)
        Clock.schedule_interval(self.update_calendar, 5)
        Clock.schedule_once(self.update_news)
        Clock.schedule_interval(self.update_news, 3600)




    #def entrance(self):
    #    self.label_entrance = self.ids['Label5']
    #    anim = Animation (opacity = 0, duration = 7, on_complete=hide_label).start(self.label_entrance)

    def entrance(self, *args):
        if self.intro == True:
            self.label_entrance = self.ids['label5']
            self.label_entrance.color = [0,0,0,0]
        else:
            self.intro = True

    def update_time(self, *args):
        self.now = datetime.datetime.now()
        self.label_time = self.ids['label3']
        self.label_time.text = self.now.strftime('%H:%M:%S %A')

    def update_weather(self, *args):
        self.url = 'ADD URL HERE'
        self.json_data = requests.get(self.url)
        self.weather = json.loads(self.json_data.text)
        self.label_weather_description = self.ids['label9']
        #print (str(((self.weather['currently']['temperature']-32)*(999999/1000000))))#(5/9))))
        self.label_weather_description.text = self.weather['currently']['summary']
        self.label_weather = self.ids['label10']
        #self.label_weather.text = 'WEATHER MOSTLY CLOUDY YOU KNOW!!!!'
        self.label_weather.text = str(math.ceil((self.weather['currently']['temperature']-32)/(1.8))) + u'\N{DEGREE SIGN}'+'C'
        #now = datetime.datetime.now().isoformat() + 'Z'

    def update_calendar(self, *args):
        self.label_calendar = self.ids['label1']

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=3, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        self.label_calendar.text = 'Upcoming events:\n'

        if not events:
            self.label_calendar.text = 'No upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            #print(start, event['summary'])
            #self.label_calendar.text = str(start + '\n' + event['summary'])
            if convert_start_getdate(start) == datetime.datetime.today().strftime('20%y-%m-%d'):
                self.label_calendar.text +=  str(convert_start_gettime(start)[: -3] + ' ' + event['summary'] + '\n')

    def update_news(self, *args):
        self.url = 'ADD URL HERE'
        #self.url = 'https://newsapi.org/v2/top-headlines?country=se&apiKey=f85b5e6aef924d8b8f87c27adde953e2'
        self.json_data = requests.get(self.url)
        self.news = json.loads(self.json_data.text)
        self.label_news = self.ids['label7']
        self.label_news.text = 'Bitcoin News: '  + self.news['articles'][1]['title'] +'\n'

class SmartMirror(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    #Window.fullscreen = True
    #Window.fullscreen = 'auto'

    SmartMirror().run()
