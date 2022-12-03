from django.urls import path
from .views import HomePage,SnacksListView,SnackDetail


urlpatterns =[

    path('',HomePage.as_view(), name='home'),
    path('snacks',SnacksListView.as_view(), name='snacks'),
    path('detail/<pk>',SnackDetail.as_view(), name='detail')

]