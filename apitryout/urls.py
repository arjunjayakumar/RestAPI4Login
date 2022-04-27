from django.urls import path
from .views import showall, showselected

urlpatterns = [
    path('profiles',showall.as_view()),
    path('profiles/<str:key>',showselected.as_view())
]