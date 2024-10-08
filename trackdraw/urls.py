from django.urls import path
from .views import DrawingListCreateView, DrawingRetrieveView

urlpatterns = [
    # List all drawings and create a new drawing
    path('api/drawings/', DrawingListCreateView.as_view(), name='drawing-list-create'),

    # Retrieve a specific drawing by ID
    path('api/drawings/<int:pk>/', DrawingRetrieveView.as_view(), name='drawing-retrieve'),
]
