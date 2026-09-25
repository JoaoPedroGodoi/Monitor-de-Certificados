import smtplib
from email.message import EmailMessage
try:
    from config_local import EMAIL_DESTINATARIOS, ASSUNTO_EMAIL, SMTP_SERVIDOR, SMTP_PORTA, EMAIL_REMETENTE
except ImportError:
    from config import EMAIL_DESTINATARIOS, ASSUNTO_EMAIL, SMTP_SERVIDOR, SMTP_PORTA, EMAIL_REMETENTE


def enviar_email(problemas, operantes):

    msg = EmailMessage()
    msg['Subject'] = f"{ASSUNTO_EMAIL} (Problemas: {len(problemas)})"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = ", ".join(EMAIL_DESTINATARIOS)

    linhas_tabela = ""
    for certificado in problemas:
        linhas_tabela += f"""
        <tr>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px;">
                {certificado['codigo']}
            </td>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px;">
                {certificado['identificador']}
            </td>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px; color:#dc2626; font-weight:bold;">
                {certificado['status']}
            </td>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px;">
                {certificado['classificacao']}
            </td>
        </tr>
        """
        
    for certificado in operantes:
        linhas_tabela += f"""
        <tr>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px;">
                {certificado['codigo']}
            </td>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px;">
                {certificado['identificador']}
            </td>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px; color:#16a34a; font-weight:bold;">
                {certificado['status']}
            </td>
            <td style="padding:10px 12px; border-bottom:1px solid #e9ecef; font-size:13px;">
                {certificado['classificacao']}
            </td>
        </tr>
        """

    html = f"""
    <html>
    <body style="font-family:Segoe UI, Arial, sans-serif; padding:24px; margin:0; background-color:#f6f8fb;">
    <div style="max-width:900px; margin:0 auto; background-color:#ffffff; border:1px solid #e5e7eb; border-radius:8px; padding:24px;">
        <div style="margin-bottom:12px;">
            <h2 style="margin:0; color:#0f172a; font-size:22px;">Monitoramento de Certificados Digitais</h2>
        </div>
        <p style="margin:0 0 16px 0; color:#475569; font-size:14px;">
            Encontramos <b>{len(problemas)}</b> certificado(s) com problema e <b>{len(operantes)}</b> operante(s).
        </p>
        <table style="width:100%; border-collapse:collapse; border:1px solid #e5e7eb; border-radius:6px; overflow:hidden;">
            <tr style="background:#0B5CAD; color:white; text-align:left;">
                <th style="padding:12px; font-size:13px; font-weight:600;">Código</th>
                <th style="padding:12px; font-size:13px; font-weight:600;">Identificador</th>
                <th style="padding:12px; font-size:13px; font-weight:600;">Status</th>
                <th style="padding:12px; font-size:13px; font-weight:600;">Classificação</th>
            </tr>
            {linhas_tabela}
        </table>
        <p style="margin:0; color:#64748b; font-size:12px; text-align:center;">
            Este e-mail foi enviado automaticamente.
        </p>
    </div>
    </body>
    </html>
    """
    msg.set_content("Monitoramento de Certificados Digitais")
    msg.add_alternative(html, subtype='html')

    try:
        with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as server:
            server.send_message(msg)
        print("E-mail enviado com sucesso via SMTP!")
    except Exception as e:
        print(f"Erro ao enviar e-mail via SMTP: {e}")