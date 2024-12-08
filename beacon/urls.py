from django.urls import path

from .views import PanicDispatchView, SearchBeaconListView

urlpatterns = [
    path('panic', PanicDispatchView.as_view()),
    path('search', SearchBeaconListView.as_view()),
]