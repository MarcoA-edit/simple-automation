import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import mimetypes

servidor_email = smtplib.SMTP('smtp.office365.com', 587)
servidor_email.starttls()
servidor_email.login('EMAIL', 'SENHA')
remetente = 'REMETENTE'
destinatarios = ['DESTINATÁRIO']
assunto = 'ASSUNTO'
conteudo = f"DESCRIÇÃO DA MENSAGEM"

mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = ', '.join(destinatarios)
mensagem['Subject'] = assunto

mensagem.attach(MIMEText(conteudo, 'plain'))

mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = ', '.join(destinatarios)
mensagem['Subject'] = assunto

mensagem.attach(MIMEText(conteudo, 'plain'))

documento = 'rel_clima.xlsx'
arquivo = 'rel_clima.xlsx'

with open(documento, 'rb') as anexo:
    tipo_mimetype, _ = mimetypes.guess_type(documento)
    parte_anexo = MIMEApplication(anexo.read(), Name=arquivo)
    parte_anexo['Content-Disposition'] = f'attachment; filename="{arquivo}"'
    parte_anexo['Content-Type'] = tipo_mimetype
    mensagem.attach(parte_anexo)

servidor_email.sendmail(remetente, destinatarios, mensagem.as_string())

servidor_email.quit()