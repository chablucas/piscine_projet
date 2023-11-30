from models import Post
from datetime import date

# Créez une instance du modèle Post
new_post = Post(
    title='Titre du post',
    content='Contenu du post',
    date=date.today(),
    active=True,
    author='Auteur du post'
)

# Enregistrez le post dans la base de données
new_post.save()

print('Post créé avec succès!')