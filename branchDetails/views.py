from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import BankBranch
from .serializers import BankBranchSerializer

class BranchDetails(generics.ListAPIView):
    serializer_class = BankBranchSerializer

    def get_queryset(self):
        branch_name = self.request.query_params.get('branch', None)
        if branch_name is None:
            raise NotFound("Branch name is required.")
        
        queryset = BankBranch.objects.filter(branch__iexact=branch_name)
        if not queryset.exists():
            raise NotFound("Branch with the given name not found.")
        
        return queryset


class BankBranchDetails(generics.RetrieveAPIView):
    queryset = BankBranch.objects.all()
    serializer_class = BankBranchSerializer
    lookup_field = 'ifsc'
    def get(self, request, *args, **kwargs):
        ifsc_code = kwargs.get('ifsc')
        try:
            branch = BankBranch.objects.get(ifsc=ifsc_code)
            serializer = self.get_serializer(branch)
            return Response(serializer.data)
        except BankBranch.DoesNotExist:
            raise NotFound("Branch with the given IFSC code not found.")