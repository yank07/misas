from django import forms
from selectable.forms import AutoCompleteWidget
from principal.lookups import *

class FruitForm(forms.Form):
    q = forms.CharField(
        label='Type the name of a fruit (AutoCompleteWidget)',
        widget=AutoCompleteWidget(FruitLookup),
        required=False,
    )
    
class IglesiaForm(forms.Form):
    ciudad = forms.CharField(
        label='Ciudad',
        widget=AutoCompleteWidget(CiudadLookup),
        required=False,        
    )
    