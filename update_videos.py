import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import check_videos as vidcheck

class UpdateVideo:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Update Video")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=0, pady=0)

        enter_lbl = tk.Label(window, text="Enter Rating")
        enter_lbl.grid(row=1, column=1, padx=0, pady=0)

        self.input_txt_vid = tk.Entry(window, width=3)
        self.input_txt_vid.grid(row=0, column=2, padx=0, pady=0)

        self.input_txt_rating = tk.Entry(window, width=3)
        self.input_txt_rating.grid(row=1, column=2, padx=0, pady=0)

        add_video_btn = tk.Button(window, text="Update Video", command=self.update_video_rating)
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    
    def update_video_rating(self):
        key = self.input_txt_vid.get()
        # get the video name
        name = lib.get_name(key)
        if name is not None:
            lib.library[key].rating = int(self.input_txt_rating.get())
            vidcheck.set_text(self.list_txt, lib.list_all())
        else:
            vidcheck.set_text(self.list_txt, f"Video {key} not found")