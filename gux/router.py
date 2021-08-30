from rest_framework import routers
from problem_1.views import TestingsViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'testings', TestingsViewSet)

