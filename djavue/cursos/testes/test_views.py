import pytest
from rest_framework.test import APIClient

from djavue.cursos.models import Curso


@pytest.mark.django_db
def test_curso_list_view():
    client = APIClient()
    Curso.objects.create(titulo='Django para APIs', descricao='Aprenda Vue do zero.')
    response = client.get('/api/cursos/')
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_curso_detail_view():
    client = APIClient()
    curso = Curso.objects.create(titulo='Websockets Django', descricao='Aprenda Vue do zero.')
    response = client.get(f'/api/cursos/{curso.id}/')
    assert response.status_code == 200
    assert response.data['titulo'] == 'Websockets Django'
