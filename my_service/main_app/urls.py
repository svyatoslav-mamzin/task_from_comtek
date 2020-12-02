from django.urls import path, include

from .views import GlossaryView, CurrentGlossariesView, ElementsGlossarySpecVersView, ElementsGlossaryCurrentVersView

app_name = "main_app"

urlpatterns = [
    path('elements/<id>/<version>', ElementsGlossarySpecVersView.as_view()),
    path('elements/<id>', ElementsGlossaryCurrentVersView.as_view()),
    path('glossaries/<date>', CurrentGlossariesView.as_view()),
    path('glossaries/', GlossaryView.as_view()),
]