import string
import random

def gerar_senha(comprimento=8):
    """
    Gera uma senha aleatória com o comprimento especificado.

    Parâmetros:
        comprimento (int): O número de caracteres da senha. Padrão é 8.

    Retorna:
        str: Uma senha aleatória contendo letras, números e caracteres especiais.
    """
    
    if comprimento < 1:
        raise ValueError("O comprimento da senha deve ser pelo menos 1.")  # Evita valores inválidos
    
    # Conjunto de caracteres possíveis: letras maiúsculas, minúsculas, números e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo 'comprimento' caracteres aleatórios da lista
    senha = ''.join(random.choices(caracteres, k=comprimento))
    
    return senha  # Retorna a senha gerada

# Teste da função com uma senha de 5 caracteres
senha = gerar_senha(5)
print(senha)  # Exibe a senha gerada