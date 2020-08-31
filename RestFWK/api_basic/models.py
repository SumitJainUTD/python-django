from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)

    # def __int__(self, title, author, email):
    #     self.title = title
    #     self.author = author
    #     self.email = email

    def __str__(self):
        return self.title


