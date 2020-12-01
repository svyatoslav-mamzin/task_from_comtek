from django.urls import path, include

from main_app import views

urlpatterns = [
    # previous login view
    path('glossaries/', views.glossary_list, name='glossaries'),
]
