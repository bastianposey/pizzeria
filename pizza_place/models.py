from django.db import models

class pizza(models.Model):
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class topping(models.Model):
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text