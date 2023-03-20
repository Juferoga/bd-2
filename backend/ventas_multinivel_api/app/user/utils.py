import secrets, string

def generate_password():
  password = ''
  for _ in range(0,18):
    password += secrets.choice(string.ascii_letters + string.digits)
  return password