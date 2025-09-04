from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à BSI4 Store!</h1> <p><a href='/about/'>Sobre</a></p>")

def about(request):
    return HttpResponse("<h1>Sobre a BSI4 Store</h1> <p><a href='/'>Voltar para a Home</a></p>")