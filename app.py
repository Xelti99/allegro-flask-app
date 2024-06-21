from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'https://Xelti99.github.io/allegro-redirect2'

@app.route('/')
def home():
    return '<a href="https://allegro.pl/auth/oauth/authorize?response_type=code&client_id={}&redirect_uri={}&scope=allegro_api_scope">Login with Allegro</a>'.format(CLIENT_ID, REDIRECT_URI)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'Authorization failed.'

    token_url = "https://allegro.pl/auth/oauth/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(token_url, headers=headers, data=data)
    token_data = response.json()
    return f"Access Token: {token_data.get('access_token')}"

if __name__ == '__main__':
    app.run()
