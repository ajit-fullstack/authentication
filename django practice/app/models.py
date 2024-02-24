from django.db.models import Model, CharField

# Create your models here.
class Todos(Model):
    todo = CharField(max_length=500)
    