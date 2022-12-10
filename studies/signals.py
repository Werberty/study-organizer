from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from studies.models import Content, Subject


def string_to_list(content_list):
    content_list = content_list.split(' - ')
    list_content = []
    for content in content_list:
        list_content.append(content.strip())

    return list_content


@receiver(post_save, sender=Subject)
def content_create(sender, instance, created, *args, **kwargs):
    if created:
        content_list = string_to_list(instance.contents)

        for value in content_list:
            content = Content.objects.create(
                name=value,
                subject=instance
            )
            content.save()


@receiver(pre_save, sender=Subject)
def content_update(sender, instance, *args, **kwargs):
    contents = Content.objects.filter(subject=instance)

    print(contents)
    if contents:
        contents.delete()

    content_list = string_to_list(instance.contents)

    for value in content_list:
        content = Content.objects.create(
            name=value,
            subject=instance
        )
        content.save()
