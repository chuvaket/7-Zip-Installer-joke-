from tkinter import *
import webbrowser
import time 

buttontxt = ' Install '

root = Tk()

root.title("7-Zip Installer")
root.geometry("400x250")


def Quit():
    root.quit()


def Rick():
    """Open in webbrowser link which you given"""
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #open browser
    time.sleep(1)
    a = 1
    return a


text_label = Label(root, text="Welcome to the 7-Zip installer!", font=40)
text_label.pack(pady=(0,20))


text_labely = Label(root, text="\n Starting the installation \n Download path: C:\Program Files(x86)\ 7-Zip")
text_labely.pack()


button_exit = Button(root, text=' Exit ', font=20, command=Quit,)
button_exit.pack(side=BOTTOM, pady=30)


button_start = Button(root, text=buttontxt, font=20, command=Rick,)
button_start.pack(side=BOTTOM, pady=10)



root.mainloop()