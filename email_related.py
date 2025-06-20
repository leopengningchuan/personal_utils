import re, os, platform

if platform.system() == 'Windows':
    import win32com.client as win32

def is_valid_email(email_address):
    return re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email_address) is not None


def is_valid_email_list(email_address_list):
    if isinstance(email_address_list, str):
        if not is_valid_email(email_address_list):
            raise ValueError(f"Invalid email format: {email_address_list}")
        return email_address_list
            
    elif isinstance(email_address_list, list):
        for email_address in email_address_list:
            if not is_valid_email(str(email_address)):
                raise ValueError(f"Invalid email format: {email_address}")
        return ";".join(email_address_list)
    

def outlook_send_email(email_sender, email_receiver, email_subject, email_body, 
                       email_attached = None, email_cc = None, email_bcc = None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    # check email address
    if not isinstance(email_sender, str):
        raise ValueError(f"Invalid email format: {email_sender}")
    else:
        mail.SentOnBehalfOfName = is_valid_email_list(email_sender)
    mail.To = is_valid_email_list(email_receiver)
    if email_cc:
        mail.CC = is_valid_email_list(email_cc)
    if email_bcc:
        mail.BCC = is_valid_email_list(email_bcc)

    if email_attached:
        if isinstance(email_attached, list):
            for f in email_attached:
                file_path = os.path.abspath(f)
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"Attachment not found: {f}")
                mail.Attachments.Add(file_path)
        else:
            file_path = os.path.abspath(email_attached)
            if not os.path.exists(file_path):
                    raise FileNotFoundError(f"Attachment not found: {file_path}")
            mail.Attachments.Add(file_path)
    
    mail.Subject = email_subject
    mail.Body = email_body
    mail.Send()

    print(f'{email_subject.ljust(50)} ----- email sent successfully.')