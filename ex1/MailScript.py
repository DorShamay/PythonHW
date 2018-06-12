#!/bin/usr/env python3.6

#########################################
# Porpuse : Send Mail                   #
# Version : 0.0.2                       #
# Creator : DorShamay                   #
#########################################

import smtplib
import email.utils
import sys
import getpass

from email.mime.text import MIMEText

exit = ("\n Exit nicely via the MainMenu Please")

def mainmenu():
    ans = True
    while ans:
        print("""
        1.Mail Sending Service
        2.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print("\n Enjoy !")
            main()
        elif ans == "2":
            print("\n Goodbye !")
            sys.exit(0)
        elif ans != "":
            print("\n Not Valid Choice Try again")

def main():
    try:
        gmailuser = input("Write your Gmail User here --> ")
        password = getpass.getpass("Write your Gmail password here --> ")
        recipient = input("Please write your Recipient Mail --> ")
        author = input("Please write your email address --> ")
        subject = input("Please put your subject here --> ")
        description = input("Put your description here --> ")

    # Create the message
        msg = MIMEText(description)
        msg['To'] = email.utils.formataddr((recipient, recipient))
        msg['From'] = email.utils.formataddr((author, author))
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmailuser, password)
        server.set_debuglevel(False) # show communication with the server
        try:
            server.sendmail(author, recipient, msg.as_string())
            sys.exit(0)
        finally:
            pass
    except TypeError:
        print("You didn't write the input correctly please try again")
    except KeyboardInterrupt:
        print(exit)
        mainmenu()

mainmenu()
main()