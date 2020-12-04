from django.urls import path, include

from .views import GlossaryView, CurrentGlossariesView, ElementsGlossarySpecVersView, ElementsGlossaryCurrentVersView, \
    ElementGlossaryFilter

app_name = "main_app"

urlpatterns = [
    path('elements/filter/<id>/', ElementGlossaryFilter.as_view()),
    path('elements/<id>/<version>', ElementsGlossarySpecVersView.as_view()),
    path('elements/<id>', ElementsGlossaryCurrentVersView.as_view()),
    path('glossaries/<date>', CurrentGlossariesView.as_view()),
    path('glossaries/', GlossaryView.as_view()),
]