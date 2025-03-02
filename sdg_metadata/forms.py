from django import forms
from .models import SDGMetadata

class SDGMetadataForm(forms.ModelForm):
    class Meta:
        model = SDGMetadata
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label='Search for Projects')