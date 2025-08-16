import json
import smtplib
from config import settings

# get data from serverless.yml filters them accordingly and stores them in variable
def helper(event,context):
    thunder = json.loads(event.get('body','{}'))
    to = thunder.get('to')
    sub = thunder.get('sub')
    body = thunder.get('body')

    try:
        if all([to,sub,body]):
            send_email(to=to, sub=sub, body=body)
            return{
                'statusCode':200,
                'body':json.dumps({'response':'connection was build successfully helper is working............. transfered data to send_email..... email sent'})
            }
        elif not all([to,sub,body]):
            return {
                'statusCode':400,
                'body':json.dumps({'Error:some fields are missing in helper'})
            }
        else:
            return{
                'statusCode':404,
                'body':json.dumps({'resources not found error may occured before te condition even start'})
            }
    except Exception as e:
        return{
            'statusCode':500,
            'body':json.dumps({f'Error:as error occored at function level the problem might be in entire function, variables are not being passed {e}'})
        }

# gets the data from helper and sends the email
print("all clear 1")
def send_email(to, sub, body):
    print("all clear 2")
    try:
        print("all clear 3")    
        with smtplib.SMTP(settings.Email_host,settings.Email_port) as server:
            server.starttls()
            print("all clear 4")
            server.login(settings.Email_name,settings.Email_password)
            print("all clear 5")
            email = f"subject:  {sub}\n\n{body}"
            print("all clear 6")
            server.sendmail(settings.Email_name,to,email)
            print("all clear 7")
    except Exception as e:
        print(f"failed to send email main logic error {e}")