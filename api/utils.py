from django.core.mail import send_mail
from django.conf import settings

from accounts.models import User


def send_confirmation_email(user: User, token: str, uid: str):
    """
    Send email with confirmaion link to user.
    """

    confirmation_link =link = f"{settings.BACKEND_HOST}api/accounts/confirm-email/{uid}/{token}/"
    subject = "Confirm Your Email Address"
    message = f"Click the link to confirm your email: {confirmation_link}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

