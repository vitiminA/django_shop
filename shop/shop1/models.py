
from django.db import models
from django.dispatch import receiver
import os

class postModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='',unique=True)  # Thay đổi đường dẫn tại đây
    body = models.TextField()

    def __str__(self):
        return self.title

@receiver(models.signals.post_delete, sender=postModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Xóa file khỏi hệ thống file khi đối tượng được xóa khỏi database.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=postModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Xóa file cũ khi đối tượng có một file mới được gán.
    """
    if not instance.pk:
        return False

    try:
        old_file = postModel.objects.get(pk=instance.pk).image
    except postModel.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    
    