import yagmail
import dotenv
import os


dotenv.load_dotenv(override=True)

email = os.getenv('EMAIL')
senha = os.getenv('SENHA_APP')

def manda_email(subject, msg, destinatario):
    # filename = "document.pdf"

    yag = yagmail.SMTP(user=email, password=senha)
    yag.send(
        to=destinatario,
        subject=subject,
        contents=msg
        # attachments=filename,
    )
