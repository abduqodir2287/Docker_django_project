from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return f"Username {self.username} Password {self.password} Data {self.time}"

class Compose(models.Model):
    name = models.CharField(max_length=50)
    data = models.TimeField(auto_now=True)

    def __str__(self):
        return f"Name {self.name} Time {self.data}"

