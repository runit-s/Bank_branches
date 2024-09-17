from django.urls import path
from .views import BranchDetails, BankBranchDetails

urlpatterns = [
    path('branch/<str:ifsc>/', BankBranchDetails.as_view(), name='branch-detail'),
    path('branch/', BranchDetails.as_view(), name='bank-list'),
]
