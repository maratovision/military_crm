from django.contrib.auth.models import User
from django.core.mail import EmailMessage



def mailing(username):
    """This mailing is for applying new employees"""
    users = User.objects.filter(is_superuser=True)
    email_list = []
    for user in users:
        email_list.append(user.email)
    subject = 'Hello there!'
    body = f'User with name {username} registered in Military CRM database, please checke his account!'
    email = EmailMessage(subject=subject, body=body, to=email_list)
    email.send()
