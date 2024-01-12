import os
from pygame import mixer
from tkinter import filedialog
import tkinter as tk
from vars import *

# Play, função para tocar musica.
def play_music(music_list):
    selected_music_file = music_list.curselection()
    if selected_music_file:
        selected_music = music_playlist[selected_music_file[0]]
        mixer.music.load(selected_music)
        mixer.music.play()

# Puase, função para pausar musica.
def pause_music():
    mixer.music.pause()

# Unpause, função para despausar musica.
def unpause_music():
    mixer.music.unpause()

# Add Music, Função para adicionar musica.
def add_music(music_list):
    music_file = filedialog.askopenfilename(defaultextension = ".mp3", filetypes = [("MP3 files", "*.mp3")])
    if music_file:
        music_list.insert(tk.END, os.path.basename(music_file))
        music_playlist.append(music_file)

# Add Folder, função para adicionar pasta com musicas.
def add_folder(music_list):
    try:
        music_folder = filedialog.askdirectory(title = "Selecione a pasta onde ficam suas músicas.")
        all_mp3_files = os.listdir(music_folder)

        for mp3_file in all_mp3_files:
            if mp3_file.lower().endswith(".mp3"):
                if os.path.join(music_folder, mp3_file) in music_playlist:
                    print("erro") # ainda vou criar um codigo para emitir uma mensagem.
                    return
                else:
                    music_list.insert(tk.END, os.path.basename(mp3_file))
                    music_playlist.append(os.path.join(music_folder, mp3_file))

    except:
        print("Não foi selecionada nenhuma pasta.")

# Remove All, Playlista.
def remove_all(music_list):
    music_playlist.clear() # limpa apenas a lista.
    music_list.delete(0, tk.END) # limpa o listbox.
    mixer.music.stop()
    print("a lista foi zerada.")

# Volume, função do volume.
def set_volume(music_vol):
    volume = int(music_vol) / 100
    mixer.music.set_volume(volume)