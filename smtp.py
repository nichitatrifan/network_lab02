import socket

# gmail.com       MX preference = 20, mail exchanger = alt2.gmail-smtp-in.l.google.com
# gmail.com       MX preference = 5, mail exchanger = gmail-smtp-in.l.google.com
# gmail.com       MX preference = 40, mail exchanger = alt4.gmail-smtp-in.l.google.com
# gmail.com       MX preference = 10, mail exchanger = alt1.gmail-smtp-in.l.google.com

if __name__ == '__main__':
    PORT = 25
    
    MAIL_SERVER = str(input('Destination Server: '))
    if not MAIL_SERVER:
        MAIL_SERVER = 'gmail-smtp-in.l.google.com'
    
    EMAIL_FROM = str(input('Email from: '))
    if not EMAIL_FROM:
        EMAIL_FROM = 'my_email@email.com'
    
    RECPT_EMAIL = str(input('Recipient Email: '))
    if not RECPT_EMAIL:
        RECPT_EMAIL = 'nikiton254@gmail.com'
    
    SUBJECT = str(input('Subject: '))
    if not SUBJECT:
        SUBJECT = 'Test'
    
    BODY = str(input('Body: '))
    if not BODY:
        BODY = 'Text goest here!'

    commands = [
        f"HELO {MAIL_SERVER}\r\n",
        f"MAIL FROM:<{EMAIL_FROM}>\r\n",
        f"RCPT TO:<{RECPT_EMAIL}>\r\n",
        f"DATA\r\n",
        f"From: <{EMAIL_FROM}>\r\nTo: <{RECPT_EMAIL}>\r\nSubject: {SUBJECT}\r\n\r\n{BODY}\r\n.\r\n",
        "QUIT\r\n"
    ]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((MAIL_SERVER, PORT))
    
    server_message = client_socket.recv(1024).decode()
    print('[SERVER]: ' + str(server_message))

    for comm in commands:
        client_socket.sendall(comm.encode())
        server_message = client_socket.recv(1024).decode()
        print('[SERVER]: ' + str(server_message))
