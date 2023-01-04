from flask import Flask, request
import requests

app= Flask(__name__)

DETECT_BASE_URL=  'https://google-translate1.p.rapidapi.com/language/translate/v2/detect'
TRANSLATE_BASE_URL= 'https://google-translate1.p.rapidapi.com/language/translate/v2'

HEADERS= {
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': '2f71864143msh7f3b1c469001d71p1b9b77jsnacca71055d11',
    'content-type': "application/x-www-form-urlencoded"
}

@app.route('/')
def main():
    return 'Translation Service is up'

@app.route('/detect', methods=['POST'])
def detect():
    text= request.form.get('text')
    #url encode text
    long_list= text.split(' ')
    url_encoded_text= f"q={'%20'.join(long_list)}"

    payload= url_encoded_text
    
    #make the request
    r= requests.post(DETECT_BASE_URL, data= payload, headers= HEADERS)
    
    return r.json()

@app.route('/translate', methods=['POST'])
def translate():
    text= request.form.get('text')
    target= request.form.get('target')

    long_list= text.split(' ')
    url_encoded= f"q={'%20'.join(long_list)}&target={target}"

    payload= url_encoded

    r= requests.post(TRANSLATE_BASE_URL, data=payload, headers=HEADERS)
    
    return r.json()

if __name__=='__main__':
    app.run(debug=True)

