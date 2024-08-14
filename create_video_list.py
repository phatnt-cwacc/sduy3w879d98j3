import tkinter as tk
import tkinter.scrolledtext as tkst

import check_videos as vidcheck
import video_library as lib

from collections import defaultdict

playlist = defaultdict()

def playlist_list():
    res = ""
    for i in playlist:
        item = playlist[i]
        res += f"{i} {item.info()} - {item.play_count} play(s)\n"
    return res

class CreateVideoList:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Create Video List")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video)
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        playvid_btn = tk.Button(window, text="Play Videos", command=self.increase_playcount)
        playvid_btn.grid(row=1, column=3, padx=10, pady=10)

        clearvideo_btn = tk.Button(window, text="Reset Video List", command=self.erase_playlist)
        clearvideo_btn.grid(row=2, column=3, padx=10, pady=10)
    
    def add_video(self):
        key = self.input_txt.get()
        # get the video name
        name = lib.get_name(key)
        if name is not None:
            playlist[key] = lib.library[key]
            vidcheck.set_text(self.list_txt, playlist_list())
        else:
            vidcheck.set_text(self.list_txt, f"Video {key} not found")

    def increase_playcount(self):
        for i in playlist:
            playlist[i].play_count += 1
        vidcheck.set_text(self.list_txt, playlist_list())

    def erase_playlist(self):
        playlist.clear()
        vidcheck.set_text(self.list_txt, playlist_list())