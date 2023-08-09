from rest_framework import routers
from .api import ProjectViewSet, AddressViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls
