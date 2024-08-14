import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts

# inserts content into the text_area
def set_text(text_area, content):
    # delete existing content
    text_area.delete("1.0", tk.END)
    # insert new content
    text_area.insert(1.0, content)

# check for available videos
class CheckVideos():
    def __init__(self, window):
         # change the window width and height to 750 and 350 pixels respectively
        window.geometry("750x350")
         # change the title of the window on the menu bar
        window.title("Check Videos")

        # create a button that lists all videos when clicked
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        # set the position of the button
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # create a label for a text input area
        enter_lbl = tk.Label(window, text="Enter Video Number")
        # set the position of the label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # create a text input area
        self.input_txt = tk.Entry(window, width=3)
        # set the text input area position
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # create a button that checks all videos when clicked
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        # set the button position
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # create scrolling textbox
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        # set the textbox position
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # create a text area
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        # set the text input box position
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # create a status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        # set label position
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # list videos
        self.list_videos_clicked()

    # check if the "check video" button was clicked
    def check_video_clicked(self):
        # get text from the text input box
        key = self.input_txt.get()
        # get the video name
        name = lib.get_name(key)
        # if video is found
        if name is not None:
            # get the director, rating, and play count then format into a string, then display the string
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        # if video is not found
        else:
            # notify the user that the video is not found
            set_text(self.video_txt, f"Video {key} not found")

        # notify the user that the "check video" button is clicked
        self.status_lbl.configure(text="Check Video button was clicked!")

    # list all videos upon click
    def list_videos_clicked(self):
        # list all videos
        video_list = lib.list_all()
        # display the listed videos
        set_text(self.list_txt, video_list)
        # notify the user
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
