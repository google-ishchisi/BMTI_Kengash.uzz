from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
 
class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name='Sarlavha', null=True, blank=True)
	img = models.CharField(verbose_name='Rasm linki', max_length=200, null=True, blank=True)

	text = RichTextField(verbose_name='Post', null=True, blank=True)
	data = models.DateTimeField(auto_now_add=True)

	author = models.CharField(verbose_name='Muallif', max_length=50, null=True, blank=True)

	def __str__(self):
		return self.title


# class Galereya(models.Model):
# 	title = models.CharField(verbose_name='Foto mavzusi', max_length=100, null=True, blank=True)
# 	body = models.CharField(max_length=100, null=True, blank=True)
# 	img = models.CharField(verbose_name='Rasm linki', max_length=200, null=True, blank=True)

# 	def __str__(self):
# 		return self.title


class Azolar(models.Model):
	img = models.CharField(verbose_name='Azoning rasmi linki', max_length=200, default='^_^')
	name = models.CharField(max_length=30, verbose_name='Azoning ismi: ', null=True, blank=True)
	text = models.CharField(max_length=50, verbose_name='Lavozimi')
	telegram = models.CharField(max_length=100, verbose_name='Telegram: ', null=True, blank=True)
	instagram = models.CharField(max_length=100, verbose_name='Instagram: ', null=True, blank=True)

	def __str__(self):
		return self.name


class Carusel(models.Model):
	img = models.CharField(max_length=200)
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=300)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	izoh = models.CharField(max_length=400)
	data = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.izoh

	def get_absolute_url(self):
		return reverse("detail")
	