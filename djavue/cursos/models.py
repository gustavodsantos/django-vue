from django.db import models
from django_min_custom_user.models import MinAbstractUser
from ordered_model.models import OrderedModel


class User(MinAbstractUser):
    pass


class Curso(OrderedModel):
    titulo = models.CharField(max_length=64)
    descricao = models.TextField(null=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo
