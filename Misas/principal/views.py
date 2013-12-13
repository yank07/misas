# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404 , redirect
from django.template import RequestContext
from principal.forms import FruitForm, IglesiaForm
from django.db.models import Q
from principal.models import Fruit, Ciudad




def portada(request):
    form = FruitForm()
    form2 = IglesiaForm()
    return render_to_response('index.html',{'form':form,'form2':form2}, context_instance=RequestContext(request))



def search(req):
    if 'q' in req.GET:
        entry_list = Fruit.objects.filter(Q(name__contains=req.GET['q']) | Q(peso__contains=req.GET['q']))
        if entry_list.exists():
            return render_to_response("search.html",
                                  {'entry_list':entry_list})
        else:
            return render_to_response("search.html",
                                  {'nada':'no hay resultados'})
    elif 'ciudad' in  req.GET:
        entry_list = Ciudad.objects.filter(Q(nombre__contains=req.GET['ciudad']) )
        if entry_list.exists():
            return render_to_response("searchciudad.html",
                                  {'entry_list':entry_list})
        else:
            return render_to_response("search.html",
                                  {'nada':'no hay resultados'})
        
    else:
        return render_to_response("search_error.html",
                                  {'error':'Search query missing.'})