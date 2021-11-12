from django.urls import path

from .views import WriterInfoView


urlpatterns = [
    path('', WriterInfoView.as_view(),)
]
