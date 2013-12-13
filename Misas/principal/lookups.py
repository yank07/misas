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