from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from traffic_simulation import *
from yolo_traffic import *

main = tkinter.Tk()
main.title("Smart Control of Traffic Light Using Artificial Intelligence")
main.geometry("1000x750")
main.configure(bg='light blue')

global filename

def yoloTrafficDetection():
    global filename
    filename = filedialog.askopenfilename(initialdir="Videos", title="Select a Video File",
                                          filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
    pathlabel.config(text="File Loaded: " + filename)
    text.delete('1.0', END)
    text.insert(END, filename + " loaded\n")
    runYolo(filename)

def runSimulation():
    text.delete('1.0', END)
    text.insert(END, "Running traffic simulation...\n")
    sim = Simulation()
    sim.runSimulation()
    text.insert(END, "Simulation complete.\n")

def exit():
    main.destroy()

# Title
font = ('Helvetica', 18, 'bold')
title = Label(main, text='Smart Control of Traffic Light Using Artificial Intelligence')
title.config(bg='light blue', fg='dark blue', font=font, pady=10)
title.pack()

# Buttons frame
button_frame = Frame(main, bg='light blue')
button_frame.pack(pady=20)

font1 = ('Helvetica', 14, 'bold')

# Simulation button
simulationButton = Button(button_frame, text="Run Traffic Simulation", command=runSimulation, font=font1, bg='white', fg='dark blue')
simulationButton.grid(row=0, column=0, padx=20, pady=10)

# Yolo button
yoloButton = Button(button_frame, text="Run Yolo Traffic Detection & Counting", command=yoloTrafficDetection, font=font1, bg='white', fg='dark blue')
yoloButton.grid(row=0, column=1, padx=20, pady=10)

# Exit button
exitButton = Button(button_frame, text="Exit", command=exit, font=font1, bg='white', fg='dark blue')
exitButton.grid(row=0, column=2, padx=20, pady=10)

# Path label
pathlabel = Label(main, text="", bg='light blue', fg='dark blue', font=('Helvetica', 12, 'bold'), pady=10)
pathlabel.pack()

# Text area
text_frame = Frame(main, bg='light blue')
text_frame.pack(pady=10)

font1 = ('Helvetica', 12, 'bold')
text = Text(text_frame, height=20, width=120, font=font1, wrap='word')
text.pack(side=LEFT, fill=BOTH, expand=True)

scroll = Scrollbar(text_frame, command=text.yview)
text.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

main.mainloop()