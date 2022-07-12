from rest_framework.routers import DefaultRouter
from views import *

router = DefaultRouter()
router.register('Tag', TagViewSet)
router.register('TaggedItem', TaggedItemViewSet)
router.register('SuggestedTag', SuggestedTagViewSet)

urlpatterns = router.urls
