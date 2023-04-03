import tkinter
from tkinter import filedialog
from zipfile import ZipFile
import shutil
import os
import pygame
import customtkinter
import pathlib
import patoolib
from subprocess import Popen
import webbrowser


pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("Assets/Welcome.mp3")
    pygame.mixer.music.play()


play_music()


def selection_sound():
    pygame.mixer.music.load("Assets/Open.mp3")
    pygame.mixer.music.play()


def prompt_sound():
    pygame.mixer.music.load("Assets/selection.mp3")
    pygame.mixer.music.play()


def prompt_sound_1():
    pygame.mixer.music.load("Assets/completion_sound.mp3")
    pygame.mixer.music.play()


def completion_sound():
    pygame.mixer.music.load("Assets/Close.mp3")
    pygame.mixer.music.play()


def sample_play():
    pygame.mixer.music.load("Assets/Playstation 2 System Menu Ambience.mp3")
    pygame.mixer.music.play()


customtkinter.set_appearance_mode("light")  # appearance mode - light, dark
customtkinter.set_default_color_theme("blue")   # theme - blue, dark blue

app = customtkinter.CTk()   # create custom tkinter window as we do with tk window


def create_zip():
    status_label.configure(text="")
    contents = filedialog.askopenfilenames(title="Select_files")
    file_type = radiobutton()
    print(file_type)
    if file_type == ".zip":
        if contents != "":
            zip_name = filedialog.asksaveasfilename(title="Save as", defaultextension=".zip", filetypes=[("zip_files", ".zip")])
            if zip_name != "":
                file_name = os.path.basename(zip_name)
                current_zip_path = os.path.abspath(file_name)
                with ZipFile(file_name, "w") as zipObj:
                    for file in contents:
                        file_name = os.path.basename(file)
                        zipObj.write(file, file_name)
        # current_zip_path = os.path.abspath(file_name)
        # out_path = filedialog.askdirectory()
        # move_path = os.path.join(out_path, file_name)
        # shutil.move(current_zip_path, move_path)
        # if contents == "" and out_path == "":
        #     status_label.configure(text="")
        # elif contents == "" and out_path != "":
        #     print("Error")
        #     status_label.configure(text="Error")
        # elif contents != "" and out_path != "":
        #     print("Archived")
        #     status_label.configure(text="Done")
                move_path = os.path.join(zip_name)
                shutil.move(current_zip_path, move_path)
                if contents != "" and zip_name != "":
                    print("Archived")
                    status_label.configure(text="Done")
                    completion_sound()
            else:
                print("Name not specified!")
    elif file_type == ".rar":
        status_label.configure(text="")
        if contents != "":
            rar_name = filedialog.asksaveasfilename(title="Save as", defaultextension=".rar",
                                                    filetypes=[("rar_files", ".rar")])
            if rar_name != "":
                file_name = os.path.basename(rar_name)
                current_zip_path = os.path.abspath(file_name)
                patoolib.create_archive(file_name, contents)
                move_path = os.path.join(rar_name)
                shutil.move(current_zip_path, move_path)
                if contents != "" and rar_name != "":
                    print("Archived")
                    status_label.configure(text="Done")
                    completion_sound()
            else:
                print("Name not specified!")


def extract():
    folder = filedialog.askopenfilename(title="Open_file", defaultextension=".zip", filetypes=[

            ("zip_files", ".zip"), ("rar_files", ".rar"), ("All_Files", ".*")
        ])
    file_type = pathlib.Path(folder).suffix
    print(file_type)
    if file_type == ".zip":
        with ZipFile(folder, "r") as Zip:
            print("Extracting")
            out_path = filedialog.askdirectory()
            Zip.extractall(out_path)
        if folder != "" and out_path == "":
            status_label.configure(text="")
        else:
            print("Done")
            status_label.configure(text="Done")
            completion_sound()
    if file_type == ".rar":
        print("Extracting")
        out_path = filedialog.askdirectory()
        patoolib.extract_archive(folder, outdir=out_path)
        if folder != "" and out_path == "":
            status_label.configure(text="")
        else:
            print("Done")
            status_label.configure(text="Done")
            completion_sound()


def change_appearance_mode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
    if new_appearance_mode == "Light":
        selection_sound()
    elif new_appearance_mode == "Dark":
        completion_sound()
    else:
        completion_sound()


