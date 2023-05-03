# from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from studies.models import Content, Subject
from utils.converter import string_to_list


@receiver(post_save, sender=Subject)
def content_create(sender, instance, created, *args, **kwargs):
    if created:
        content_list = string_to_list(instance.contents, spliting=' - ')

        if content_list:
            for value in content_list:
                content = Content.objects.create(
                    name=value,
                    subject=instance
                )
                content.full_clean()
                content.save()


@receiver(pre_save, sender=Subject)
def content_update(sender, instance, *args, **kwargs):
    old_instance = Content.objects.filter(subject=instance)
    subject = Subject.objects.filter(pk=instance.pk).first()

    if old_instance:
        old_instance.delete()

    if subject:
        content_list = string_to_list(instance.contents, spliting=' - ')

        if content_list:
            for value in content_list:
                content = Content.objects.create(
                    name=value,
                    subject=instance
                )
                content.full_clean()
                content.save()
