from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Suggestion, Item, Deviation, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', "first_name", "last_name", "avatar", "birth_date", "categories", "toys")


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        lookup_field = 'slug'
        fields = ('title',
                  'description',
                  'body',
                  'cover',
                  'pub_date',
                  'author',
                  'categories',
                  'toys',
                  'slug'
                  )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        lookup_field = 'slug'
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'average_price',
                  'slug'
                  )


class DeviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deviation
        lookup_field = 'slug'
        fields = ('id',
                  'title',
                  'cover'
                  )

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ('id',
#                   'name',
#                   'email')
