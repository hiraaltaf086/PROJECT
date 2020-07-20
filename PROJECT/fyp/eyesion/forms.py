from django import forms

from eyesion.models import ImageModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['Image' ]

