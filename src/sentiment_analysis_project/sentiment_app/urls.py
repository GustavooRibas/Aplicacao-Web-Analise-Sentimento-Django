# sentiment_app/urls.py
from django.urls import path
from . import views # Importa as views do app atual
from django.contrib.auth import views as auth_views # Importa views de autenticação do Django

urlpatterns = [
    # Rota para login (usa view padrão do Django, aponta para nosso template)
    path('login/', auth_views.LoginView.as_view(template_name='sentiment_app/login.html'), name='login'),

    # Rota para logout (usa view padrão do Django)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Rota principal da aplicação (/) que chama nossa view de análise
    path('', views.analyze_sentiment_view, name='analyze'),
]