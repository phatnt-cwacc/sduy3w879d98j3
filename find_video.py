import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class FindVideo:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Find Video by Name")

        self.input_vid = tk.Entry(window, width=100)
        self.input_vid.grid(row=0, column=0, padx=0, pady=0)

        add_video_btn = tk.Button(window, text="Find Video", command=self.findvid)
        add_video_btn.grid(row=1, column=0, padx=0, pady=0)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    
    def findvid(self):
        key = self.input_vid.get()
        # get the video name
        res = ''
        for libkey, libitem in lib.library.items():
            if libitem.name.lower().find(key) != -1 or libitem.director.lower().find(key) != -1:
                res += libitem.info() + "\n"

        if res == '':
            set_text(self.list_txt, "Video name not found")
        else:
            set_text(self.list_txt, res)



       