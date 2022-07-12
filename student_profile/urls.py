from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('Profile', ProfileViewSet)
router.register('Contact', ContactViewSet)
router.register('Mark', MarkViewSet)
router.register('Experience', ExperienceViewSet)
router.register('Project', ProjectViewSet)
router.register('Membership', MembershipViewSet)

urlpatterns = router.urls
