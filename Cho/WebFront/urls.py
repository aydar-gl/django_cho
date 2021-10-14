from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/', views.category_view, name='category'),
    path('menu/<slug:slug>/', views.Menu_view.as_view(), name='menu'),
    path('menu/<slug:category_slug>/<slug:dish_slug>/', views.adding, name='dish'),
    path('basket/', views.basket_view, name='basket'),
    path('basket_clear/', views.clear_basket, name='clear_basket'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)