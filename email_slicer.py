email=input("enter email address:").strip()
user_name=email[:email.index("@")]
print("user name is:",user_name)
domain_name=email[email.index("@")+1:]
print("domain name is:",domain_name)
