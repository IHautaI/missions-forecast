from django import forms


class RelevanceForm(forms.ModelForm):

    relevant = forms.NullBooleanField()

    class Meta:
        model = Award
        fields = ('relevant', )
