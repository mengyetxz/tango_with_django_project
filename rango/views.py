from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    #Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    #Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "This Page is ..."}
    return render(request, 'rango/about.html', context_dict)


