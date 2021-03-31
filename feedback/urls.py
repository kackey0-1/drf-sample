from django.conf.urls import url

from .views import FeedbackView

urlpatterns = [
    url('', FeedbackView.as_view(), name="feedback"),
]
