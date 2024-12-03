# IT120-SMS Application (SnapSMS)

## Overview:
• Our IT120-SMS Application is a user-friendly web tool built with Django that lets you send SMS messages easily. It uses Twilio, a reliable messaging service, to send texts from a Twilio phone number to your recipient's mobile number. With this app, you can enter your phone number, choose a greeting, add the recipient’s name, write a custom message, and send it instantly.

## Key Features:
• Send SMS directly from the platform using Twilio's robust API for seamless and efficient message delivery.

• Easily manage and customize messages using the clean and user-friendly Django admin interface.

• Receive instant alerts and feedback for successful or failed message deliveries, ensuring transparency and troubleshooting.

• Manage user data, scores, and other dynamic fields directly within the admin dashboard.

• Add, edit, and save multiple messages quickly using built-in Django admin features like "Save and add another."

• Fully responsive and easy to use, even on smaller devices.

## Technologies Used:
• Backend Framework: Django 5.1.3

• Programming Language: Python 3.12.1

• Messaging Platform: Twilio API for SMS functionality

• Frontend: HTML and CSS for responsive and polished UI

## Setup and Usage Instructions:
Get started with SnapSMS on your local system by following these steps:

• Clone the Repository: git clone https://github.com/jmsespana/IT-120-SMS

• Open the cloned folder in your code editor (Visual Code)

• Launch the Django development server by typing: python manage.py runserver

• (Navigate to http://127.0.0.1:8000/ in your browser to start using SnapSMS.)

## Configuring Twilio:
To enable SMS functionality, you'll need a Twilio account. Follow these steps to configure your setup:

1. Sign Up on Twilio: Register at Twilio's Website if you don't already have an account.

2. Obtain Credentials: Retrieve your Account SID, Auth Token, and a Twilio phone number from the Twilio Console.

3. Update Credentials: Edit the file dashboard/views.py and replace the placeholders with your Twilio details:

### #Twilio Credentials
account_sid = 'your_account_sid'

auth_token = 'your_auth_token'

from_ = 'your_twilio_phone_number'

## App Navigation:
• Welcome Page: http://127.0.0.1:8000/

• Quiz Page: http://127.0.0.1:8000/quiz/

• Admin Dashboard Login: http://127.0.0.1:8000/admin/login/?next=/admin/

• Admin Homepage: http://127.0.0.1:8000/admin/
