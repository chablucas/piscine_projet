from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
#request => response

def pageDisplay(request):
    title = 'Movies Blog'
    article = Post.objects.all()
    username = request.user.username if request.user.is_authenticated else None
    context = {
        'article': article,
        'title': title,
        'name': 'WEBTECH',
        'username': username,
    }
    return render(request, 'blog/news_list.html', context)
    #template = loader.get_template('blog/article_list.html')
    #return HttpResponse(template.render({}, request))
    
def detailDisplay(request):
    article = []
    
    print(type(request.GET.get('article')))
    
    if request.GET.get('article') == '20':
        return HttpResponseNotFound("Pas d'articles")
    
    if request.GET.get('article'):
        article_id = request.GET.get('article')
        #article = Post.objects.get(id = article_id)
        article = get_object_or_404(Post, id = article_id)
        
    return render (request, 'blog/news_detailPage.html', {'article':article})
    
def form_comment(request):
    print(request.POST)
    print(request.GET)
    
    if request.POST:
        Post.objects.create(title = request.POST.get('title'), author = request.POST.get('author'))
    return render (request, 'blog/comment-form.html')



# views.py
# views.py
from django.shortcuts import render
from .models import Post
from django.db.models import Q

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

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})




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

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from blog.forms import UserLoginForm

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
    return render(request, 'blog/your_login_template.html', {'form': form})

# views.py

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigez l'utilisateur vers la page souhaitée après l'inscription
            return redirect('blog_page')  # Remplacez 'pageDisplay' par le nom de votre vue
    else:
        form = UserRegistrationForm()

    return render(request, 'blog/your_register_template.html', {'form': form})


#drf