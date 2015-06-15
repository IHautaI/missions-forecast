from django import forms
from django.forms import widgets

from forecast.models import Award



class RelevanceForm(forms.ModelForm):
    attrs = {'onclick':'this.form.submit();'}

    def __init__(self, init, *args, **kwargs):
        if init:
            self.attrs['checked'] = 'checked'

        super(RelevanceForm, self).__init__(self, *args, **kwargs)

    relevant = forms.BooleanField(widget=widgets.CheckboxInput(\
                attrs=attrs), required=False)

    class Meta:
        model = Award
        fields = ('relevant', )
