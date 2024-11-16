from django.urls import path
from judesaBackend import views

urlpatterns = [
    path('api/v1/news/', views.news ),
    path('api/v1/home/', views.home),
    path('api/v1/news/latest/', views.latest_news),
    path('api/v1/new/<int:id>/', views.new_by_id),
    path('api/v1/sponsors/', views.sponsors),
    path('api/v1/categories/', views.categories),
    path('api/v1/category/<int:id>/', views.category_by_id),
    path('api/v1/matches/get_next_matches/', views.next_matches),
    # path('/api/v1/insert_new/', views.insert_new),
    # path('/api/v1/insert_tag/', views.insert_tag),
    # path('news/<str:new_id>/basic', views.getBasicNewById),
    # path('news/<str:new_id>/detailed', views.getCompleteNewById),
    # path('category/<str:category_id>', views.getCategoryById),
    # path('products/', views.loginUser),
]
