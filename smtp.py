import socket

# gmail.com       MX preference = 20, mail exchanger = alt2.gmail-smtp-in.l.google.com
# gmail.com       MX preference = 5, mail exchanger = gmail-smtp-in.l.google.com
# gmail.com       MX preference = 40, mail exchanger = alt4.gmail-smtp-in.l.google.com
# gmail.com       MX preference = 10, mail exchanger = alt1.gmail-smtp-in.l.google.com

if __name__ == '__main__':
    MAIL_SERVER = str(input('Destination Server: '))
    PORT = 25
    EMAIL_FROM = str(input('Email from: '))
    RECPT_EMAIL = str(input('Recipient Email: '))
    SUBJECT = str(input('Subject: '))
    BODY = str(input('Body: '))

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
