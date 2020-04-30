from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import m2m_changed, pre_save, post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_signup_email(sender, instance=None, created=False, **kwargs):
    print('User signal triggered')
    if created:
        print('User was created. Sending mail')
        send_mail(
            'Welcome to my website',
            f'Hello {instance.username}',
            'from@myaddress.com',
            [instance.email],
        )
    else:
        print('User wasnt created')
