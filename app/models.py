from django.db import models

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=1000, null=True)
    content= models.TextField(null=True)
    date = models.CharField(max_length=20)
    writer = models.CharField(max_length=200)
    href = models.CharField(max_length=1000, null=True)
    title_noun = models.CharField(max_length=5000, null=True)
<<<<<<< HEAD
    채용  = models.IntegerField(null = True)
    합격자  = models.IntegerField(null = True)
    의회  = models.IntegerField(null = True)
=======
    # content_noun = models.TextField(null=True)
    채용  = models.IntegerField(null = True)
    합격자  = models.IntegerField(null = True)
    의회  = models.IntegerField(null = True)
    행사  = models.IntegerField(null = True)
>>>>>>> c9dc42488970bd77d009e4a706fab4731398f6b8
    관람 = models.IntegerField(null = True)
    대회 = models.IntegerField(null = True)
    의견수렴  = models.IntegerField(null = True)
    업체  = models.IntegerField(null = True)
<<<<<<< HEAD
=======
    전체교육  = models.IntegerField(null = True)
>>>>>>> c9dc42488970bd77d009e4a706fab4731398f6b8
    전문교육  = models.IntegerField(null = True)
    청소년  = models.IntegerField(null = True)
    주민자치 = models.IntegerField(null = True)
class InverseTable(models.Model):
    word = models.CharField(max_length=100, null=True)
    frequency = models.IntegerField(null=True)
    location = models.TextField(null=True,max_length=200000)
class ContentInverseTable(models.Model):
    word = models.CharField(max_length=100, null=True)
    frequency = models.IntegerField(null=True)
    location = models.TextField(null=True,max_length=200000)