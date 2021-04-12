from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class RiviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    list_dispaly = ("__str__", "rating_average")
