from django.contrib import admin
from . models import Post, Category, Tags, CustomUser

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'bio')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)



