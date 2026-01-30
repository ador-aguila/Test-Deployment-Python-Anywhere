# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Student



@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(
            user=instance,
            name=instance.username,  # You can use instance.username if full_name is blank
            email=instance.email
        )
        print("✅ Student profile created!")