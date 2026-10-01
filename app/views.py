from django.shortcuts import render, redirect
from .models import Zayavka, Review, User
from .forms import CreateZayavkaForm, CreateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    
    if(request.method == 'POST'):
        
        review = request.POST.get('review')
        
        if(review == ''):
            return redirect('/')
        
        zayavka_id = request.POST.get('zayavka_id')
        zayavka_db = Zayavka.objects.get(id=zayavka_id)
        
        Review.objects.create(
            text=review,
            user=request.user,
            zayavka=zayavka_db
            
        )
        
        return redirect('/')
        
    data = Zayavka.objects.filter(user=request.user)
    return render(request, 'index.html', context={
        'zayavki': data
    })

def register(request):
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', context={
        'form': form
    })
    
@login_required
def create(request):
    if (request.method == 'POST'):
        form = CreateZayavkaForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.user = request.user
            newForm.save()
            return redirect('/')
    else:
        form = CreateZayavkaForm()
    return render(request, 'create.html', context={
        'form': form
    })