# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/v1/risk-type', views.RiskTypeViewSet)

router.register(r'api/v1/field-value',             views.FieldValueViewSet);
router.register(r'api/v1/field',                   views.FieldViewSet);
router.register(r'api/v1/risk-field',              views.RiskFieldViewSet);
router.register(r'api/v1/risk-type-default-field', views.RiskTypeDefaultFieldViewSet);
router.register(r'api/v1/risk-type',               views.RiskTypeViewSet);
router.register(r'api/v1/risk',                    views.RiskViewSet);

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]