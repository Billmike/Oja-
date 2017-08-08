from django.contrib import admin

# Register your models here.
from .models import Post, FarmerProfile

class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ["__unicode__", "time_posted", "time_updated"]
	list_filter = ["product_name", "product_price"]
	class Meta:
		model = Post
			


admin.site.register(Post, PostAdmin)
admin.site.register(FarmerProfile)