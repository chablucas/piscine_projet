# script.py

import requests
from BlogMovies.models import Post

def get_top_100_movies(api_key, access_token):
    base_url = 'https://image.tmdb.org/t/p/w500'  # URL de base des affiches avec une largeur de 500 pixels

    url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
        'api_key': api_key,
        'page': 6
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'results' in data:
        # Triez les films par ordre alphabétique du titre
        sorted_movies = sorted(data['results'], key=lambda x: x['title'])

        # Enregistrez les informations pour les 100 premiers films dans la base de données
        for movie_data in sorted_movies[:100]:
            title = movie_data.get('title', 'N/A')

            # Vérifiez si le film existe déjà dans la base de données
            if not Post.objects.filter(title=title).exists():
                # Le film n'existe pas, ajoutez-le à la base de données
                post = Post(
                    title=title,
                    date=movie_data.get('release_date'),
                    content=movie_data.get('overview', 'N/A'),  # Ajout de la description
                    poster_path=f"{base_url}{movie_data.get('poster_path', 'N/A')}",  # URL complète de l'affiche
                )
                post.save()

                print(f"Post saved: {post.title}")
            else:
                print(f"Le film '{title}' existe déjà dans la base de données.")

    else:
        print(f"Error: {data.get('status_message', 'Unknown error')}")

# Fonction run() ajoutée
def run():
    api_key = 'b431efe348ad83c9f97e43296b16f0bf'
    access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNDMxZWZlMzQ4YWQ4M2M5Zjk3ZTQzMjk2YjE2ZjBiZiIsInN1YiI6IjY1NjljMDY0NzFmMDk1MDExYjI2MDU1MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W9fItTz3SY76bdoKEyW9hDvJfgrpY_SMbQQoC66G0Hc'

    # Utilisez la fonction avec votre clé d'API et jeton d'accès
    get_top_100_movies(api_key, access_token)
