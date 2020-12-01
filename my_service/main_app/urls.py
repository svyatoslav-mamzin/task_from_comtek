from django.urls import path, include

from .views import GlossaryView

app_name = "main_app"

urlpatterns = [
    path('glossaries/', GlossaryView.as_view()),
]