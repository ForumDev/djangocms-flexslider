from django.contrib import admin
from flexslider.models import Slide
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.

class FlexSliderAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Slide, FlexSliderAdmin)