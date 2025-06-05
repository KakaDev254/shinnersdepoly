from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="client_logos/")
    

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    """Any photo shown in the normal gallery grid."""
    title       = models.CharField(max_length=120)
    image       = models.ImageField(upload_to="gallery/")
      # for manual sorting
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ "-created_at"]

    def __str__(self):
        return self.title

class TeamBuildingItem(models.Model):
    """Photos that appear in the Team-Building section."""
    title       = models.CharField(max_length=120)
    image       = models.ImageField(upload_to="team_building/")
    

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title    

class CharityEvent(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='past_events/')

    def __str__(self):
        return self.title    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="e.g. Wedding Client")
    message = models.TextField()
    approved = models.BooleanField(default=False)  # Only show approved testimonials
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}" 