from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.URLField()
    c_id = models.CharField(max_length=50)
    c_type = models.CharField(max_length=50)
    faction = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    attack = models.PositiveIntegerField()
    health = models.PositiveIntegerField(default=10)
    text = models.TextField(max_length=300)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.c_type}"

class Deck(models.Model):
    name = models.CharField(max_length=200)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return f"{self.name}"

    