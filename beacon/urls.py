from django.urls import path

from .views import (
    PanicDispatchView, SearchBeaconListView,
    GlobalPanicDispatchView, ChangePinView
)

urlpatterns = [
    path('panic', PanicDispatchView.as_view()),
    path('search', SearchBeaconListView.as_view()),
    path('security-pin', ChangePinView.as_view()),
    path('panic/global', GlobalPanicDispatchView.as_view())
]