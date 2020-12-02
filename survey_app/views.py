from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'gender': request.POST['gender'],
            'lang': request.POST['language'],
            'loc': request.POST['location'],
            'contnt': request.POST['contnt']
        }
        return render(request, 'results.html', context)