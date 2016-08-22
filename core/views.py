from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	template_name = "core/index.html"
	return render(request, template_name)

def cursos(request):
	template_name = 'core/cursos.html'
	return render(request, template_name)

def contato(request):
	template_name = 'core/contato.html'
	return render(request, template_name)