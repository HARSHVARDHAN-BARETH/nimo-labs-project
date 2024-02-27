from tkinter import *
from pytube import YouTube

def download_video():
    link = yt_link.get()
    try:
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        stream.download("")
        status_label.config(text="Done Successfully!", fg="green")
    except Exception as e:
        status_label.config(text="Download Failed ", fg="red")

root = Tk()
root.geometry("500x350")
root.title("Youtube Downloader")
root.config(bg="#f0f8ff")

# Label
label = Label(root, text="Enter your video link", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#1e90ff", pady=15)
label.pack(pady=10)

# Entry
yt_link = Entry(root, width=40, font=("Helvetica", 12), bd=2, relief="groove", insertbackground="#1e90ff")
yt_link.pack(pady=10, ipady=10)

# Button
download_button = Button(root, text="Download", command=download_video, pady=10, padx=10, bg="#dc143c", fg="white", font=("Helvetica", 12, "bold"))
download_button.pack()

# Status Label
status_label = Label(root, text="", font=("Helvetica", 12), bg="#f0f8ff")
status_label.pack(pady=10)

root.mainloop()
