import pytest
from rest_framework.test import APIRequestFactory

from djavue.cursos.models import Curso
from djavue.cursos.serializers import CursoSerializer


@pytest.mark.django_db
def test_curso_serializer():
    curso = Curso.objects.create(titulo='Vue para Iniciantes', descricao='Aprenda Vue do zero.')
    factory = APIRequestFactory()
    request = factory.get('/')  # Cria uma requisição GET fictícia
    serializer = CursoSerializer(curso, context={'request': request})  # Adiciona o contexto da requisição
    data = serializer.data
    assert data['titulo'] == 'Vue para Iniciantes'
    assert data['descricao'] == 'Aprenda Vue do zero.'
    assert 'url' in data
    assert 'order' in data


@pytest.mark.django_db
def test_curso_serializer_validation():
    data = {'titulo': 'React Native', 'descricao': 'Aprenda Vue do zero.'}
    serializer = CursoSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()
    assert Curso.objects.count() == 1
