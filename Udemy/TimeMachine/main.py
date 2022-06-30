from pprint import pprint
from tkinter import *
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tkinter import messagebox

SPOT_CLI= "your-client-id"
SPOT_KEY= "your-client-secret" 
SPOT_URI= "your-uri-redirect"

scope= "playlist-modify-private"
username="your-username"

def playlist():
    global scope, username

    try:
        data= date.get()
        name_pl= playlist_name.get()
        descr_pl= play_descr.get(1.0, END)

        if len(data)==0 or len(name_pl)==0:
            messagebox.showinfo(title='Oops', message="Please don't leave the first two fields empty!")

        else:
            response = requests.get(f"https://www.billboard.com/charts/hot-100/{data}/").text
            soup= BeautifulSoup(response, 'html.parser')
            titles= soup.find_all("h3", id="title-of-a-story", class_="a-font-primary-bold-s")
            songs= [song.getText().replace('\n', '').replace('\t', '') for song in titles ]
            for song in songs:
                print(f"{song}\n")

            #Spotify ascess
                    
            token= SpotifyOAuth(
                scope=scope, 
                username= username, 
                client_id=SPOT_CLI, 
                client_secret=SPOT_KEY, 
                cache_path="./Udemy/TimeMachine/src/token.txt", 
                redirect_uri=SPOT_URI
                )  #Para criar o token tem que passar os paramêtros acima

                # Então cria um spotify object para executar as ações passando o token como parametro

            spotObject= spotipy.Spotify(auth_manager= token)
            
            user_id = spotObject.current_user()["id"]

            #Procurando as músicas

            songs_uri=[]
            year= data.split('-')[0] #Pegar o ano com split
            for s in songs:
                result= spotObject.search(q=f'track:{s} year:{year}', type="track") # metodo search com a query (o que voce quer pesquisar) e o tipo da search
                try: # tentar pegar a uri e adicionar na lista
                    uri= result['tracks']['items'][0]['uri']
                    songs_uri.append(uri)
                except: # se não achar a track é pq não existe no spotify
                    print(f"{s} doesn't exist in Spotify. Skipped.")
            
            #Criando a Playlist


            if descr_pl=='':
                descr_pl= None

            playlist= spotObject.user_playlist_create(user= username, name= name_pl, public=False, description= descr_pl)

            #Adicionando as músicas

            spotObject.playlist_add_items(playlist_id= playlist['id'], items= songs_uri[1:])

            #Avisar quando terminar

            messagebox.showinfo(title="let's listen", message="The playlist has been created, go listen to it on your spotify.")

    except:
        messagebox.showinfo(title='Oops', message="Something went wrong, please check the inputs and try again.")

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


descr_label= Label(text="Playlist's description:\n(Optional)", font= ('Arial', 10))
descr_label.grid(column=1, row=6)
play_descr= Text(screen, height = 4, width = 30)
play_descr.grid(column=1, row=7)



btn= Button(text="Create", command=playlist, width=20)
btn.grid(column=1, row=8)

screen.mainloop()