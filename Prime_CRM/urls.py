from django.urls import path
from .views import index, ClientAddView, ClientDeleteView, ClientUpdateView, ContractView, ContractUpdateView, ContractAddView, ContractDeleteView, ContractsAllView

urlpatterns = [
    path('', index, name='index'),
    path('add_client', ClientAddView.as_view(), name="add-client"),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name="edit-client"),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name="delete-client"),
    path('contracts/<int:pk>', ContractView, name="show-contracts"),
    path('edit_contract/<int:pk>', ContractUpdateView.as_view(), name="edit-contract"),
    path('contracts/add_contract/<int:pk>', ContractAddView.as_view(), name="add-contract"),
    path('delete_contract/<int:pk>', ContractDeleteView.as_view(), name="del-contract"),
    path('contracts_all', ContractsAllView, name="Contracts_all")
]

