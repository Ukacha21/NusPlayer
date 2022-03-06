from tkinter import *
from tkinter import filedialog as fdialog
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton, MDFloatingRootButton, MDRoundFlatIconButton
from pygame import mixer
import os
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

class Main(MDApp):

    mixer.init()

    win = Tk()
    win.overrideredirect(1)
    win.geometry("1x1")

    files = []

    total = 0

    def addFiles(self, *args):
        
        getfile = fdialog.askopenfilenames(initialdir="%Music%", title="Please select the files you want to add",
        filetypes = [("mp3 files", "*.mp3"), ("all files", "*.*")]
        )



        self.files.append(getfile)

        #mixer.music.load(getfile)
        #mixer.music.play()
        
        #print(self.files)
        for i in self.files[0]:
            basename = os.path.basename(i)
            #print(basename)
            self.total += 1
            print(self.total, basename)
            mixer.music.load(self.files[0][0])
            mixer.music.play()
            basename = os.path.basename(self.files[0][0])
            musicLabel.text = basename

    item = 0
    nextout = "no"

    def nextMusic(self, *args):
        if self.item >= 0:
            self.item += 1
            #print(self.item)
            if self.item < self.total:
                mixer.music.load(self.files[0][self.item])
                mixer.music.play()
                basename = os.path.basename(self.files[0][self.item])
                musicLabel.text = basename
                print("total: ", self.total, "\n", "current: ", self.item)
            if self.item == (self.total-1):
                root.remove_widget(nextButton)
                self.nextout = "yes"
                print("You've reached the end of the list")
                
            else:
                pass
        else:
            pass

    def prevMusic(self, *args):
        if self.item == 0:
            print("you re on the first track")
        elif  self.item != 0:
            self.item -= 1
            mixer.music.load(self.files[0][self.item])
            mixer.music.play()
            basename = os.path.basename(self.files[0][self.item])
            musicLabel.text = basename
            if self.nextout == "yes":
                self.nextout = "no"
                root.add_widget(nextButton)

    theme = "Dark"

    def flip_theme(self, *args):
        if self.theme == "Dark":
            self.theme = "Light"
            self.theme_cls.theme_style = self.theme
        elif self.theme == "Light":
            self.theme = "Dark"
            self.theme_cls.theme_style = self.theme
        

    def build(self):

        global root
        root = MDScreen()

         # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 
        # 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 
        #'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        self.theme_cls.theme_style = self.theme
        self.theme_cls.primary_palette = "BlueGray"

        
        #icon = "invert-colors",
        #icon = "invert-colors",
        themeFlipButton = MDIconButton(
            icon = "invert-colors",
            pos_hint = {"center_x": .2, "center_y": .9},
            on_press = self.flip_theme
            )

        global musicLabel
        musicLabel = MDLabel(
            text="Plase start by selecting a track to play",
            pos_hint = {"center_x": .5, "center_y": .3},
            halign = "center",
            )

        def pause(self, *args):
            mixer.music.pause()
            root.remove_widget(pauseButton)
            root.add_widget(playButton)
    
        def unpause(self, *args):
            mixer.music.unpause()
            root.remove_widget(playButton)
            root.add_widget(pauseButton)

        addMusicButton = MDIconButton(
            icon = "file-plus-outline",
            pos_hint = {"center_x": .1, "center_y": .9},
            
            on_press = self.addFiles
            )

        pauseButton = MDFloatingRootButton(
            text= "pause",
            icon= "pause",
            pos_hint = {"center_x": .5, "center_y": .1 },
            font_size = 15,
            on_press = pause
            )

        playButton = MDFloatingRootButton(
            text= "play",
            icon= "play",
            pos_hint = {"center_x": .5, "center_y": .1 },
            font_size = 15,
            on_press = unpause
            )

        global nextButton
        nextButton = MDIconButton(
            icon= "skip-next-outline",
            pos_hint = {"center_x": .6, "center_y": .1 },
            on_press = self.nextMusic
            )

        prevButton = MDIconButton(
            text= "pause",
            icon= "skip-previous-outline",
            pos_hint = {"center_x": .4, "center_y": .1 },
            on_press = self.prevMusic
            )

        mainImage = Image(
            source="backpic.png"
        )

        root.add_widget(mainImage)
        root.add_widget(addMusicButton)
        root.add_widget(pauseButton)
        root.add_widget(nextButton)
        root.add_widget(prevButton)
        root.add_widget(musicLabel)
        root.add_widget(themeFlipButton)


        return root

Main().run()