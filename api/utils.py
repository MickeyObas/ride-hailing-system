from django.core.mail import send_mail
from django.conf import settings

from accounts.models import User

import re 

def send_confirmation_email(user: User, token: str, uid: str):
    """
    Send email with confirmaion link to user.
    """

    confirmation_link =link = f"{settings.BACKEND_HOST}api/accounts/confirm-email/{uid}/{token}/"
    subject = "Confirm Your Email Address"
    message = f"Click the link to confirm your email: {confirmation_link}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None