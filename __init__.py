from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# 🏠 Page d'accueil
@app.route('/')
def hello_world():
    return render_template('hello.html')

# 🔐 Exercice 1 : chiffrement avec clé fixe du serveur
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()
        valeur = f.decrypt(token_bytes)
        return f"Valeur décryptée : {valeur.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"

# 🔑 Exercice 2 : chiffrement/déchiffrement avec clé personnelle fournie
@app.route('/encrypt/<string:cle>/<string:valeur>')
def encrypt_personnel(cle, valeur):
    try:
        f_perso = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        token = f_perso.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur de chiffrement : {str(e)}"

@app.route('/decrypt/<string:cle>/<string:token>')
def decrypt_personnel(cle, token):
    try:
        f_perso = Fernet(cle.encode())
        token_bytes = token.encode()
        valeur = f_perso.decrypt(token_bytes)
        return f"Valeur décryptée : {valeur.decode()}"
    except Exception as e:
        return f"Erreur de déchiffrement : {str(e)}"

# 🧪 Générateur de clé pour Exercice 2
@app.route('/generate_key')
def generate_key():
    cle = Fernet.generate_key()
    return f"Votre clé Fernet : {cle.decode()}"

if __name__ == "__main__":
    app.run(debug=True)
