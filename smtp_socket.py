import sys
import socket

# gmail.com       MX preference = 20, mail exchanger = alt2.gmail-smtp-in.l.google.com
# gmail.com       MX preference = 5, mail exchanger = gmail-smtp-in.l.google.com
# gmail.com       MX preference = 40, mail exchanger = alt4.gmail-smtp-in.l.google.com
# gmail.com       MX preference = 10, mail exchanger = alt1.gmail-smtp-in.l.google.com

def validate_hostname(inpt):
        candidate = inpt.strip()
        try:
                if len(candidate) == 0:
                        candidate = None
                        raise socket.gaierror
                socket.gethostbyname(candidate)
                return candidate
        except socket.gaierror:
                print("[ERR]  invalid destination:", candidate)
                sys.exit(1)


if __name__ == '__main__':
    MAIL_SERVER, PORT = ('64.233.184.26', 25)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((MAIL_SERVER, PORT))
    
    server_message = client_socket.recv(1024).decode()
    print('[SERVER]: ' + str(server_message))

    EMAIL_FROM = 'your_mom@email.com'
    RECPT_EMAIL = 'nikiton254@gmail.com'
    SUBJECT = 'TestSend'
    BODY = 'hello world!'

    commands = [f"HELO {MAIL_SERVER}\r\n",
        f"MAIL FROM:<{EMAIL_FROM}>\r\n",
        f"RCPT TO:<{RECPT_EMAIL}>\r\n",
        f"DATA\r\n",
        f"From: <{EMAIL_FROM}>\r\nTo: <{RECPT_EMAIL}>\r\nSubject: {SUBJECT}\r\n\r\n{BODY}\r\n.\r\n",
        "QUIT\r\n"
    ]

    for comm in commands:
        client_socket.sendall(comm.encode())
        server_message = client_socket.recv(1024).decode()
        print('[SERVER]: ' + str(server_message))
