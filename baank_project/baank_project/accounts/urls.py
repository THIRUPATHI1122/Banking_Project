from django .urls import path
from .views import *

urlpatterns = [

    path('',account_list,name='account_list'),
    path('account/create/',account_create,name = 'account_create'),
    path('account/update/<int:pk>/',account_update,name='account_update'),
    path('account/delete/<int:pk>',account_delete,name='account_delete'),
    path('account/transfer/',transfer_view,name= 'transfer'),
    path('account/history/',transfer_history,name='transfer_history'),

]