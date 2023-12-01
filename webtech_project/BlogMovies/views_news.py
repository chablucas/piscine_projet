from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Post
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.
#request => response

def page_display(request):
    title = 'Movies Blog'
    article = Post.objects.all()[:40]
    username = request.user.username if request.user.is_authenticated else None
    context = {
        'article': article,
        'title': title,
        'name': 'WEBTECH',
        'username': username,
    }
    return render(request, 'BlogMovies/home_page.html', context)
    #template = loader.get_template('blog/article_list.html')
    #return HttpResponse(template.render({}, request))

def search_view(request):
    query = request.GET.get('q', '')

    if query:
        # Diviser la requête en mots-clés
        keywords = query.split()

        # Construire une condition de recherche pour chaque mot-clé
        conditions = Q()
        for keyword in keywords:
            conditions |= Q(title__icontains=keyword)

        results = Post.objects.filter(conditions)
    else:
        results = Post.objects.all()

    return render(request, 'BlogMovies/search_results.html', {'results': results, 'query': query})


def user_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigez l'utilisateur vers la page souhaitée après la connexion
                return redirect('blog_page')  # Remplacez 'pageDisplay' par le nom de votre vue
    else:
        form = UserLoginForm()
    return render(request, 'BlogMovies/your_login_template.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigez l'utilisateur vers la page souhaitée après l'inscription
            return redirect('blog_page')  # Remplacez 'pageDisplay' par le nom de votre vue
    else:
        form = UserRegistrationForm()

    return render(request, 'BlogMovies/your_register_template.html', {'form': form})

def custom_logout(request):
    logout(request)
    return render(request, 'BlogMovies/logout.html')

def post_details(request, parameter_value):
    post = get_object_or_404(Post, title=parameter_value)  # Utilisez le champ que vous souhaitez (title, author, etc.)
    return render(request, 'BlogMovies/detail_movies.html', {'post': post})
