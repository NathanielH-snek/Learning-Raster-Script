# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:49:28 2022

@author: 11nho
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:33:30 2022

@author: 11nho
"""

#%%imports and setup for initial data
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pds

#%%Create Button Function for data input
def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("Excel Files", "*.xlsx"),))
    l1 = Label(window, text = "File path: " + file_path).pack()

window = Tk()
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
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
for num in toneStart:
    try:
        int(float(num))
    except:
        pass
    else:
        graphStart.append(num - 30)
print("Complete")

#%%creates the second parameter of the x value for each graph
print("calculating GraphEnd")
for num in toneStart2:
    try:
        int(float(num))
    except:
        pass
    else:
        graphEnd.append(num + 30)
print("Complete")
#%%Makes usvTimes usable
print("Calculating USVTimeStamps")
for num in usvTimes:
    try:
        int(float(num))
    except:
        pass
print("Complete")
#%%pair beggining and end parameter into a full list 
graphpair = zip(graphStart,graphEnd)

#%%check to make sure zip worked
graphx = list(graphpair)
print(graphx)




#%%create graphs
print("Creating Graphs")
for index, num in enumerate(graphx):
    x,y = num
    leftbound = x
    rightbound = y
    
    a = []
    for x in usvTimes:
        try:
            x + 0
        except:
            pass
        else:
            if leftbound <= x <= rightbound:
                a.append(x)
    plt.figure()
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.hlines(1, leftbound, rightbound)
    plt.eventplot(a, orientation='horizontal', colors='b')
else:
    pass

plt.show()
print("Graphs Complete")







    
