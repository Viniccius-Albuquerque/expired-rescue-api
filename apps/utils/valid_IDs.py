# Validation user ID
def validando_id(ID_valido):
    if ID_valido is not None:
        if not isinstance(ID_valido,int) or isinstance(ID_valido,bool):
            raise TypeError("O ID deve ser um número inteiro.")
        if ID_valido <= 0:
            raise ValueError("O ID não pode ser zero ou negativo.")
    return ID_valido