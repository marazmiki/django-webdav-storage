from django import forms

from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
