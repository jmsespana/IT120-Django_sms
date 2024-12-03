from django.db import models
from twilio.rest import Client
from django.conf import settings


# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def send_sms(self, body):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=settings.TWILIO_TO_PHONE_NUMBER
        )
        print(f"Message sent with SID: {message.sid}")

    def save(self, *args, **kwargs):
        if self.score >= 70:
            body = f"Congratulations {self.name}, your score is {self.score}"
        else:
            body = f"Sorry {self.name}, your score is {self.score}. Try again"
        
        # Send the SMS
        self.send_sms(body)

        # Save the model instance
        return super().save(*args, **kwargs)
