from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Назва посту")
    smallDescriptions = models.TextField(verbose_name="Короткий опис максимум 30 символів")
    content = models.TextField(verbose_name="Основний вміст посту")
    image = models.ImageField()
    
    def __str__(self):
        return f"{self.name}, {self.id}"


def getNews():
    return reversed(list(News.objects.all()))


def getNewsById(id):
    print(News.objects.all().filter(id=id))
    return News.objects.all().filter(id=id)