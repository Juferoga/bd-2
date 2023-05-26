from cryptography.fernet import Fernet

# mi_password = encriptar("netware124")

# user = authenticate_user("sgaa", mi_password)
# if not isinstance(user, UserOfDB):
#     print (user)
# else:
#     print("valid username")
# # if isinstance(authenticate_user("sga", mi_password), UserOfDB):
#     # print("hola mundo")

print(Fernet.generate_key())