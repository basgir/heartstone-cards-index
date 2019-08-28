from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.all_cards, name='all_cards'),
    path('cards/<int:id>', views.get_card, name='get_card'),
]