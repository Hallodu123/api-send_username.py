import os
import requests
from flask import Flask

app = Flask(__name__)

# Setze hier deine Webhook-URL ein
WEBHOOK_URL = "<https://discordapp.com/api/webhooks/1299309155097509949/JAvAAZMaH-ZyoP9g2ETw_p-7JE0EUG2qrnLsWIAdb4IDg90yZkONcbGGuyDLH9QBiri8>"

@app.route('/api/send_username')
def send_username():
    # Benutzername über die Discord-API abrufen (dazu benötigen wir den Token)
    username = "<splash64_>"  # Füge hier deinen Discord-Benutzernamen hinzu
    
    # Nachricht mit Benutzername erstellen
    content = {
        "content": f"Benutzername: {username}"
    }

    # Nachricht an Discord-WebHook senden
    response = requests.post(WEBHOOK_URL, json=content)

    if response.status_code == 204:  # Erfolgreiche Antwort
        return "Dein Benutzername wurde erfolgreich gesendet!", 200
    else:
        return "Fehler beim Senden der Nachricht", response.status_code

# Route für das GIF
@app.route('/gif')
def gif():
    return '''
    <html>
        <body>
            <a href="/api/send_username" target="_blank">
                <img src="https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif" alt="Klicke hier!" />
            </a>
        </body>
    </html>
    '''


