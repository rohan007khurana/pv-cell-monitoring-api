from django.urls import path
from . import views

urlpatterns = [
    path('api/readings/', views.ReadingList.as_view()),
    path('api/readings/<int:pk>/', views.ReadingDetail.as_view())
]