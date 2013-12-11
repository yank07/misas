# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from ajax_search.forms import SearchForm



def portada(request):
    
    return render_to_response('index.html', context_instance=RequestContext(request))

def search_helper(count, query):
        import itertools
        model_list = Article.objects.filter(title__icontains=query, status=1)
        for L in range(1, count+1):
                for subset in itertools.permutations(words, L):
                        count1=1
                        query1=subset[0]
                        while count1!=len(subset):
                                query1=query1+" "+subset[count1]
                                count1+=1
                        model_list = entry_list | Article.objects.filter(title__icontains=query1, status=1)
        return (model_list.distinct())



