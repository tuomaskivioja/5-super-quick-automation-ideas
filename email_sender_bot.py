import requests

# specify the Mailgun API endpoint and credentials
MAILGUN_API_ENDPOINT = ""
MAILGUN_API_KEY = ''

# define a function to send an email
def send_email(to, subject, body):

    # create a dictionary with the email data
    data = {
        # ! Fill in
        'from': '',
        'to': to,
        'subject': subject,
        'text': body
    }

    # send a POST request to the Mailgun API endpoint
    response = requests.post(
        MAILGUN_API_ENDPOINT,
        auth=('api', MAILGUN_API_KEY),
        data=data
    )

    # check if the request was successful
    if response.status_code == 200:
        print('Email sent successfully!')
    else:
        print('An error occurred while sending the email.')

# example usage - ! Fill in
to = ""
subject = 'HI'
body = 'HIT THE LINKE BUTTON'
send_email(to, subject, body)