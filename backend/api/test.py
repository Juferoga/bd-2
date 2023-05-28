


sql1 = [ 
            f"create user default tablespace USERSDEF temporary tablespace USERSTMP quota 1m on USERSDEF",
            f"grant connect to ",
]

print(sql1[0])
print(sql1[1])


# Cosas que se han modificado

# ALTER TABLE USUARIO ADD (T_USERNAME VARCHAR2(20));
# ALTER TABLE USUARIO ADD CONSTRAINT username_unique UNIQUE (T_USERNAME);