from tkinter import *
import os
import time
def check(/root/Desktop/Tracker/server/maplink.txt, attempts=0, timeout=5, sleep_int=5):
    if attempts < timeout and os.path.exists(/root/Desktop/Tracker/server/maplink.txt) and os.path.isfile(/root/Desktop/Tracker/server/maplink.txt): 
        try:
            file = open(/root/Desktop/Tracker/server/maplink.txt)
            messagebox.showinfo("Location Found")
        except:
            # perform an action
            sleep(sleep_int)
            check(/root/Desktop/Tracker/server/maplink.txt, attempts + 1)