from django.urls import path
from app.views import index, CarView

urlpatterns = [
    #path('', index, name='index'),
    path('', CarView.as_view(), name='index'),
]