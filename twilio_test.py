#!python3

import os
from twilio.rest import Client

account_sid = os.environ["ACd8851761adb1535a93f8c3a8e1597382"]
auth_token = os.environ["69567a3c81425b2a0e2395ea60f57dce"]

client = Client(account_sid, auth_token)

client.message.create(
	to=os.environ["+40726182217"],
	from_="+12064880209",
	body="test"
	)