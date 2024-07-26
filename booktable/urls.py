from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookTableViewSet

router = DefaultRouter()
router.register(r'booktables/', BookTableViewSet, basename='booktable')

urlpatterns = [
    path('', include(router.urls)),
    
    # path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),
    # path('questions/update-latest-version/<int:pk>/', QuestionViewSet.as_view({'patch': 'update_latest_version'}), name='update-latest-version'),    path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),

    path('booktables/', BookTableViewSet.as_view({'get': 'list'}), name='booktables-list'),
    path('booktable/create/', BookTableViewSet.as_view({'post': 'create'}), name='booktable-create'),
    path('booktable/<int:pk>/', BookTableViewSet.as_view({'get': 'retrieve'}), name='booktable-retrieve'),
    path('booktable/update/<int:pk>/', BookTableViewSet.as_view({'put': 'update'}), name='booktable-update'),
    path('booktable/<int:pk>/', BookTableViewSet.as_view({'delete': 'delete'}), name='booktable-delete'),
  
# path('customer/register/', register_customer, name="customer-register" ),
#      path('customer/loginpage/', login_page, name="login-page" ),
#     path('customer/tablepage/',table_page, name="tablepage" ),
#  path('customer/login/',login_customer, name="customer-login" ),


]
