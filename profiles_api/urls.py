from django.urls import path, include

from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
# 'profile' don't need bse_name 
# because it has the queryset which will specify the base_name

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]
