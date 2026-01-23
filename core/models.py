from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="news/")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title




class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/")
    description = models.TextField()
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    discount_price = models.DecimalField(max_digits=5,decimal_places=2)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name='product',db_index=True,null=True,blank=True)

    def __str__(self):
        return self.title

class Club(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="news/")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    description = models.TextField()

    def __str__(self):
        return self.title
class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="event/")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Slider(models.Model):
    image = models.ImageField(upload_to="slide/")
    description = models.TextField()

    def __str__(self):
        return self.description

class Book(models.Model):
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    series = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Toy(models.Model):
    themes = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.themes

class Technique(models.Model):
    themes = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.themes






