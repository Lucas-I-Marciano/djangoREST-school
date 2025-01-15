from validate_docbr import CPF

def nome_invalido(value):
    return not value.replace(' ', '').isalpha()

def cpf_invalido(value):
    cpf = CPF()
    return not cpf.validate(str(value))

def celular_invalido(value):
    return len(value) != 13