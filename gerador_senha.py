import string
import random

def gerar_senha(comprimento=8, incluir_especiais=True):
    """
    Gera uma senha aleatória com o comprimento especificado.

    Parâmetros:
        comprimento (int): O número de caracteres da senha. Padrão é 8.
        incluir_especiais (bool): Se True, inclui caracteres especiais. Padrão é True.

    Retorna:
        str: Uma senha aleatória contendo letras, números e (opcionalmente) caracteres especiais.
    """

    if comprimento < 1:
        raise ValueError("O comprimento da senha deve ser pelo menos 1.")  # Evita valores inválidos

    # Conjunto de caracteres básicos: letras e números
    caracteres = string.ascii_letters + string.digits
    
    # Adiciona caracteres especiais, se necessário
    if incluir_especiais:
        caracteres += string.punctuation

    # Garante que a senha contenha pelo menos uma letra maiúscula, uma minúscula e um número
    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]

    # Se incluir caracteres especiais, adiciona pelo menos um
    if incluir_especiais:
        senha.append(random.choice(string.punctuation))

    # Preenche o restante da senha com caracteres aleatórios
    senha += random.choices(caracteres, k=comprimento - len(senha))

    # Embaralha os caracteres para evitar padrões previsíveis
    random.shuffle(senha)

    return ''.join(senha)

# Exemplo de uso
senha = gerar_senha(12)
print(senha)