from django.db import models


class url_table(models.Model):
    shorten_url = models.CharField(max_length=30)
    url = models.TextField(primary_key=True)

