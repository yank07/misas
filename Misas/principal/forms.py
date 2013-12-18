from django import forms
from selectable.forms import AutoCompleteWidget, AutoComboboxSelectWidget,AutoCompleteSelectField,AutoComboboxWidget
from principal.lookups import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



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
   
    iglesia = AutoCompleteSelectField(
        lookup_class=IglesiaLookup,
        label='Iglesia',
        widget=AutoComboboxSelectWidget,
        required=False,        
    )
    horario_misa = forms.CharField(
        label='Horario de misa',
        widget=AutoComboboxWidget(HorarioMisaLookup),
        required=False,        
    )
    def __init__(self, *args, **kwargs):
        super(IglesiaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()    
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-inline row'
        self.helper.label_class = 'col-xs-3'
        self.helper.field_class = 'col-xs-8'
        self.helper.form_method = 'get'
        self.helper.form_action = 'search'
        self.helper.add_input(Submit('save', 'save', css_class = 'btn-primary col-xs-offset-3'))

        
    