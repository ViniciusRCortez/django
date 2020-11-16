from django.db import models


class Empregado(models.Model):
    e_id = models.TextField(max_length=20)
    e_name = models.TextField(max_length=100)
    e_email = models.EmailField()
    e_contact = models.TextField(max_length=20)

    class Meta:
        db_table = 'Empregado'
