from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150, blank=True)
    def get_full_name(self):
        return f"{self.name} "
    def __str__(self):
        return self.get_full_name();
    pass
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name="books") # cascade means delete here if author is deleted
    is_bestseller = models.BooleanField(default = False)
    count_in_library = models.IntegerField(default =10 , blank=True)
    slug = models.SlugField(default="",blank=True,editable=True,null=False,db_index=True) #here db_index true makes it a bit more efiicient to search as we oftenly use slugs
    def get_full_name(self):
        return f"{self.title} ({self.author})"
    def __str__(self):
        return self.get_full_name();
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    pass

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email