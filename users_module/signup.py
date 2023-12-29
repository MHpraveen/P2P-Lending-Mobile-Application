import re

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import sqlite3

from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton

KV = """
<SignupScreen>:
    ScrollView:
        do_scroll_x: False

        canvas.before:
            Color:
                rgba: 174/255, 214/255, 241/255, 1
            Rectangle:
                size: self.size
                pos: self.pos


        GridLayout:
            cols: 1
            height: self.minimum_height
            spacing: 1
            padding:40
            pos_hint: {'center_x': 0.1,'center_y': 0.5}


            MDLabel:
                id: label1
                text: 'Sign Up         '
                font_size: 30
                halign: 'center'
                font_name: "Roboto-Bold"
                pos_hint: {'top': 1, 'left': 1}  
                height: self.texture_size[1]
                padding: 15



            MDTextField:
                id: name
                hint_text: 'Enter full name'
                multiline: False
                helper_text: 'Enter a valid name'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                size_hint_x: None
                height: self.minimum_height
                icon_left: 'account'
                width: 370
                spacing: 15
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1  
                helper_text_color: 0, 0, 0, 1  
                pos_hint: {'center_y': 0.1}  
            MDTextField:
                id: mobile
                hint_text: 'Enter mobile number'
                multiline: False
                helper_text: 'Enter a valid number'
                helper_text_mode: 'on_focus'
                size_hint_x: None
                height: self.minimum_height
                icon_left: 'cellphone'
                width: 370
                font_name: "Roboto-Bold"

            MDTextField:
                id: email
                hint_text: 'Enter your email'
                multiline: False
                helper_text: 'Enter a valid email'
                helper_text_mode: 'on_focus'
                size_hint_x: None
                height: self.minimum_height
                icon_left: 'email'
                width: 370
                font_name: "Roboto-Bold"

            MDTextField:
                id: password
                hint_text: "Enter Your Password"
                icon_left: 'lock-outline'
                helper_text_mode: 'on_focus'
                height: self.minimum_height
                size_hint_x: None
                multiline: False
                width: 370
                helper_text: "Password must be greater than 8 characters"
                font_size: 23
                password: True
                font_name: "Roboto-Bold"

            MDTextField:
                id: password2
                hint_text: "Re-Enter Your Password"
                helper_text: "Password does not match"
                helper_text_mode: 'on_focus'
                icon_left: 'lock-outline'
                size_hint_x: None
                width: 370
                font_size: 22
                password: True
                font_name: "Roboto-Bold"

            BoxLayout:
                orientation: 'horizontal'
                size_hint: None, None
                width: "260dp"
                height: "35dp"
                MDCheckbox:
                    id: terms_checkbox
                    size_hint_x: None
                    width: "20dp"
                MDLabel:
                    text: "Terms and Conditions"
                    font_size: 16
                    theme_text_color: 'Custom'
                    text_color: 6/255, 143/255, 236/255, 1
                    halign: 'left'
                    valign: 'center'
                    on_touch_down: app.root.get_screen("SignupScreen").show_terms_dialog() if self.collide_point(*args[1].pos) else None

            BoxLayout:
                orientation: 'horizontal'
                size_hint: None, None
                width: "260dp"
                height: "25dp"
                MDCheckbox:
                    id: kyc_checkbox
                    size_hint_x: None
                    width: "20dp"
                MDLabel:
                    text: "I authorize the company to fetch my KYC details via the Central KYC(CKYC) Registry"
                    font_size: 16
                    theme_text_color: 'Primary'
                    halign: 'left'
                    valign: 'center'

            MDCard:
                size_hint: None, None
                size: "300dp", "86dp"
                pos_hint: {'center_x': 0.1, 'center_y': 0.5}
                md_bg_color: 1, 1, 1, 0  # Card background color

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 20
                    padding:50
                    MDRectangleFlatButton:
                        text: "Back"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 6/255, 143/255, 236/255, 1
                        on_release: app.root.get_screen("MainScreen").manager.current = 'MainScreen'
                        font_name: "Roboto-Bold"
                        size_hint_y: None
                        size: "150dp", "50dp"
                        pos_hint: {'center_x': 0.5}
                    MDRectangleFlatButton:
                        text: "Signup"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 6/255, 143/255, 236/255, 1
                        on_release: root.go_to_login()
                        size_hint_y: None
                        size: "150dp", "50dp"
                        font_name: "Roboto-Bold"
                        pos_hint: {'center_x': 0.5}




"""

