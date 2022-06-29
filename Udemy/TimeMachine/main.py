from tkinter import *
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import json

SPOT_CLI= ""
SPOT_KEY= "" #The Key will be reseted after i commit
SPOT_URI= ""

scope= "playlist-modify-private"
username=""

def playlist():
    global scope, username

    data= date.get()
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{data}/").text
    soup= BeautifulSoup(response, 'html.parser')
    titles= soup.find_all("h3", id="title-of-a-story", class_="a-font-primary-bold-s")
    songs= [song.getText().replace('\n', '').replace('\t', '') for song in titles ]
    for song in songs:
        if song!="Producer(s):" and song!='Imprint/Promotion Label:' and song!='Songwriter(s):':
            print(f"{song}\n")

    #Spotify ascess
            
    token= SpotifyOAuth(
        scope=scope, 
        username= username, 
        client_id=SPOT_CLI, 
        client_secret=SPOT_KEY, 
        cache_path="./Udemy/TimeMachine/src/token.txt", 
        redirect_uri=SPOT_URI
        )

    spotObject= spotipy.Spotify(auth_manager= token)
    
    user_id = spotObject.current_user()["id"]
    print(user_id)

    




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

play_label= Label(text="Playlist's name:", font= ('Arial', 10))
play_label.grid(column=1, row=4)
playlist_name= Entry(width=30, justify="center")
playlist_name.grid(column=1, row=5)


descr_label= Label(text="Playlist's description:", font= ('Arial', 10))
descr_label.grid(column=1, row=6)
play_descr= Text(screen, height = 4, width = 30)
play_descr.grid(column=1, row=7)



btn= Button(text="Create", command=playlist, width=20)
btn.grid(column=1, row=8)

screen.mainloop()