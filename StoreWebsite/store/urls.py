from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import register_user, user_login, user_logout

router = DefaultRouter()
#router.register('Customer', CustomersViewSets, basename='Customer')
router.register('Product', ProductsViewSets, basename='Product')
router.register('Orders', OrdersViewSets, basename='Orders')
router.register('Reviews', ReviewsViewSets, basename='Reviews')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
