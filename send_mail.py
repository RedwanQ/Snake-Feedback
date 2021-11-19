import smtplib 
from email.mime.text import MIMEText


def send_mail(customer, game, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '77ac2eab5e4f57'
    password = '4f5250fa72a52e'
    message = f"<h3>Welcome {customer.capitalize()} </h3><ul><li>Customer: {customer}</li><li>Dealer: {game}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>   "
    sender_email = 'hyvirusper@gmail.com'
    receiver_email = 'ridwanmohamedco@outlook.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Snake Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # send
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())