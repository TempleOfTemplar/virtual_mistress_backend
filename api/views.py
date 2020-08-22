from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from . import serializers
from .filters import SuggestionFilter
from .models import Suggestion, Deviation, Item


class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = serializers.SuggestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('categories', 'toys')
    lookup_field = 'slug'
    filterset_class = SuggestionFilter


class CurrentUserView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)


class DeviationViewSet(viewsets.ModelViewSet):
    queryset = Deviation.objects.all()
    serializer_class = serializers.DeviationSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
    lookup_field = 'slug'
