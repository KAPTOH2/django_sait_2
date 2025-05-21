from django.contrib import admin
from .models import *

admin.site.register(AbcModel)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_title', 'item_nav', 'item_nav_position', 'item_content', 'item_current_date']
    list_display_links = ['id','item_title', ]
    list_editable = ['item_nav', 'item_nav_position',]
    search_fields = ['item_content', 'item_nav']
    list_filter = ['item_title', 'item_nav']
    list_per_page = 15

