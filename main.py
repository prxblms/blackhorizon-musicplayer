import customtkinter
# import tkinter as tk
# from tkinter import *
# from pygame import mixer
# from vars import * # var.py
from func import * # func.py

# Frame do menu de controle do player de música
class PlayerMenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, music_list):
        super().__init__(master, fg_color = grey_color)

        # Add Folder, Playlist
        self.pause_button = customtkinter.CTkButton(self, text = "Add Folder", font = default_font, fg_color = purple_color, hover_color = dark_purple_color, width = 100, command = lambda:add_folder(music_list))
        self.pause_button.grid(row = 0, column = 0, padx = (6, 0), pady = 6)
        
        # Play
        self.play_button = customtkinter.CTkButton(self, text = "Play", font = default_font, fg_color = purple_color, hover_color = dark_purple_color, width = 100, command = lambda:play_music(music_list))
        self.play_button.grid(row = 0, column = 1, padx = (6, 0), pady = 6)

        # Pause
        self.pause_button = customtkinter.CTkButton(self, text = "Pause", font = default_font, fg_color = "#6800FF", hover_color = "#33007C", width = 100, command = pause_music)
        self.pause_button.grid(row = 0, column = 2, padx = (6, 0), pady = 6)
        
        # Unpause
        self.unpause_button = customtkinter.CTkButton(self, text = "Unpause", font = default_font, fg_color = purple_color, hover_color = dark_purple_color, width = 100, command = unpause_music)
        self.unpause_button.grid(row = 0, column = 3, padx = (6, 6), pady = 6)

        # Remove Folder, Playlist
        self.unpause_button = customtkinter.CTkButton(self, text = "Remove All", font = default_font, fg_color = purple_color, hover_color = dark_purple_color, width = 100, command = lambda:remove_all(music_list))
        self.unpause_button.grid(row = 0, column = 4, padx = (6, 6), pady = 6)

# Frame do titulo do app
class TitleFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color = purple_color)

        self.title_label = customtkinter.CTkLabel(self, text = "BlackHorizon™ Music Player", font = title_font)
        self.title_label.grid(row = 0, column = 0, padx = 10, pady = 2)

# Classe principal do app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(" ")
        self.geometry("600x300")
        self.resizable(False, False)
        self.configure(fg_color = dark_gray_color)
        self.grid_columnconfigure(0, weight = 1)
        #self.grid_rowconfigure(0, weight=0)

        self.title_frame = TitleFrame(self)
        self.title_frame.grid(row = 0, column = 0, padx = 10, pady = (10))

        self.music_list = tk.Listbox(self, width = 90, height = 10, selectmode = tk.SINGLE)
        self.music_list.grid(row=1, column = 0)

        self.volume_slider = customtkinter.CTkSlider(self, from_= 0 , to = 100, height = 100, orientation = "vertical", command = set_volume)
        self.volume_slider.set(50)
        self.volume_slider.grid(row = 1, column = 1, sticky = "ns")

        self.scrollbar = customtkinter.CTkScrollbar(self, width = 12, height = 10)
        self.scrollbar.grid(row = 1, column = 2, sticky = "ns")
        
        self.music_list.configure(yscrollcommand=self.scrollbar.set)

        self.player_menu_frame = PlayerMenuFrame(self, self.music_list)
        self.player_menu_frame.grid(row = 2, column = 0, padx = 8, pady = 8)

        # Inicia o pygame para tocar as musicas
        mixer.init()

if __name__ == "__main__":
    app = App()
    app.mainloop()