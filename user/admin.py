from django.contrib import admin
from  .models import *


# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Message')

admin.site.register(contactus,contactusAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic')

admin.site.register(slider,sliderAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic','gdate')

admin.site.register(igallery,igalleryAdmin)

class ncategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category','cpic','cdate')

admin.site.register(ncategory,ncategoryAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','cpic','cdate')

admin.site.register(city,cityAdmin)

class trendingAdmin(admin.ModelAdmin):
    list_display = ('id','thead','tpic','tdate','tdes')

admin.site.register(trending,trendingAdmin)

class mynewsAdmin(admin.ModelAdmin):
    list_display = ('id','ntitle','npic','ndate','ndes','nhead','ncategory','ncity')

admin.site.register(mynews,mynewsAdmin)

class topheadlineAdmin(admin.ModelAdmin):
    list_display = ('id','ttitle')
admin.site.register(topheadline,topheadlineAdmin)

class videonewsAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vhead','vdes','vdate','vcity','vcategory')
admin.site.register(videonews,videonewsAdmin)
