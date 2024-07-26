from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, register_customer,login_page,login_customer,book_table_page

router = DefaultRouter()
router.register(r'customers/', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
    
    # path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),
    # path('questions/update-latest-version/<int:pk>/', QuestionViewSet.as_view({'patch': 'update_latest_version'}), name='update-latest-version'),    path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),

    path('customers/', CustomerViewSet.as_view({'get': 'list'}), name='customers-list'),
    path('customers/create/', CustomerViewSet.as_view({'post': 'create'}), name='customer-create'),
    path('customer/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve'}), name='customer-retrieve'),
    path('customer/register/', register_customer, name="customer-register" ),
    path('customer/<int:pk>/', CustomerViewSet.as_view({'delete': 'delete'}), name='customer-delete'),
    path('customer/update/<int:pk>/', CustomerViewSet.as_view({'put': 'update'}), name='Customer-update'),
     path('customer/loginpage/', login_page, name="login-page" ),
    path('customer/booktable/',book_table_page, name="book-tablepage" ),
 path('customer/login/',login_customer, name="customer-login" ),


]
