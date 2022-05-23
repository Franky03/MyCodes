from tkinter import *
from tkinter import messagebox
import pytube
import moviepy.editor as mp
import os

user= os.getenv("USERNAME")
# ---------------------------- FUNCTIONS ------------------------------- #
def mp4_download():
    url= url_input.get()
    if len(url)==0:
        messagebox.showinfo(title='Oops', message="Please don't leave the URL empty!")
    else:
        try:
            video= pytube.YouTube(url)
            video= video.streams.get_highest_resolution()
            video.download(f'C:/Users/{user}/Desktop')
            messagebox.showinfo(title='Downloaded ✔', message='The video has been successfully downloaded to the desktop.')
            url_input.delete(0, END)
        
        except:
            messagebox.showinfo(title='Failed :(', message='Unfortunately the video was not downloaded, please try again.')

def mp3_download():
    url= url_input.get()
    if len(url)==0:
        messagebox.showinfo(title='Oops', message="Please don't leave the URL empty!")
    else:
        try:
            video= pytube.YouTube(url)
            video= video.streams.get_audio_only()
            video.download(f'C:/Users/{user}/Desktop')
            title= str(video.title)
            clip= mp.AudioFileClip(f'C:/Users/{user}/Desktop/{title}.mp4')
            clip.write_audiofile(f'C:/Users/{user}/Desktop/{title}.mp3')
            os.remove(f'C:/Users/{user}/Desktop/{title}.mp4')
            messagebox.showinfo(title='Downloaded ✔', message='The music has been successfully downloaded to the desktop.')
            url_input.delete(0, END)
        
        except:
            messagebox.showinfo(title='Failed :(', message='Unfortunately the video was not downloaded, please try again.')

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.config(padx=10, pady=10, bg='white')
window.title('Youtube Converter')

logo= PhotoImage(file='./Files/YoutubeConverter/download.png')
canvas= Canvas(width=200, height=200, highlightthickness=0, bg='white')
canvas.create_image(100,100,image= logo)
canvas.grid(column=1, row=0)

url_label= Label(text='URL:', font= ('Courier', 18, 'bold'), bg='white')
url_label.grid(column=0, row=1)

url_input= Entry(width=50)
url_input.grid(column=1, row=1, columnspan=2)

mp3= Button(text='MP3', command=mp3_download)
mp3['font']= 'Courier'
mp4= Button(text='MP4', command=mp4_download)
mp4['font']= 'Courier'
mp3.grid(column=0, row=3, ipadx=50)
mp4.grid(column=2, row=3, ipadx=50)


window.mainloop()