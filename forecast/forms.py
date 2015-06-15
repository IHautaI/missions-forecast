from django import forms
from django.forms import widgets

from forecast.models import Award



class RelevanceForm(forms.ModelForm):
    attrs = {'onclick':'this.form.submit();'}

    relevant = forms.BooleanField(widget=widgets.CheckboxInput(\
                attrs=attrs), required=False)

    class Meta:
        model = Award
        fields = ('relevant', )
