from tkinter import *
import tkinter.messagebox
import os
import time
def check():
	file_size = os.path.getsize('/root/Desktop/Tracker/server/maplink.txt')
	while True:
		new_size=os.path.getsize('/root/Desktop/Tracker/server/maplink.txt')
		if (new_size > file_size):
			tkinter.messagebox.showinfo("Location Found", "the location has been found, click ok to visit their location")

			break
	mapp = open('/root/Desktop/Tracker/server/maplink.txt','r')
	os.system(mapp)
	
def link():
	os.system("""bash trace.sh> programLog.txt 2>&1 &""")
	def copying(event):
		button.config(text="copied link",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
		copier = Tk()
		r = open("/root/Desktop/Tracker/server/links.txt")
		copier.withdraw()
		copier.clipboard_clear()
		copier.clipboard_append(r.read())
		copier.update()
		copier.destroy()
		 
	file_size = os.path.getsize('/root/Desktop/Tracker/server/links.txt')
	while True:
		new_size=os.path.getsize('/root/Desktop/Tracker/server/links.txt')
		if (new_size > file_size):
			button.config(text="copy link",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
			button.bind('<Enter>', copying)
			break
root=Tk()
root.title("Location Tracker")
root.geometry("500x300")
button= Button(root, text="generate link", font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=link)
button.grid(row=2, column=3)

button2=Button(root, text="check result", font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=check)
button2.grid(row=3,column=3)
root.mainloop()