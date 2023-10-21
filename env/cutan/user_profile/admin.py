from django.contrib import admin

from .models import Profile, Country


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'created_at')
    list_display_links = ('id', 'user')
    search_fields = ('user__username',)
    list_filter = ('сountry',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)