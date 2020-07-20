from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'eyesion'

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'homepage'),
    path('list/', views.ImageListView.as_view(), name= 'list'),
    path('upload/', views.ImageUploadView.as_view(), name= 'upload'),
    path('search/result/', views.SearchResultsView.as_view(), name= 'search-results'),
    path('<int:id>/details/', views.ImageDetailView.as_view(), name= 'details'),
    path('<int:id>/predict/', views.PredictView.as_view(), name= 'predict'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()