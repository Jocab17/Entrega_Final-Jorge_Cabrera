from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'header', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'header', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'cuerpo')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }