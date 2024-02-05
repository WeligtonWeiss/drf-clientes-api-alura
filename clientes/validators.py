import re
from validate_docbr import CPF

def cpf_valido(cpf):
    cpf = CPF()
    return cpf.validate(cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o celular é válido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)

    return resposta
#         
#     return nome
# def validate_rg(self, rg):
#     if len(rg) != 9:
#         raise serializers.ValidationError("O RG deve ter 9 dígitos")
#     return rg
# def validate_celular(self, celular):
#     if len(celular) < 11:
#         raise serializers.ValidationError("O celular deve ter pelo menos 11 dígitos")
#     return celular