from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    amount_left = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Review(models.Model):
    RATING = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5)
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    author = models.CharField(max_length=63)
    text = models.TextField()
    rating = models.CharField(max_length=2, choices=RATING)