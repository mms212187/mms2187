from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Product
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Product)
def send_mail_on_product_save(sender, instance, created, **kwargs):

    if created:
        action = "добавлен"
    else:
        action = "изменен"


    if instance.quantity == 0:
        send_mail(
            subject=f"Товар {instance.name} закончился на складе",
            message=f"Товар {instance.name} {action} и закончился на складе. Срочно пополните инвентарь!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['mms2107@gmail.com'],
            fail_silently=False,
        )
    else:
        send_mail(
            subject=f"Товар {instance.name} был {action}",
            message=f"Товар {instance.name} был {action} на складе. Текущее количество: {instance.quantity}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['mms2107@gmail.com'],
            fail_silently=False,
        )


@receiver(pre_delete, sender=Product)
def send_mail_on_product_delete(sender, instance, **kwargs):

    send_mail(
        subject=f"Товар {instance.name} удален из базы данных",
        message=f"Товар {instance.name} был удален из базы данных.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['mms2107@gmail.com'],
        fail_silently=False,
    )
