from .models import Project, Address
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = AddressSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