# Connect to the SQLite database
conn = sqlite3.connect("user_profile.db")
cursor = conn.cursor()

# Create a table named 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT,
        mobile_number TEXT,
        password TEXT,
        confirm_password TEXT,
        accept_terms TEXT,  -- Column for the "Terms and Conditions" checkbox
        authorize_kyc TEXT   -- Column for the "Authorize KYC" checkbox
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()


class SignupScreen(Screen):
    Builder.load_string(KV)

    def save_to_database(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect("user_profile.db")
            cursor = conn.cursor()

            cursor.execute('SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1')
            latest_user_id = cursor.fetchone()

            if latest_user_id is not None:
                next_user_id = latest_user_id[0] + 1
            else:

                next_user_id = 1000

            cursor.execute('''
                INSERT INTO users (
                    user_id, fullname, email, mobile_number, password, confirm_password,
                    accept_terms, authorize_kyc
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                next_user_id,
                self.ids.name.text, self.ids.email.text, self.ids.mobile.text,
                self.ids.password.text, self.ids.password2.text,
                "Accepted" if self.ids.terms_checkbox.active else "Rejected",
                "Accepted" if self.ids.kyc_checkbox.active else "Rejected"
            ))

            conn.commit()
        except sqlite3.Error as e:

            print(f"SQLite error: {e}")
        finally:

            if conn:
                conn.close()

    def go_to_login(self):
        name = self.ids.name.text
        mobile = self.ids.mobile.text
        email = self.ids.email.text
        password = self.ids.password.text
        password2 = self.ids.password2.text
        terms_checkbox = self.ids.terms_checkbox
        kyc_checkbox = self.ids.kyc_checkbox

        validation_errors = []

        if not name or not (name.isalpha() and len(name) >= 4):
            validation_errors.append((self.ids.name, "Please enter an valid name"))

        if not mobile or not (len(mobile) == 10 or len(mobile) == 12) or not mobile.startswith(('6', '7', '8', '9')):
            validation_errors.append((self.ids.mobile, "Invalid mobile number"))

        if not email or "@gmail.com" not in email:
            validation_errors.append((self.ids.email, "Invalid email address"))

        if not password or not self.is_strong_password(password):
            validation_errors.append((self.ids.password, "Please set an strong password"))

        if not password2 or password != password2:
            validation_errors.append((self.ids.password2, "Passwords do not match"))

        if not terms_checkbox.active:
            validation_errors.append((terms_checkbox, "Please accept the Terms and Conditions"))
            self.show_validation_error(terms_checkbox, "Please accept the Terms and Conditions")

        if not kyc_checkbox.active:
            validation_errors.append((kyc_checkbox, "Please authorize KYC details"))
            self.show_validation_error(kyc_checkbox, "Please authorize KYC details")

        for widget, error_text in validation_errors:
            self.show_validation_error(widget, error_text)

        if validation_errors:
            return

        self.save_to_database()

        snackbar = Snackbar(
            text="Signup Successful!",
            md_bg_color=[1, 1, 1, 1],
            text_color=[0, 0, 0, 1],
            pos_hint={'top': 1},
            duration=2
        )
        snackbar.open()

        self.manager.current = 'LoginScreen'

    def show_validation_error(self, widget, error_text):
        widget.error = True
        widget.helper_text_color = (1, 0, 0, 1)
        widget.helper_text = error_text
        widget.helper_text_mode = "on_error"
        if isinstance(widget, MDCheckbox):
            widget.theme_text_color = 'Error'

    def show_popup(self, message):
        Snackbar(text=message, md_bg_color=[1, 1, 1, 1], text_color=[0, 0, 0, 1]).open()

    def show_terms_dialog(self):
        dialog = MDDialog(
            title="Terms and Conditions",
            text="I agree with terms and conditions",
            size_hint=(0.8, 0.5),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def is_strong_password(self, password):

        return bool(
            re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=])[A-Za-z\d!@#$%^&*()-_+=]+$', password))
