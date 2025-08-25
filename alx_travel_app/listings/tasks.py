from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_confirmation_email(user_email, booking_id, amount):
    """
    Send payment confirmation email asynchronously.
    """
    subject = "Payment Confirmation"
    message = f"""
    Dear Customer,

    Your payment for Booking #{booking_id} was successful.
    Amount Paid: {amount} KES

    Thank you for using our service!
    """

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])

    return f"Payment confirmation email sent to {user_email}"