password = input("şifrenizi giriniz : ")


def check_password(passw):
    import re
    if len(passw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]", passw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]", passw):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]", passw):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]", passw):
        raise Exception("parola alpha numeric karakter içermelidir")
    elif re.search("\s", passw):
        raise Exception("parola boşluk içermemelidir")
    else:
        raise Exception("Geçerli parola")

#password = "123456"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola")
finally:
    print("Validation tamamlandı")