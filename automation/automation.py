import re

def emails(data):

    with open(data, 'r') as f:
        file = f.read()
        email_not_duplicated = []
        e_pattern = r"[a-z0-9]+@[a-z]+.[a-z]+"
        emails = re.findall(e_pattern, file)
        emails.sort()
        for email in emails:
            if email not in email_not_duplicated:
                email_not_duplicated.append(email)

        with open('emails.txt', 'w') as w:
            for email in email_not_duplicated:
                w.write(f'{str(email)}\n')    
    
    return email_not_duplicated



if __name__ == '__main__':
   print(emails('assets/potential-contacts.txt'))
