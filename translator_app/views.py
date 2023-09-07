"""This file contains class based views for translate model."""

from rest_framework.generics import ListCreateAPIView
from translator_app.models import Translate
from translator_app.serializers import TranslateSerializer


class TranslateView(ListCreateAPIView):
    """
    This view will create and list translate instance.
    """
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer
