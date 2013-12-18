from selectable.base import ModelLookup
from selectable.registry import registry, LookupAlreadyRegistered
from principal.models import *

class FruitLookup(ModelLookup):
    model = Fruit
    search_fields = ('name__icontains', )
    
registry.register(FruitLookup)


class CiudadLookup(ModelLookup):
    model = Ciudad
    search_fields = ('nombre__icontains', )
    
registry.register(CiudadLookup)



class IglesiaLookup(ModelLookup):
    model = Iglesia
    search_fields = ('nombre__icontains', )
    def get_query(self, request, term):
        results = super(IglesiaLookup, self).get_query(request, term)
        ciudadd = request.GET.get('ciudad', '')
        if ciudadd:
            results = results.filter(ciudad__nombre=ciudadd)
        return results

    def get_item_label(self, item):
        return u"%s, %s" % (item.nombre, item.ciudad)
    
registry.register(IglesiaLookup)

class HorarioMisaLookup(ModelLookup):
    model = HorarioMisa
    search_fields = ('hora__icontains', )
    
registry.register(HorarioMisaLookup)

