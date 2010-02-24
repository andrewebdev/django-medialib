from django.contrib import admin

from medialib.models import Picture

class PictureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'is_visible', 'created_date', 'small_picture',
                    'medium_picture', 'large_picture', 'admin_thumbnail']
    list_filter = ['is_visible', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['title', 'slug']

admin.site.register(Picture, PictureAdmin)
