from tkinter import *
from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOT_CLI= "f94dfeab131a48bfa5f265be36e0c081"
SPOT_KEY= "" #The Key will be reseted after i commit

def playlist():
    try:
        data= date.get()
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{data}/").text
        soup= BeautifulSoup(response, 'html.parser')
        titles= soup.find_all("h3", id="title-of-a-story", class_="a-font-primary-bold-s")
        songs= [song.getText().replace('\n', '').replace('\t', '') for song in titles ]
        for song in songs:
            if song!="Producer(s):" and song!='Imprint/Promotion Label:' and song!='Songwriter(s):':
                print(f"{song}\n")
        
    except:
        print("ERROR")



#Body
screen= Tk()
screen.config(padx=50, pady=50)
screen.title("Machine Time Playlist")

image= PhotoImage(file="./Udemy/TimeMachine/src/headphone-icon.png")
canva= Canvas(width=200,height=200, highlightthickness=0, )
canva.create_image(100,100, image=image)
canva.grid(column=1, row=0)

text= Label(text="Create a Spotify Playlist", font= ('Arial', 20))
text.grid(column=1, row=1)
date_text= Label(text="The year you want travel to:\nYYYY-MM-DD", font= ('Arial', 10))
date_text.grid(column=1, row=2)

date= Entry(width=30, justify="center")
date.grid(column=1, row=3)

btn= Button(text="Create", command=playlist, width=20)
btn.grid(column=1, row=4)

screen.mainloop()