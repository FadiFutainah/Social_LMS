from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('Page', PageViewSet)
router.register('PageReferencesFeature', PageReferencesFeatureViewSet)
router.register('PageReference', PageReferenceViewSet)
router.register('Feature', FeatureViewSet)
router.register('Content', ContentViewSet)
router.register('Feedback', FeedbackViewSet)
router.register('FinishedPage', FinishedPageViewSet)

urlpatterns = router.urls
