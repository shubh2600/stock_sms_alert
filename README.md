# stock_sms_alert
Create account on https://www.twilio.com
get your free ph number from twilio
copy ACCOUNT SID from dashboard section and paste in the code eg. = account_sid = "xxxxxxxxxxx"
copy AUTH TOKEN from dashboard section and paste in the code eg. = auth_token = "xxxxxxxx"
copy your genrated free twilio ph number and paste in from variable and your personal number  in to variable client.messages.create(
    to="xxxxx",
    from_="xxxxxx",
    body=text,
)
