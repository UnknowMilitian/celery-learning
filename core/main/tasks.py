# from django.core.mail import send_mail
# from core.celery import app

# from .service import send
# from .models import Contact


# @app.task
# def test_task():
#     print("Test task executed successfully")


# @app.task(bind=True)
# def send_spam_email(self, user_email):
#     try:
#         if user_email:
#             send(user_email)
#             self.logger.info(f"Email sent to {user_email}")
#         else:
#             self.logger.warning("No email provided")
#     except Exception as e:
#         self.logger.error(f"Failed to send email: {str(e)}")
#         raise e


# tasks.py
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_spam_email(user_email):
    send_mail(
        "Welcome!",
        "Thank you for registering!",
        "from@example.com",
        [user_email],
        fail_silently=False,
    )
