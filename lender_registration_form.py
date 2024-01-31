from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
import sqlite3
from kivy import platform
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3
from kivymd.uix.pickers import MDDatePicker


KV = '''
<LenderScreen>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_to_dashboard()]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title



    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)


        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)


        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)
            MDTextField:
                id: username
                hint_text: 'Enter full name'
                multiline: False
                helper_text: 'Enter valid name'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                font_name: "Roboto-Bold"


            Spinner:
                id: spinner_id
                text: "Select Gender"
                values: ["Select Gender", "Male", "Female", "Other"]
                multiline:False
                size_hint_y: (None)
                size_hint: 1, None
                height: "40dp"
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDTextField:
                id: date_textfield
                hint_text: "Select Date Of Birth"
                icon_right: "calendar"
                readonly: True
                on_focus: root.show_date_picker()
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1



            MDRectangleFlatButton:
                text: 'Next'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: root.add_data(username.text, spinner_id.text, date_textfield.text)


<LenderScreen1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'lender_registration_form')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20sp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: mobile_number
                hint_text: 'Enter mobile number'
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0,0,0, 1
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()

            MDTextField:
                id: altername_email
                hint_text: 'Enter your alternate email'
                multiline: False
                helper_text: 'Enter your valid email_id'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()

            Spinner:
                id: spinner_id
                text: "Please Select your References"
                values: ["Select your References" ,"Google", "Facebook", "Ads","Electronic media","Others"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            GridLayout:
                cols: 1
                spacing:dp(30)



                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(mobile_number.text, altername_email.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20sp"
                font_name: "Roboto-Bold"               

            MDTextField:
                id: aadhar_number
                hint_text: 'Enter Government ID1 '
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                hint_text_color: 0, 0, 0, 1


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload_icon1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_1()
                
                MDLabel:
                    id: upload_label1
                    text: 'Upload Govt ID1'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            MDTextField:
                id: pan_number
                hint_text: 'Enter Government ID2 '
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height: self.minimum_height
                hint_text_color: 0, 0, 0, 1

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    id: upload_icon2
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.file_manager_open_2()
    
                MDLabel:
                    id: upload_label2
                    text: 'Upload Govt ID2'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(aadhar_number.text, pan_number.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"               

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True

            Spinner:
                id: spinner_id
                text: "Please Select Education Details"
                values: ["Select Education Details", "10th class", "Intermediate", "Bachelors", "Masters", "PHD"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_press: root.next_pressed(spinner_id.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

            MDLabel:
                text: ""

<LenderScreen_Edu_10th>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Education Details'

                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: "Upload 10th class certificate"

                halign: 'center'
                bold:True
                size_hint_y: None
                height:dp(50)


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
    
                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()
    
                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
            GridLayout:
                cols: 1
                spacing:dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_Intermediate>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}


            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_Bachelors>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title"

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "Upload 10th class Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload B.tech/B.E certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_Masters>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}


            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload B.tech/B.E Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreen_Edu_PHD>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}


            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th Class Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Btech/B.E Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload PHD Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload_5()

                MDLabel:
                    id: upload_label5
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: app.root.current = 'LenderScreen4'
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreen4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_name: "Roboto-Bold"
                font_size: "20dp"
            MDLabel:
                text: 'Address'
                halign: 'center'
                bold: True
            MDTextField:
                id: country
                hint_text: 'Enter Country Name'
                multiline: False
                helper_text_mode: 'on_focus'
            MDTextField:
                id: state
                hint_text: 'Enter State Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None
            MDTextField:
                id: city
                hint_text: 'Enter City Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  

            MDTextField:
                id: zip_code
                hint_text: 'Enter postal/zipcode '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()
            MDTextField:
                id: street_address
                hint_text: 'Enter Street Name'
                multiline: False
                helper_text: 'Enter valid address'
                helper_text_mode: 'on_focus'

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]


                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(street_address.text, city.text, zip_code.text, state.text, country.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreen5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen4')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                font_size: "20dp"
                halign: 'center'
                font_name: "Roboto-Bold"

            Spinner:
                id: spinner_id
                text: "Select Loan Type"
                values: ["Select Loan Type", "Individual", "Institutional"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: investment
                hint_text: 'Enter investment Amount '
                multiline: False
                helper_text: 'Enter above 100000'
                helper_text_mode: 'on_focus'
                input_type: 'number'  
                on_touch_down: root.on_investment_touch_down()


            Spinner:
                id: spinner2
                text: "Select Lending Period"
                values: ["Select Lending Period","1-year", "1-2 years", "2-3 years", "3-4 years", "5-years Above"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_press: root.next_pressed(spinner_id.text, investment.text, spinner2.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreenInstitutionalForm1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Institutional Type'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)


            MDLabel:
                text: 'Step-1'
                halign: 'center'
                bold: True

            MDTextField:
                id: business_name
                hint_text: 'Enter business name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: business_location
                hint_text: 'Enter business location'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id:  business_address
                hint_text: 'Enter business full address'
                multiline: False

                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id:branch_name
                hint_text: 'Enter branch name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(business_name.text,business_location.text,business_address.text,branch_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm2>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Step-2'
                halign: 'center'
                bold: True

            Spinner:
                id: spin
                text: "Please Select Business Type"
                values: ["Select Business Type","Partnership", "Cooperation", "Cooperative", "Solo Proprietorship", "Cash", "Cheque", "Online Transaction", "Limited Liability Company"]
                multiline:False
                background_color: (0,0,0,0)
                size_hint_y: None
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDTextField:
                id: nearest_location
                hint_text: 'Enter nearest location '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None


            Spinner:
                id: spinner_id
                text: "Select No.Of Employees Working"
                values: ["Select No.Of Employees Working", "1-10", "10-50", "50-100", "100-200", "200-500", "500-100", "1000+"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDTextField:
                id:year_of_estd
                hint_text: 'Enter year of estd'
                multiline: False                        
                helper_text_mode: 'on_focus'

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spin.text,nearest_location.text,spinner_id.text,year_of_estd.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


<LenderScreenInstitutionalForm3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Step-3'
                halign: 'center'
                bold: True

            Spinner:
                id: spinner_id
                text: "Select Industry Type"
                values: ["Select Industry Type","Public", "Government"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDTextField:
                id: last_six_months_turnover
                hint_text: 'Enter last 6 months turnover'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_last_six_months_turnover_touch_down()

            MDLabel:
                text: "Last 6 months bank statements"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
    
                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload1()
    
                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spinner_id.text,last_six_months_turnover.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Step-4'
                halign: 'center'
                bold: True

            MDTextField:
                id: director_name
                hint_text: 'Enter director name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: director_mobile_number
                hint_text: 'Enter director mobile number'
                multiline: False                   
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_director_mobile_number_touch_down()

            MDTextField:
                id:  din
                hint_text: 'Enter DIN'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id:cin
                hint_text: 'Enter CIN'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(director_name.text,director_mobile_number.text,din.text,cin.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenInstitutionalForm5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm4')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Step-5'
                halign: 'center'
                bold: True

            MDTextField:
                id: reg_office_address
                hint_text: 'Enter registered office address '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDLabel:
                text: "Proof of verification"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
    
                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload1()
    
                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id:branch_name
                hint_text: 'Enter branch name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(reg_office_address.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


<LenderScreenIndividualForm1>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ""
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Individual Type'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True   
                size_hint_y: None

            Spinner:
                id: spinner1
                text: "Please Select Employment Type"
                values: ["Employment Type","Full-Time", "Part-Time","Contract","Freelance","Intern"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDTextField:              
                id:company_name
                hint_text: 'Enter company name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner2
                text: "Please Select Organisation Type"
                values: ["Select Organisation Type","Cooperation","Partnership","Sole proprietorship","Hierarchical Organization"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spinner1.text, company_name.text, spinner2.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
<LenderScreenIndividualForm2>:
    name: 'len_reg_individual_form2'
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDTextField:              
                id:company_address
                hint_text: 'Enter company address'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:company_pin_code
                hint_text: 'Enter Company Pincode'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_company_pin_code_touch_down()

            MDTextField:              
                id:company_country
                hint_text: 'Enter Company Country'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:landmark
                hint_text: 'Enter landmark'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:business_phone_number
                hint_text: 'Enter business phone number'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_business_phone_number_touch_down()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(company_address.text, company_pin_code.text, company_country.text, landmark.text, business_phone_number.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenIndividualForm3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                font_name: "Roboto-Bold"
                font_size: "20dp"   
            MDTextField:              
                id:annual_salary
                hint_text: 'Enter annual salary'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_annual_salary_touch_down()

            MDTextField:              
                id:designation
                hint_text: 'Enter designation'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDLabel:
                text: "Upload Employee ID"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        
        
                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload1()
        
                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
            MDLabel:
                text: "Upload last 6 months bank statements"
                halign: 'center'
                bold: True
        
        
            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        
        
                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: root.upload2()
        
                MDLabel:
                    id: upload_label2
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(annual_salary.text, designation.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"        


<LenderScreenIndividualBankForm1>:

    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: account_holder_name
                hint_text: 'Enter account holder name '
                multiline: False
                helper_text: 'Enter valid account holder name'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner_id
                text: "Please Select Account Type"
                values: ["Select Account Type","Savings", "Current", "NRI","Joint Account","Salary"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDTextField:
                id: account_number
                hint_text: 'Enter account number '
                multiline: False
                helper_text: 'Enter valid account number'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: bank_name
                hint_text: 'Enter bank name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(account_holder_name.text, spinner_id.text, account_number.text, bank_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 

<LenderScreenIndividualBankForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualBankForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDTextField:
                id: ifsc_code
                hint_text: 'Enter Bank ID '
                multiline: False
                helper_text: 'Enter valid ifsc code'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: branch_name
                hint_text: 'Enter branch name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]



                MDRaisedButton:
                    text: "Submit"
                    on_release: root.go_to_lender_dashboard(ifsc_code.text, branch_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 



<LenderScreenInstitutionalBankForm1>:
    name: 'len_reg_institutional_bank_form1'
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDTextField:
                id: account_holder_name
                hint_text: 'Enter account holder name '
                multiline: False
                helper_text: 'Enter valid account holder name'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner_id
                text: "Please Select Account Type"
                values: ["Select Account Type", "Current","Escrow Account","Payroll Account"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



            MDTextField:
                id: account_number
                hint_text: 'Enter account number '
                multiline: False
                helper_text: 'Enter valid account number'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: bank_name
                hint_text: 'Enter bank name '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(account_holder_name.text, spinner_id.text, account_number.text, bank_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"   

<LenderScreenInstitutionalBankForm2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalBankForm1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title


    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: ifsc_code
                hint_text: 'Enter Bank ID '
                multiline: False
                helper_text: 'Enter valid ifsc code'
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: branch_name
                hint_text: 'Enter branch name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]


                MDRaisedButton:
                    text: "Submit"
                    on_release: root.go_to_lender_dashboard(ifsc_code.text, branch_name.text)
                    md_bg_color: 0.031, 0.463, 0.91, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"


'''

