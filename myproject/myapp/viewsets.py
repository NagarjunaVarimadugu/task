from rest_framework import viewsets
from .serializers import View_serializer
from .models import Company

class index_viewset(viewsets.ModelViewSet):

    serializer_class = View_serializer
    queryset = Company.objects.all()


