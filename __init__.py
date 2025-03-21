from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Page d'accueil

# Génération d'une clé unique (valable tant que le serveur reste actif)
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Chiffrement de la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retour en str pour l'affichage

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur = f.decrypt(token_bytes)  # Déchiffrement avec la clé
        return f"Valeur décryptée : {valeur.decode()}"  # Retour en texte lisible
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
