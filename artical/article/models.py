from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User (models.Model):
	user_name=models.CharField(max_length=255)
	user_email=models.CharField(max_length=255)
	user_password=models.CharField(max_length=20)
	user_img=models.CharField(max_length=255)
	user_type=models.CharField(max_length=20)
	user_status=models.BooleanField(default=1)
	user_secret_quation=models.CharField(max_length=255)
	user_secret_answer=models.CharField(max_length=255)

	def __str__(self):
		 return self.user_name

class Article(models.Model):
	art_title=models.CharField(max_length=255)
	art_content=models.TextField()
	art_img=models.CharField(max_length=255)
	art_status=models.CharField(max_length=50)
	art_publish_date=models.DateTimeField(auto_now_add=True)
	art_number_views=models.IntegerField(default=0)
	art_user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		 return self.art_title

class keywords(models.Model):
	keyword_name=models.CharField(max_length=255)
	keyword_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	def __str__(self):
		 return self.keyword_name

class Comment(models.Model):
	Comment_content=models.TextField()
	Comment_status=models.BooleanField(default=1)
	Comment_parent_id=models.IntegerField()
	Comment_user_like=models.ManyToManyField(User)
	Comment_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	def __str__(self):
		 return self.Comment_content

class  Banwords(models.Model):
	banword_name=models.CharField(max_length=255)
	def __str__(self):
		 return self.banword_name

class Emotions(models.Model):
	emotion_letter=models.CharField(max_length=255)
	emotion_img=models.CharField(max_length=255)
	def __str__(self):
		 return self.emotion_letter




