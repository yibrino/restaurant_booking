from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TableListViewSet

router = DefaultRouter()
router.register(r'tables/', TableListViewSet, basename='table')

urlpatterns = [
    path('', include(router.urls)),
    
    # path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),
    # path('questions/update-latest-version/<int:pk>/', QuestionViewSet.as_view({'patch': 'update_latest_version'}), name='update-latest-version'),    path('questions/create', QuestionViewSet.as_view({'post': 'create'}), name='question-create'),

    path('tables/', TableListViewSet.as_view({'get': 'list'}), name='tables-list'),
    path('tables/create/', TableListViewSet.as_view({'post': 'create'}), name='table-create'),
    path('table/<int:pk>/', TableListViewSet.as_view({'get': 'retrieve'}), name='table-retrieve'),
    path('tables/update/<int:pk>/', TableListViewSet.as_view({'put': 'update'}), name='booktable-update'),
    path('tables/<int:pk>/', TableListViewSet.as_view({'delete': 'delete'}), name='booktable-delete'),
#     path('customer/register/', register_customer, name="customer-register" ),
#      path('customer/loginpage/', login_page, name="login-page" ),
#     path('customer/tablepage/',table_page, name="tablepage" ),
#  path('customer/login/',login_customer, name="customer-login" ),


]
