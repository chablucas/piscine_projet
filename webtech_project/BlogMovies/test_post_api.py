import os
from django import setup

# Spécifiez le chemin complet vers le fichier manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webtech_project.settings')
setup()

import requests
from models import Post  

# Définissez la fonction de création de post
def creer_post(author, date, title, content, imdb_id):
    url = 'http://www.omdbapi.com/?apikey=5d612a88&i=' + imdb_id  # Utilisez l'identifiant IMDb dans l'URL

    # Créer un objet Post au lieu d'envoyer une requête POST
    post = Post(author=author, date=date, title=title, content=content)
    post.save()

    if post.id:
        print('Post créé avec succès!')
    else:
        print('Erreur lors de la création du post.')

# Définissez la fonction de recherche de film
def rechercher_film(movie_title):
    url = f'http://www.omdbapi.com/?apikey=5d612a88&s={movie_title}'
    response = requests.get(url)

    if response.status_code == 200:
        # Extraction de l'identifiant IMDb à partir de la réponse de recherche
        imdb_id = response.json()["Search"][0]["imdbID"]

        # Utilisation de l'identifiant IMDb pour la création de post
        creer_post(author='John Doe', date='2023-11-30', title='Mon post sur un film', content='Contenu du post', imdb_id=imdb_id)
    else:
        print(f'Erreur lors de la recherche du film. Statut: {response.status_code}, Message: {response.text}')

# Exécutez la fonction de recherche de film avec un titre de film spécifique
rechercher_film('Inmoraru')