conn = sqlite3.connect("fin_user_profile.db")
cursor = conn.cursor()

class LenderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = MDDatePicker()
        self.date_picker.bind(on_save=self.on_date_selected)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        a = 0
        row_id_list = []
        status = []
        name_list = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            name_list.append(row[1])
        log_index = status.index('logged')
        self.ids.username.text = name_list[log_index]

    def show_date_picker(self):
        self.date_picker.open()
    def on_date_selected(self, instance, the_date,a):
        print(f"Selected date: {the_date, the_date.year}")
        self.ids.date_textfield.text = f'{the_date.year}-{the_date.month}-{the_date.day}'

    def add_data(self, name, gender,date):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        b = 'lender'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')


        cursor.execute("UPDATE fin_registration_table SET name = ?, gender = ?, date_of_birth = ?, user_type = ? WHERE customer_id = ?",
                       (name, gender, date,b, row_id_list[log_index]))
        conn.commit()

        self.manager.current = 'LenderScreen1'

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderLanding'  # Replace with the actual name of your previous screen

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'


class LenderScreen1(Screen):
    def add_data(self, mobile_number, alternate_email):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET mobile_number = ?, alternate_email = ? WHERE customer_id = ?",
                       (mobile_number, alternate_email, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreen2'
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen'


class LenderScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()
    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()


    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET pan_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()


    def add_data(self, aadhar_number, pan_number):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_number = ?, pan_number = ? WHERE customer_id = ?", (aadhar_number, pan_number, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreen3'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen1'


class LenderScreen3(Screen):

    def next_pressed(self, id):
        if id == '10th class':
            LenderScreen_Edu_10th()
            self.manager.current = 'LenderScreen_Edu_10th'

        elif id == 'Intermediate':
            LenderScreen_Edu_Intermediate()
            self.manager.current = 'LenderScreen_Edu_Intermediate'

        elif id == 'Bachelors':
            self.manager.current = 'LenderScreen_Edu_Bachelors'
        elif id == 'Masters':
            self.manager.current = 'LenderScreen_Edu_Masters'
        elif id == 'PHD':
            self.manager.current = 'LenderScreen_Edu_PHD'
        print(id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET highest_qualification = ? WHERE customer_id = ?",
                       (id, row_id_list[log_index]))
        conn.commit()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen2'


class LenderScreen_Edu_10th(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_Intermediate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_Bachelors(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.manager_open_3 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )
        self.file_manager_3 = MDFileManager(
            exit_manager=self.exit_manager_3,
            select_path=self.select_path_3
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()


    def file_manager_open_3(self):
        self.file_manager_3.show('/')
        self.manager_open_3 = True

    def select_path_3(self, path):
        print(f"Selected path 3: {path}")
        self.update_data_with_file_3(path)
        self.exit_manager_3()

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label3.text = 'Upload Successfully'

    def exit_manager_3(self, *args):
        self.manager_open_3 = False
        self.file_manager_3.close()

    def upload_3(self):
        if not self.manager_open_3:
            self.file_manager_open_3()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_Masters(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.manager_open_3 = False
        self.manager_open_4 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )
        self.file_manager_3 = MDFileManager(
            exit_manager=self.exit_manager_3,
            select_path=self.select_path_3
        )
        self.file_manager_4 = MDFileManager(
            exit_manager=self.exit_manager_4,
            select_path=self.select_path_4
        )
    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def file_manager_open_3(self):
        self.file_manager_3.show('/')
        self.manager_open_3 = True

    def select_path_3(self, path):
        print(f"Selected path 3: {path}")
        self.update_data_with_file_3(path)
        self.exit_manager_3()

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label3.text = 'Upload Successfully'

    def exit_manager_3(self, *args):
        self.manager_open_3 = False
        self.file_manager_3.close()

    def upload_3(self):
        if not self.manager_open_3:
            self.file_manager_open_3()

    def file_manager_open_4(self):
        self.file_manager_4.show('/')
        self.manager_open_4 = True

    def select_path_4(self, path):
        print(f"Selected path 4: {path}")
        self.update_data_with_file_4(path)
        self.exit_manager_4()

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label4.text = 'Upload Successfully'
    def exit_manager_4(self, *args):
        self.manager_open_4 = False
        self.file_manager_4.close()

    def upload_4(self):
        if not self.manager_open_4:
            self.file_manager_open_4()

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen_Edu_PHD(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.manager_open_3 = False
        self.manager_open_4 = False
        self.manager_open_5 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )
        self.file_manager_3 = MDFileManager(
            exit_manager=self.exit_manager_3,
            select_path=self.select_path_3
        )
        self.file_manager_4 = MDFileManager(
            exit_manager=self.exit_manager_4,
            select_path=self.select_path_4
        )
        self.file_manager_5 = MDFileManager(
            exit_manager=self.exit_manager_5,
            select_path=self.select_path_5
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload_1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload_2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()

    def file_manager_open_3(self):
        self.file_manager_3.show('/')
        self.manager_open_3 = True

    def select_path_3(self, path):
        print(f"Selected path 3: {path}")
        self.update_data_with_file_3(path)
        self.exit_manager_3()

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label3.text = 'Upload Successfully'

    def exit_manager_3(self, *args):
        self.manager_open_3 = False
        self.file_manager_3.close()

    def upload_3(self):
        if not self.manager_open_3:
            self.file_manager_open_3()

    def file_manager_open_4(self):
        self.file_manager_4.show('/')
        self.manager_open_4 = True

    def select_path_4(self, path):
        print(f"Selected path 4: {path}")
        self.update_data_with_file_4(path)
        self.exit_manager_4()

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label4.text = 'Upload Successfully'

    def exit_manager_4(self, *args):
        self.manager_open_4 = False
        self.file_manager_4.close()

    def upload_4(self):
        if not self.manager_open_4:
            self.file_manager_open_4()
    def file_manager_open_5(self):
        self.file_manager_5.show('/')
        self.manager_open_5 = True

    def select_path_5(self, path):
        print(f"Selected path 5: {path}")
        self.update_data_with_file_5(path)
        self.exit_manager_5()

    def update_data_with_file_5(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET phd_certificate = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label5.text = 'Upload Successfully'
    def exit_manager_5(self, *args):
        self.manager_open_5 = False
        self.file_manager_5.close()

    def upload_5(self):
        if not self.manager_open_5:
            self.file_manager_open_5()
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen4(Screen):
    def add_data(self, street, city, zip_code, state, country):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET street_name = ?, city_name = ?, zip_code = ?, state_name = ?, country_name = ? WHERE customer_id = ?",
                       (street, city, zip_code,state, country, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreen5'
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.zip_code.input_type = 'number'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'


class LenderScreen5(Screen):
    def next_pressed(self, id, investment, period):
        if id == 'Individual':
            self.manager.current = 'LenderScreenIndividualForm1'

        elif id == 'Institutional':
            self.manager.current = 'LenderScreenInstitutionalForm1'
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET loan_type = ?, investment = ?, lending_period = ? WHERE customer_id = ?",
            (id, investment, period, row_id_list[log_index]))
        conn.commit()
    def on_investment_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.investment.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen4'


class LenderScreenInstitutionalForm1(Screen):
    def add_data(self, business_name, business_location, business_address, business_branch_name):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET business_name = ?, business_location = ?, business_address = ?, business_branch_name = ? WHERE customer_id = ?",
            (business_name, business_location, business_address,business_branch_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenInstitutionalForm2'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'


class LenderScreenInstitutionalForm2(Screen):
    def add_data(self, business_type, nearest_location, no_of_employees_working, year_of_estd):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET business_type = ?, nearest_location = ?, no_of_employees_working = ?, year_of_estd = ? WHERE customer_id = ?",
            (business_type, nearest_location, no_of_employees_working, year_of_estd, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenInstitutionalForm3'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm1'


class LenderScreenInstitutionalForm3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, industry_type, last_six_months_turnover):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET industry_type = ?, last_six_months_turnover = ? WHERE customer_id = ?",
            (industry_type, last_six_months_turnover, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenInstitutionalForm4'
    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm2'


class LenderScreenInstitutionalForm4(Screen):
    def add_data(self, director_name, director_mobile_number, DIN, CIN):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET director_name = ?, director_mobile_number = ?, DIN = ?, CIN = ? WHERE customer_id = ?",
            (director_name, director_mobile_number, DIN, CIN, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenInstitutionalForm5'

    def on_director_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.director_mobile_number.input_type = 'number'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm3'


class LenderScreenInstitutionalForm5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET proof_of_verification_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    def add_data(self, registered_office_address):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET registered_office_address = ? WHERE customer_id = ?",
            (registered_office_address, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenInstitutionalBankForm1'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm4'


class LenderScreenIndividualForm1(Screen):
    def add_data(self, employeent_type, company_name, organization):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET employment_type = ?, company_name = ?, organization_type = ? WHERE customer_id = ?",
            (employeent_type, company_name, organization, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenIndividualForm2'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'


class LenderScreenIndividualForm2(Screen):
    def add_data(self, company_address, company_pincode, company_country, landmark, business_number):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET company_address = ?, company_pincode = ?, company_country = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
            (company_address, company_pincode, company_country, landmark, business_number, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenIndividualForm3'
    def on_company_pin_code_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.company_pin_code.input_type = 'number'
    def on_business_phone_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.business_phone_number.input_type = 'number'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualForm1'


class LenderScreenIndividualForm3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open_1 = False
        self.manager_open_2 = False
        self.file_manager_1 = MDFileManager(
            exit_manager=self.exit_manager_1,
            select_path=self.select_path_1
        )
        self.file_manager_2 = MDFileManager(
            exit_manager=self.exit_manager_2,
            select_path=self.select_path_2
        )

    # Other existing methods here...

    def file_manager_open_1(self):
        self.file_manager_1.show('/')
        self.manager_open_1 = True

    def select_path_1(self, path):
        print(f"Selected path 1: {path}")
        self.update_data_with_file_1(path)
        self.exit_manager_1()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def exit_manager_1(self, *args):
        self.manager_open_1 = False
        self.file_manager_1.close()

    def upload1(self):
        if not self.manager_open_1:
            self.file_manager_open_1()

    # Repeat similar methods for file manager 2...

    def file_manager_open_2(self):
        self.file_manager_2.show('/')
        self.manager_open_2 = True

    def select_path_2(self, path):
        print(f"Selected path 2: {path}")
        self.update_data_with_file_2(path)
        self.exit_manager_2()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?", (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def exit_manager_2(self, *args):
        self.manager_open_2 = False
        self.file_manager_2.close()

    def upload2(self):
        if not self.manager_open_2:
            self.file_manager_open_2()


    def add_data(self, annual_salary, designation):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
            (annual_salary, designation, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenIndividualBankForm1'
    def on_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.annual_salary.input_type = 'number'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualForm2'


class LenderScreenIndividualBankForm1(Screen):
    def add_data(self, account_holder_name, account_type, account_number, bank_name):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ? WHERE customer_id = ?",
            (account_holder_name, account_type, account_number, bank_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenIndividualBankForm2'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualForm3'


class LenderScreenIndividualBankForm2(Screen):
    def go_to_lender_dashboard(self, bank_id, branch_name):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bank_id = ?, branch_name = ? WHERE customer_id = ?",
            (bank_id, branch_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'lender_dashboard'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenIndividualBankForm1'


class LenderScreenInstitutionalBankForm1(Screen):
    def add_data(self, account_holder_name, account_type, account_number, bank_name):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute(
            "UPDATE fin_registration_table SET account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ? WHERE customer_id = ?",
            (account_holder_name, account_type, account_number, bank_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'LenderScreenInstitutionalBankForm2'
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalForm5'


class LenderScreenInstitutionalBankForm2(Screen):
    def go_to_lender_dashboard(self, bank_id, branch_name):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET bank_id = ?, branch_name = ? WHERE customer_id = ?",
                       (bank_id, branch_name, row_id_list[log_index]))
        conn.commit()
        self.manager.current = 'lender_dashboard'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreenInstitutionalBankForm1'

    def go_to_dashboard(self):
        self.manager.current = 'dashboard'


class MyScreenManager(ScreenManager):
    pass