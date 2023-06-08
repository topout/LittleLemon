from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'table', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]