from flask import Flask, render_template
import requests
from post import Post

response= requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects= []
for p in response:
    post_obj= Post(p['id'], p['title'], p['subtitle'], p['body'])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", post=post_objects)

@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", num= num, post= post_objects[num-1])

if __name__ == "__main__":
    app.run(debug=True)