def change_scaling(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
    customtkinter.set_window_scaling(new_scaling_float)
    if new_scaling == "80%":
        app.geometry("999x415")
        completion_sound()
    elif new_scaling == "90%":
        app.geometry("950x415")
        completion_sound()
    elif new_scaling == "100%":
        app.geometry("895x415")
        selection_sound()
    elif new_scaling == "110%":
        app.geometry("859x415")
        selection_sound()
    elif new_scaling == "120%":
        app.geometry("827x415")
        selection_sound()


def sidebar_button():
    print("sidebar button click")
    webbrowser.open("https://www.youtube.com/")


def radiobutton():
    value = radio_var.get()
    return value


def clear_selection():
    radio_var.set(value="None")


def open_website():
    webbrowser.open("https://")
    print("open website button click")


def open_github():
    print("open github click")


def openJava():
    Popen("Assets/Huffman Coder/Encoder.exe")


app_frame = customtkinter.CTkFrame(master=app, width=140, corner_radius=0)
app_frame.grid(row=0, column=1, rowspan=4, sticky="NSEW")
app_frame.grid_rowconfigure(4, weight=1)

sidebar_frame = customtkinter.CTkFrame(master=app, width=80, corner_radius=0, fg_color="gray75")
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="NSEW")
sidebar_frame.grid_rowconfigure(4, weight=1)

logo_label = customtkinter.CTkLabel(master=sidebar_frame, text="Easy Solutions", font=("", 20))
logo_label.grid(row=0, column=0, padx=0, pady=(30, 10))

open_website_button = customtkinter.CTkButton(master=sidebar_frame, command=lambda: [selection_sound(), open_website()], text="Open Website")
open_website_button.grid(row=1, column=0, padx=20, pady=10)

open_github_button = customtkinter.CTkButton(master=sidebar_frame, command=lambda: [selection_sound(), open_github()], text="Open GitHub")
open_github_button.grid(row=2, column=0, padx=20, pady=10)

open_file_compressor_button = customtkinter.CTkButton(master=sidebar_frame, command=lambda: [selection_sound(), openJava()], text="Open File Compressor")
open_file_compressor_button.grid(row=3, column=0, padx=20, pady=10)

appearance_mode_label = customtkinter.CTkLabel(master=sidebar_frame, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

appearance_mode_optionmenu = customtkinter.CTkOptionMenu(master=sidebar_frame, values=["Light", "Dark", "System"],
                                                         command=change_appearance_mode)
appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))

scaling_label = customtkinter.CTkLabel(master=sidebar_frame, text="UI Scaling:", anchor="w")
scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

scaling_optionmenu = customtkinter.CTkOptionMenu(master=sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                 command=change_scaling)
scaling_optionmenu.set("100%")
scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 40))

text_var = tkinter.StringVar(value="Easy - ZR")
title = customtkinter.CTkLabel(master=app_frame, textvariable=text_var, width=120, height=25, fg_color=("white", "gray75"),
                               font=("",  50), corner_radius=8)
title.grid(row=0, column=0, ipadx=219, ipady=10, padx=20, pady=(40, 20), sticky="N")

status_label = customtkinter.CTkLabel(master=app_frame, text="", width=120, height=25, fg_color=("white", "gray75"),
                                      font=("",  20), corner_radius=8)
status_label.grid(row=4, column=0, ipadx=100, ipady=10, padx=40, pady=(50, 20))

button_frame = customtkinter.CTkFrame(master=app_frame, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
button_frame.grid(row=5, column=0, ipady=5, pady=(20, 40))

radio_var = tkinter.StringVar()
radio_button_1 = customtkinter.CTkRadioButton(master=button_frame, variable=radio_var, value=".zip", text=".zip", command=lambda: [prompt_sound(), radiobutton()])
radio_button_1.grid(row=6, column=0, pady=(20, 10), padx=50, sticky="nw")

radio_button_2 = customtkinter.CTkRadioButton(master=button_frame, variable=radio_var, value=".rar", text=".rar", command=lambda: [prompt_sound(), radiobutton()])
radio_button_2.grid(row=6, column=0, pady=(20, 10), sticky="ne")

radio_button_3 = customtkinter.CTkRadioButton(master=button_frame, variable=radio_var, value=None, text="reset", command=lambda: [prompt_sound_1(), clear_selection()])
radio_button_3.grid(row=6, column=2, pady=(20, 10), sticky="ne")

exit_button = customtkinter.CTkButton(master=button_frame, text="Exit", command=app.quit)
exit_button.grid(column=2, row=0, padx=35, pady=(20, 0))

archive_button = customtkinter.CTkButton(master=button_frame, text="Archive", command=lambda: [selection_sound(), create_zip()])
archive_button.grid(column=0, row=0, padx=35, pady=(20, 0))

extract_button = customtkinter.CTkButton(master=button_frame, text="Extract", command=lambda: [selection_sound(), extract()])
extract_button.grid(column=1, row=0, padx=35, pady=(20, 0))

app.geometry("895x415")
app.title("Easy - ZR")
app.resizable(False, False)
app.mainloop()
