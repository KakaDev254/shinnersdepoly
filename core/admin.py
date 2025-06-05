from django.contrib import admin
from .models import Client, GalleryItem, TeamBuildingItem, CharityEvent, Testimonial

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(GalleryItem)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(TeamBuildingItem)
class TeamBuildingAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(CharityEvent)
class PastEventAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "approved", "submitted_at")
    list_filter = ("approved", "submitted_at")
    actions = ["approve_selected"]

    def approve_selected(self, request, queryset):
        queryset.update(approved=True)
    approve_selected.short_description = "Approve selected testimonials"
