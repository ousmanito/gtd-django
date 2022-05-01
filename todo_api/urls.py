from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'task', views.TaskViewSet,basename="task")
router.register(r'user', views.UserViewSet, basename='user' )

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]