import mandaEmail as me


subject = input('Digite o assunto do email: ')
msg = input('Digite a mensagem que vc quer enviar por email: ')
destinatario = input('Para quem quer enviar?: ')

me.manda_email(subject=subject, msg=msg, destinatario=destinatario)
