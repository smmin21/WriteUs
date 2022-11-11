from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import *
from .apps import WriteusAppConfig

# Create your views here.
def home(request):
    if (request.method == 'POST'):
        new_novel = Novel()
        new_novel.tmp_body = request.POST['body']
        new_novel.pub_date = timezone.now()
        new_novel.save()
        return redirect('create', new_novel.id)
    return render(request, 'home.html')

def create(request, nID):
    novel = get_object_or_404(Novel, id=nID)
    if (request.method == 'POST'):
        novel.body += ' ' + novel.tmp_body
        novel.tmp_body = request.POST['body']
        novel.tmp_body += " " + WriteusAppConfig.generator.text_generator(novel.tmp_body)
        novel.save()
        return redirect('create', novel.id)
    else:
        if novel.body == '':
            novel.tmp_body += " " + WriteusAppConfig.generator.text_generator(novel.tmp_body)
            novel.save()
    ctx = {
        'novel':novel,
    }
    return render(request, 'create.html', ctx)