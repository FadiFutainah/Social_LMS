from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('VotedItem', VotedItemViewSet)

urlpatterns = router.urls
