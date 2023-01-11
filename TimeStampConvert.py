import pandas as pd
from pathlib import Path
import tkinter as tk
from tkinter import *
from tkinter import filedialog


def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("Excel Files", "*.xlsx"),("Text Files","*.txt")))
    l1 = Label(window, text = "File path: " + file_path).pack()
    
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

def close():
    window.destroy()

# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
b2 = Button(window, text = "OK", command = close).pack()
window.geometry("%dx%d" % (width, height))
window.mainloop()
print(file_path)

#Downloads Folder Path to save files
myPath = str(Path.home() / "Downloads")
#Gather File Name
print("Input File Name:")
filename = str(input())

#Reading TXT File and Converting it to an Excel File
file = pd.read_csv(filepath_or_buffer=file_path)
fullSavePath = myPath + "/" + filename + ".csv"
file.to_csv(fullSavePath)
csvFile = pd.read_csv(filepath_or_buffer=fullSavePath)
csvFile.to_excel(myPath + "/" + filename + ".txt")
