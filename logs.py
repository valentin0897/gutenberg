import logging
import logging.config
import smtplib
import json

logging.basicConfig(
    filename='logs.log',
    format='%(levelname)s::%(asctime)s::%(message)s'
)


class Gmail():
    def __init__(self, email_to, email_from):
        self.email_to = email_to
        self.email_from = email_from

    def send_email(self, message: str) -> None:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login()
            server.sendmail(self.email_from, self.email, message)
            server.close()
            logging.info('Successfully sent the message to Gmail')
        except Exception as e:
            logging.error(f'Failed to send mail through Gmail: {e}')


class EmailHandler(logging.Handler):
    """Handler to send emails"""
    def __init__(self, mailer):
        super().__init__()
        self.mailer = mailer

    def emit(self, record: logging.LogRecord):
        """Sends message to email specified in .env file"""

        self.mailer.send_email(self.format(record))


class OnlyCriticalFilter(logging.Filter):
    """Base class to filter out logs"""

    def filter(self, record):
        return record.levelno == logging.CRITICAL


with open('logging_config.json', 'rt') as file:
    config = json.load(file)
    logging.config.dictConfig(config)


root_logger = logging.getLogger()

gmail = Gmail("some@email", "some@email")
emailHandler = EmailHandler(gmail)
root_logger.addHandler(emailHandler)

emailHandler.addFilter(OnlyCriticalFilter())
