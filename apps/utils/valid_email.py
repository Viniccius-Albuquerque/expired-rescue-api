def email(NewEmail):
    if not isinstance(NewEmail,str):
        raise TypeError("O email do usuário deve ser uma string.")
    NewEmail = NewEmail.strip()
    if not NewEmail:
        raise ValueError("O email do usuário não pode ser vazio.")
    if "@" not in NewEmail or "." not in NewEmail:
        raise ValueError("O email do usuário deve conter '@' e '.'")
    if NewEmail.count("@") != 1:
        raise ValueError("O email do usuário deve conter apenas um '@'.")
    return NewEmail
