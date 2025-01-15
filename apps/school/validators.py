def nome_invalido(value):
    return not value.replace(' ', '').isalpha()

def cpf_invalido(value):
    return len(value) != 11

def celular_invalido(value):
    return len(value) != 13