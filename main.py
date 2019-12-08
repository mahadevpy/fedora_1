from option_1 import open_app
from option_2 import camera_wid
from option_3 import github_wid
from op import option
import tkinter as tk
n = 0;
window = tk.Tk()
window.geometry("250x150")
window.title('Google Code In')
python = tk.Button(window, text = "Python", width = 25, command =  open_app)
python.pack()
camera_w = tk.Button(window, text = "Take a Photo", width = 25, command = camera_wid)
camera_w.pack()
git = tk.Button(window, text = "Open Github", width = 25, command = github_wid)
git.pack()
exit = tk.Button(window, text = "Quit", width = 5, command = window.quit, fg = "Red")
exit.pack(side = 'bottom')
options = tk.Button(window, text = "Options", width = 10, command = option, fg = 'Blue')
options.pack(side = 'bottom')

window.mainloop()
