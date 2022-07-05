from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddName.as_view()),
    path('names/', views.NamesView.as_view()),
    path('<int:id>', views.Name.as_view()),
]