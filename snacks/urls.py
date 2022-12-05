from django.urls import path
from .views import HomeView,SnackListView,SnackDetailView,SnackCreateView,SnackUpdateView,SnackDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snack_list/',SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/snack_detail', SnackDetailView.as_view(), name='snack_detail'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('<int:pk>/update_snack',SnackUpdateView.as_view(), name='update_snack'),
    path('<int:pk>/delete_snack',SnackDeleteView.as_view(), name='delete_snack')

]