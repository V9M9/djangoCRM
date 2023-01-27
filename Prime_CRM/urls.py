from django.urls import path
from .views import index, ClientAddView, ClientDeleteView, ClientUpdateView, ContractView

urlpatterns = [
    path('', index, name='index'),
    path('add', ClientAddView.as_view(), name="add-client"),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name="edit-client"),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name="delete-client"),
    path('contracts/<int:pk>', ContractView, name="show-contracts"),
]

