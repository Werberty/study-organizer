from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from studies.models import Content, Subject
from utils.converter import string_to_list


@receiver(post_save, sender=Subject)
def content_create(sender, instance, created, *args, **kwargs):
    if created:
        content_list = string_to_list(instance.contents, spliting=' - ')

        for value in content_list:
            content = Content.objects.create(
                name=value,
                subject=instance
            )
            content.save()


@receiver(pre_save, sender=Subject)
def content_update(sender, instance, *args, **kwargs):
    contents = Content.objects.filter(subject=instance)

    if contents:
        contents.delete()

    content_list = string_to_list(instance.contents, spliting=' - ')

    for value in content_list:
        content = Content.objects.create(
            name=value,
            subject=instance
        )
        content.save()
