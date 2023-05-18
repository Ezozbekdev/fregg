from django.db import models


class Service(models.Model):
    img = models.ImageField(upload_to="img/")
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    img = models.ImageField(upload_to="img/testimonial/")
    name = models.CharField(max_length=160)
    dg = models.CharField(max_length=120)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class About(models.Model):
    text = models.TextField()
