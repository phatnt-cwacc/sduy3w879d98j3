import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class EraseVideo:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Erase Video")

        self.input_vid = tk.Entry(window, width=100)
        self.input_vid.grid(row=0, column=0, padx=0, pady=0)

        add_video_btn = tk.Button(window, text="Erase Video", command=self.erasevid)
        add_video_btn.grid(row=1, column=0, padx=0, pady=0)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    
    def erasevid(self):
        key = self.input_vid.get()
        
        try:
            lib.library.pop(key)
        except KeyError:
            set_text(self.list_txt, "Video not found")
            return
        
        set_text(self.list_txt, lib.list_all())