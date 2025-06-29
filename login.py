from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.floatlayout import MDFloatLayout
#from kivy.uix.button import Button
from kivy.uix.widget import Widget
import mysql.connector
import re
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.properties import ListProperty, StringProperty , BooleanProperty
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from main import MainScreen


class PreSplash(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass
class AddScreen(Screen):
    pass
class AddincomeScreen(Screen):
    pass
class AddexpenseScreen(Screen):
    pass
class ShowexpenseScreen(Screen):
    con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pas"
        )
    d = con.cursor()
    def load_table(self,r):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.8, 0.9),
            padding=50,
            use_pagination=True,
            check=True,
            rows_num=8,
            elevation=20,
            background_color_header="#4343f7",
            background_color_selected_cell="#36f569",
            column_data=[
                ("expense id", dp(30)),
                ("source", dp(30)),
                ("date", dp(30)),
                ("amount", dp(30)),
                 ],
             )
        for x in r:
            self.data_tables.add_row(x)
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        query = "select * from expenseinfo"
        self.d.execute(query)
        self.r = self.d.fetchall()
        self.load_table(self.r)
        
        
class ShowincomeScreen(Screen):
    con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pas"
        )
    d = con.cursor()
    def load_table(self,r):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.8, 0.9),
            padding=50,
            use_pagination=True,
            check=True,
            rows_num=8,
            elevation=20,
            background_color_header="#4343f7",
            background_color_selected_cell="#36f569",
            column_data=[
                ("income id", dp(30)),
                ("source", dp(30)),
                ("date", dp(30)),
                ("amount", dp(30)),
                 ],
             )
        for x in r:
            self.data_tables.add_row(x)
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        query = "select * from incomeinfo"
        self.d.execute(query)
        self.r = self.d.fetchall()
        self.load_table(self.r)
        
        
        
        
        
class ShowScreen(Screen):
    pass




class PAS (MDApp):
    
    
    btn_color = ListProperty((177/255, 35/255, 65/255, 1))
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    database = mysql.connector.Connect(host="localhost", user="root", password="", database="pas")
    cursor = database.cursor()
    
    def build(self):
        global manager
        manager = ScreenManager()
        manager.add_widget(Builder.load_file("pre_splash.kv"))
        manager.add_widget(Builder.load_file("login.kv"))
        manager.add_widget(Builder.load_file("signup.kv"))
        manager.add_widget(MainScreen(name="main"))
        manager.add_widget(Builder.load_file("addinfo.kv"))
        manager.add_widget(Builder.load_file("addincome.kv"))
        manager.add_widget(Builder.load_file("addexpense.kv"))
        manager.add_widget(Builder.load_file("showinfo.kv"))
        manager.add_widget(Builder.load_file("showexpense.kv"))
        manager.add_widget(Builder.load_file("showincome.kv"))
        #manager.add_widget(AddScreen(name="addinfo"))
        return manager
    
    def get_id(self, instance):
        for id, widget in instance.parent.parent.parent.parent.ids.items():
            if widget.__self__ == instance:
                return id
    
    def change_color(self, instance):
        if self.get_id(instance) == "color1":
            self.btn_color = (139/255, 202/255, 193/255, 1)
        elif self.get_id(instance) == "color2":
            self.btn_color = (177/255, 35/255, 65/255, 1)
        elif self.get_id(instance) == "color3":
            self.btn_color = (99/255, 102/255, 241/255, 1)
    
    def send_info(self, fullname, email, npasswrd, cpasswrd):
        if re.fullmatch(self.regex, email.text):
            if(npasswrd.text==cpasswrd.text):
                self.cursor.execute(f"INSERT INTO logininfo VALUES('{fullname.text}', '{email.text}', '{cpasswrd.text}')")
                self.database.commit()
                fullname.text=""
                email.text=""
                npasswrd.text=""
                cpasswrd.text=""
                
    def send_income_info(self, income_id, source, date, amount):
        self.cursor.execute(f"INSERT INTO incomeinfo VALUES('{income_id.text}', '{source.text}', '{date.text}', '{amount.text}')")
        self.database.commit()
        income_id.text=""
        source.text=""
        date.text=""
        amount.text=""
        
    def send_expense_info(self, expense_id, source, date, amount):
        self.cursor.execute(f"INSERT INTO expenseinfo VALUES('{expense_id.text}', '{source.text}', '{date.text}', '{amount.text}')")
        self.database.commit()
        expense_id.text=""
        source.text=""
        date.text=""
        amount.text=""
    
    def receive_info(self, email, cpasswrd):
        #manager.current = "main"
        self.cursor.execute("select email, cpasswrd from logininfo")
        '''manager.current = "main"'''
        email_list = []
        for i in self.cursor.fetchall():
            email_list.append(i[0])
        if email.text in email_list and email.text !="":
            self.cursor.execute(f"select cpasswrd from logininfo where email='{email.text}'")
            for j in self.cursor:
                if cpasswrd.text == j[0]:
                    manager.current = "main"
                else:
                    print("Incorrect Password!")
        else:
            print("Incorrect Email!")
        
        email.text=""
        cpasswrd.text=""
        
    def add_info(self, *args): 
        manager.current = "addinfo"
    def show_info(self, *args): 
        manager.current = "showinfo"
    def add_income(self, *args): 
        manager.current = "addincome"
        
    def add_expense(self, *args): 
        manager.current = "addexpense"
        
    def show_expense(self, *args): 
        manager.current = "showexpense"
    
    def show_income(self, *args): 
        manager.current = "showincome"
    
    def on_start(self):
        Clock.schedule_once(self.login,15)
    
    def login(self, *args):
        manager.current = "login"


if __name__ == "__main__":
    PAS().run()
                    