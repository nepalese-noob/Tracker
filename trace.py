from tkinter import *
import os
import time
def link():
	os.system("bash trace.sh")
	while not os.path.exists("/root/Desktop/Target/server/link.txt"):
		time.sleep(1)

	if os.path.isfile("/root/Desktop/Target/server/link.txt"):
		button.config(text="list generated click to copy")
	else:
	    raise ValueError("%s isn't a file!" % file_path)
root=Tk()
root.title("Location Tracker")
root.geometry("500x300")
button= Button(root, text="generate link", font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=link).grid(row=2, column=3)
root.mainloop()