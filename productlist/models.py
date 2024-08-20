from django.db import models
from django.utils.timezone import now
from owner.models import Productowner

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    ownerr = models.ForeignKey(Productowner, on_delete=models.DO_NOTHING)

    
    def __str__(self):
        return self.title