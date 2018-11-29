from django.db import models

class Clothing(models.Model):
    type = models.CharField(max_length = 100, blank=False)
    price = models.IntegerField()
    weatherChoices = (
        ('WARM', 'This piece of clothing can be worn in colder temperatures'),
        ('MEDIUM', 'This piece of clothing can be worn in any temperature'),
        ('COOL', 'This piece of clothing can be worn in warmer temperatures')
    )
    color = models.CharField(max_length=20, blank=True)
    size = models.CharField(max_length=20, blank=True)
    weather = models.CharField(max_length=10, choices=weatherChoices, default="SOLD")    #available, sold, restocking
    
    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)

class Shirts(Clothing):
    pass

class Pants(Clothing):
    pass

class Shoes(Clothing):
    pass