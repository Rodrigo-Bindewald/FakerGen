# Importando Bíblioteca faker
from faker import Faker
import random

# Criando uma instância do Faker para gerar dados fictícios
fake = Faker('pt_BR')  # Usando a localidade pt_BR para gerar dados brasileiros

# Função para gerar um CPF válido (usando Faker para formato e uma lógica simples para dígitos válidos)
def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]  # Gera os 9 primeiros dígitos aleatórios
    for _ in range(2):  # Calcula os dois dígitos verificadores
        val = sum([(len(cpf)+1-i)*v for i, v in enumerate(cpf)]) % 11
        cpf.append(11-val if val > 1 else 0)
    return '{}.{}.{}-{}'.format(*[''.join(map(str, cpf[i:i+3])) for i in range(0, 9, 3)], ''.join(map(str, cpf[9:])))

# Gerando Nome Completo
nome_completo = fake.name()

# Gerando CPF válido
cpf_falso = gerar_cpf()

# Gerando e-mail
email_falso = fake.email()

# Gerando Endereço Completo
endereco_completo = fake.address()

# Gerando Telefone com DDD
telefone = fake.phone_number()

# Exibindo todos os dados de forma estruturada
print(f"Nome Completo: {nome_completo}")
print(f"CPF: {cpf_falso}")
print(f"E-mail: {email_falso}")
print(f"Endereço Completo: {endereco_completo}")
print(f"Telefone: {telefone}")
