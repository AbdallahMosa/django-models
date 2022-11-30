from django.urls import path
from .views import HomePage,SnacksListView


urlpatterns =[

    path('',HomePage.as_view(), name='home'),
    path('snacks',SnacksListView.as_view(), name='snacks')
]