from django.shortcuts import render
from . forms import Search
from . models import Corpus, Zone
from . import das

# Create your views here.

def start(request):
    template = 'app_one/index.html'
    context = {}
    return render(request, template, context)

def product(request):
    template = 'app_one/product.html'
    context = {}
    return render(request, template, context)

def subject(request):
    template = 'app_one/subject.html'
    context = {}
    return render(request, template, context)

def testform(request):
    form = Search
    template = 'app_one/visual.html'
    context = {'form':form}
    das.app
    print('k')
    # o1 = Corpus.objects.values('name_corpus')
    # print(o1)


    # o1 = Corpuses.objects.values('number_corpus')
    # # for i in o1:
    # #     print(i['number_corpus'])
    # # print(o1)
    # o2 = Corpuses.objects.filter(number_corpus=65)
    # o2 = o2.values('zones')
    # print(o2)
    return render(request, template, context)

