from django.urls import path, include
from .views import (
    BearingListView,
    BearingDetailView,
)

app_name = 'bearings'

urlpatterns = [
    path('', BearingListView.as_view(), name='index'),
    path('<int:pk>/', BearingDetailView.as_view(), name='detail'),
]