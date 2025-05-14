# sentiment_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from textblob import TextBlob
from .forms import SentimentAnalysisForm

# ============================================
# Aplicação Web de Análise de Sentimento com Django
# ============================================
# Autor: Gustavo Rodrigues Ribeiro
# Descrição: Este projeto é uma aplicação web simples desenvolvida
# utilizando o framework Django. O objetivo principal é permitir que 
# usuários autenticados submetam blocos de texto para análise de sentimento. 
# A aplicação processa o texto e retorna uma classificação (Positivo, Negativo ou Neutro)
# acompanhada de uma pontuação numérica de polaridade.
# ============================================

@login_required
def analyze_sentiment_view(request):
    form = SentimentAnalysisForm()
    analysis_result = None

    if request.method == 'POST':
        form = SentimentAnalysisForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_to_analyze']
            try:
                # Realiza a análise de sentimento
                blob = TextBlob(text)
                polarity = blob.sentiment.polarity

                # Classifica o resultado da análise em positivo, neutro e negativo
                if polarity > 0.1:
                    sentiment = "Positivo"
                    sentiment_class = "success"
                elif polarity < -0.1:
                    sentiment = "Negativo"
                    sentiment_class = "danger"
                else:
                    sentiment = "Neutro"
                    sentiment_class = "secondary"

                analysis_result = {
                    'text': text,
                    'polarity': round(polarity, 3),
                    'sentiment': sentiment,
                    'sentiment_class': sentiment_class,
                }
                # Mantém o texto no formulário após a análise
                form = SentimentAnalysisForm(initial={'text_to_analyze': text})

            except Exception as e:
                # Logar o erro 'e' seria ideal em produção
                analysis_result = {
                    'error': 'Ocorreu um erro ao analisar o texto. Tente novamente.'
                }
        # Se o formulário POST não for válido, ele será re-renderizado com os erros

    context = {
        'form': form,
        'analysis_result': analysis_result,
    }
    return render(request, 'sentiment_app/analyze.html', context)