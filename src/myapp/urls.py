from .views import  CategoryDetail, CategoryList
from django.urls import path

urlpatterns = [
    path('', CategoryList.as_view(), name='category'),
    path('<category>', CategoryDetail.as_view(), name='category'),
]
