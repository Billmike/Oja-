from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
	"""Class to handle the uploads by farmers"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	product_name = models.CharField(max_length = 200)
	product_description = models.TextField()
	slug = models.SlugField(unique=True)
	product_price = models.FloatField()
	product_image = models.ImageField(null=True, blank=True)
	time_updated = models.DateTimeField(auto_now= True)
	time_posted = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.product_name

	def get_absolute_url(self):
		#return reverse("posts:detail", kwargs={"slug":self.slug})
		return "/posts/%s/"  %(self.id)

def create_slug(instance, new_slug=None):
	slug = slugify(instance.product_name) #turn the tile into a slug
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id") #Check to see if slug already exists
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug #return slug if it doesn't exist


def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
		
pre_save.connect(pre_save_post_receiver, sender=Post)

class FarmerProfile(models.Model):
	"""Class that creates the profile of farmers"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user_name = models.CharField(max_length=10, default="mike")
	farm_produce = models.CharField(max_length=200)
	phone_number = models.IntegerField()
	business_address = models.CharField(max_length=200)
	email_address = models.EmailField(max_length=200)

	def __unicode__(self):
		return self.first_name + " " + self.last_name


class SendQuotes(models.Model):
	"""docstring for SendQuotes"""
	name_of_product = models.CharField(max_length=200)
	qty_of_product = models.FloatField()
	delivery_address = models.CharField(max_length = 500)
	phone_number = models.IntegerField()

	def get_absolute_url(self):
		#return reverse("posts:detail", kwargs={"slug":self.slug})
		return "/posts/%s/"  %(self.id)
		
