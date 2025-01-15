from validate_docbr import CPF
import re

def nome_invalido(value):
    return not value.replace(' ', '').isalpha()

def cpf_invalido(value):
    cpf = CPF()
    return not cpf.validate(str(value))

def celular_invalido(value):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    result =  re.findall(model, value)
    print(result)
    print(bool(result))
    return not bool(result)