# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:33:30 2022

@author: 11nho
"""

#%%imports and setup for initial data
import sys
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pds
from tqdm import tqdm as tq
from pathlib import Path
#%%Create Button Function for data input
def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("Excel Files", "*.xlsx"),))
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
#%%Read Excel File
ds = pds.read_excel(io = file_path, usecols = "A,D", skiprows = 1, keep_default_na = False)
#%%usv incident beggining times in seconds
usvTimes = ds["Begin Time (s)"].tolist()
#beginning times for tones in seconds
toneStart = ds["Tone Time Markers"].tolist()
toneStart2 = ds["Tone Time Markers"].tolist()
#%%creates empty lists to be used by loops later
graphStart = []
graphEnd = []
#%%creates the first parameter of the x value for each graph
print("Calculating GraphStart")
for num in tq(toneStart):
    try:
        int(float(num))
    except:
        pass
    else:
        graphStart.append(num - 10)
print("Complete")
#%%creates the second parameter of the x value for each graph
print("Calculating GraphEnd")
for num in tq(toneStart2):
    try:
        int(float(num))
    except:
        pass
    else:
        graphEnd.append(num + 10)
print("Complete")
#%%Makes usvTimes usable
print("Calculating USVTimeStamps")
for num in tq(usvTimes):
    try:
        int(float(num))
    except:
        pass
print("Complete")
#%%pair beggining and end parameter into a full list 
graphpair = zip(graphStart,graphEnd)

#%%Zip x and y coordinates together
graphx = list(graphpair)
#%%%create graphs
print("Input File Name:")
filename = str(input())
print("Creating Graphs")
myPath = str(Path.home() / "Downloads")
print(myPath)

lists = []
for index, num in tq(enumerate(graphx)):
    x,y = num
    leftbound = (x - x) - 30
    rightbound = y - x
    za = x - 20
    zb = x + 20
    sublist = []
    for i in usvTimes:
        try:
            i + 0
        except:
            pass
        else:
            if i == 0:
                continue
            elif za <= i <= zb:
                sublist.append(i-x)
    lists.append(sublist)
data = lists
print("Input Y Height Limit:")
ymax = int(input())
plt.eventplot(data , colors='black' , lineoffsets=1 , linelengths=1)
plt.xlim(-20,20)
plt.ylim(0,ymax)
plt.autoscale(False)
print("Input Y Label:")
ylabel = str(input())
plt.ylabel(ylabel)
plt.xlabel("Time of USV Incidence Normalized to Tone Onset")
plt.title(filename)
plt.savefig(myPath + "/Eventplot" + filename + ".pdf")
plt.show()
print("Graphs Complete")







    
