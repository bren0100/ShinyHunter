import tkinter as tk
import tkinter.ttk as ttk
import pyautogui as kcmd
import threading as th



#Constants
GBA_FPS = 59.7275
GBA_FRAMERATE = 1000 / GBA_FPS

#global vars
targetTime = 0

#This gets called when the user presses the start button
def TimedCodeExecution(event):
    targetTime = CalculateTargetTime()
    print(targetTime)

    #Create the threads for the commmands and set the timers
    PreTimerThread = th.Timer(preTimer.get(), RestartCommand)
    EnterCommandThread = th.Timer(targetTime, AcceptCommand)

    #start the timers
    PreTimerThread.start()
    EnterCommandThread.start()

def AcceptCommand():
    kcmd.press("x")

def RestartCommand():
    kcmd.hotkey("z", "x","backspace","enter")

def CalculateTargetTime():
    #get the value from pre-timer, target frame, last frame
    preTimer = int(ent_PreTimer.get())
    targetFrame = int(ent_TargetFrame.get())
    lastFrame = int(ent_LastFrame.get())

    return (round(((targetFrame - lastFrame) * GBA_FRAMERATE)) / 1000) + preTimer

window = tk.Tk()
window.title("Shiny Hunter")

#tkinter variables
preTimer = tk.IntVar(window, value = 0, name="preTimer")
targetFrame = tk.IntVar(window, value = 0, name="targetFrame")
lastFrame = tk.IntVar(window, value = 0, name="lastFrame")


frm_WindowFrame = tk.Frame(master=window, width=400, height=400)
frm_WindowFrame.pack(fill="both", padx=10, pady=10)


frm_PreTimer = tk.Frame(master=frm_WindowFrame)
frm_PreTimer.pack(fill="x", padx=5, pady=5)
lbl_PreTimer = ttk.Label(master=frm_PreTimer, text="Pre-Timer (in seconds): ")
lbl_PreTimer.pack(side="left")
ent_PreTimer = ttk.Entry(master=frm_PreTimer, textvariable=preTimer)
ent_PreTimer.pack(side="right")


frm_TargetFrame = tk.Frame(master=frm_WindowFrame)
frm_TargetFrame.pack(fill="x", padx=5, pady=5)
lbl_TargetFrame = ttk.Label(master=frm_TargetFrame, text="Target Frame: ")
lbl_TargetFrame.pack(side="left")
ent_TargetFrame = ttk.Entry(master=frm_TargetFrame, textvariable=targetFrame)
ent_TargetFrame.pack(side="right")


frm_LastFrame = tk.Frame(master=frm_WindowFrame)
frm_LastFrame.pack(fill="x", padx=5, pady=5)
lbl_LastFrame = ttk.Label(master=frm_LastFrame, text="Last frame hit:")
lbl_LastFrame.pack(side="left")
ent_LastFrame = ttk.Entry(master=frm_LastFrame, textvariable=lastFrame)
ent_LastFrame.pack(side="right")


btn_Start = tk.Button(master=frm_WindowFrame, text="Start")
btn_Start.bind("<Button-1>", TimedCodeExecution)
btn_Start.pack(padx=5, pady=5)


frm_CountDown = tk.Frame(master=frm_WindowFrame)
frm_CountDown.pack(fill="x", side="bottom", padx=5, pady=5)
lbl_CountDownTimerText = ttk.Label(master=frm_CountDown, text="Time remaining: ")
lbl_CountDownTimerNumbers = ttk.Label(master=frm_CountDown, text="0000000.000")
lbl_CountDownTimerText.pack()
lbl_CountDownTimerNumbers.pack()

window.mainloop()