from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsSuperuserPermission
from .pagination import CustomPagination
from .throttling import IPThrottling
# Create your views here.



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperuserPermission]
    pagination_class= CustomPagination
    # throttle_classes=[IPThrottling]
    
    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)
    
    def get_throttles(self):
        # import pdb;pdb.set_trace()
        if self.action=='list':
            self.throttle_classes = [IPThrottling]
            self.throttle_scope='list'
        else:
            throttle_classes = []
        # return throttle_classes
        return super().get_throttles()
    
    


