from tkinter import *
import os
import time
def link():
	def copying(event):
		button.config(text="copied link",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
		copier = Tk()
		r = open("/root/Desktop/Tracker/server/link.txt")
		copier.withdraw()
		copier.clipboard_clear()
		copier.clipboard_append(r.read())
		copier.update()
		copier.destroy()
		
	os.system("""bash trace.sh> programLog.txt 2>&1 &""")
	file_size = os.path.getsize('/root/Desktop/Tracker/server/link.txt')
	while True:
		new_size=os.path.getsize('/root/Desktop/Tracker/server/link.txt')
		if (new_size > file_size):
			button.config(text="copy link",font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN)
			button.bind('<Enter>', copying)
			break
root=Tk()
root.title("Location Tracker")
root.geometry("500x300")
button= Button(root, text="generate link", font=('Times New Roman', 18,'bold'), bg="purple", fg="yellow", state="normal", activebackground="blue", activeforeground="red", cursor="hand2", relief=SUNKEN, command=link)
button.grid(row=2, column=3)
root.mainloop()