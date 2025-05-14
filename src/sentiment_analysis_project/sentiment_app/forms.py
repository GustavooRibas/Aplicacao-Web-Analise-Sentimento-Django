# sentiment_app/forms.py
from django import forms

class SentimentAnalysisForm(forms.Form):
    text_to_analyze = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', # Classe Bootstrap
            'rows': 5,
            'placeholder': 'Digite ou cole o texto aqui para análise...'
        }),
        label="Texto para Análise",
        required=True
    )