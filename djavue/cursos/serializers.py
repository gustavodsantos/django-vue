from rest_framework import serializers

from .models import Curso, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'email', 'is_staff']


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ['url', 'titulo', 'descricao', 'slug', 'order']
