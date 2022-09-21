from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    # print(created)
    if created:
        UserProfile.objects.create(user=instance)
        # print('Profile created')
    else:
        try:
            # Si existe modifique y grabe
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the user profile if not exists
            UserProfile.objects.create(user=instance)
            # print('El perfil no existía pero hemos creado uno')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
# post_save.connect(post_save_create_profile_receiver, sender=User)