from .models import Post
from django.shortcuts import render
from .forms import CommentModelForm
from django.http import HttpResponse



def form_comment (request):    
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponse('Formulaire envoyé')
            
        else:
            print('error') 
            
    else:
        form = CommentModelForm()

    return render(request, 'NewFilm/form-comment.html', {"formulaire": form})
