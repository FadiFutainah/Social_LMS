from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('Forum', ForumViewSet)
router.register('Reply', ReplyViewSet)

urlpatterns = router.urls
