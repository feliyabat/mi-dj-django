from django.shortcuts import render

def home(request):
    return render(request, 'pfront/home.html')

def about(request):
    return render(request, 'pfront/about.html')

def contact(request):
    sent = False
    if request.method == 'POST':
        # nombre = request.POST.get('nombre'); mensaje = request.POST.get('mensaje')
        sent = True
    return render(request, 'pfront/contact.html', {'sent': sent})