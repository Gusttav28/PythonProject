from django.db import models

# Create your models here.

# This models is to register the author of the books
class Author(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    

# This model class is connected to the class model Author by the ForeignKey and is to register book on the DB
# The way the this one can connect is because that ForeignKey, this one expect to have two different parametters
# the first one will refer to the the model in where the model is going to shate the information
# And the second one refer to the behavior when the referenced object is going to be deleted, this are some common options:
# models.CASCADE: Deletes the object containing the foreign key when the referenced object is deleted.
# models.PROTECT: Prevents deletion of the referenced object if there are still foreign key references to it.
# models.SET_NULL: Sets the foreign key field to NULL when the referenced object is deleted (requires null=True on the field).
# models.SET_DEFAULT: Sets the foreign key field to a default value when the referenced object is deleted (requires default on the field).
# models.DO_NOTHING: Does nothing when the referenced object is deleted, potentially leading to data inconsistency.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE) 
    joined_at = models.DateTimeField(auto_now_add=True)
    

# This class over here is to register the members of the books store
class Member(models.Model):
    cx_name = models.CharField(max_length=200)
    cx_lastName = models.CharField(max_length=200)
    cx_email = models.EmailField(max_length=254)
    cx_phoneNumber = models.IntegerField()
    

# And this model class has information of a loan member that gets a book from the storex
class loan(models.Model):
    book_title = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.ForeignKey(Member, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()
    order_createdAt = models.DateTimeField(auto_now_add=True)
    