from django import forms

from .models import stockdetalle, cuenta


# class cuentaForm(forms.ModelForm):
#
#     class Meta:
#         model = cuenta
#         exclude = ()
#
# cuentaFormSet = forms.inlineformset_factory(cuenta, stockdetalle, form=cuentaForm, extra=1)

class stockdetalleForm(forms.ModelForm):
    class Meta:
        model = stockdetalle
        exclude = ()

stockdetalleFormSet = forms.inlineformset_factory(cuenta, stockdetalle,
                                            form=stockdetalleForm, extra=5)




