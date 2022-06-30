from django.urls import path
from .views import ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView, ClientCreateView
# List of fuction views (client_list, client_detail,)

app_name = "clients"

urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('<int:pk>/update/',ClientUpdateView.as_view(), name="client-update"),
    path('<int:pk>/delete/',ClientDeleteView.as_view(), name="client-delete"),
    path('create/', ClientCreateView.as_view(), name="client-creation")]
