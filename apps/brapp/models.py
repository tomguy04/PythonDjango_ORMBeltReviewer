# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# class CourseManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['name']) < 6:
#             errors["name"] = "course name must be more than 5 characters"
#         if len(postData['description']) < 16:
#             errors["description"] = "description must be more than 15 characters."
#         return errors

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    # book = models.ForeignKey(Book, related_name = 'authors',  blank = True, null = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # reviews = models.ForeignKey(Review, related_name = 'books', blank = True, null = True)
    author = models.ForeignKey(Author, related_name = 'books', blank = True, null = True) 


class Review(models.Model):
    description = models.CharField(max_length=255)
    stars = models.IntegerField()
    books = models.ForeignKey(Book, related_name = 'reviews', blank = True, null = True)
    # def __str__(self):
    #     return self.description

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviews = models.ForeignKey(Review, related_name = 'users', blank = True, null = True)

    # objects = CourseManager()
    # Example: For one book, there are many reviews.
            #  So the FK goes on the reviews table (the many part).

            # one author, many book, FK in books.




