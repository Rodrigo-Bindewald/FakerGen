# FakerGen
FakerGen é uma aplicação Python desenvolvida para gerar dados fictícios válidos, como nome completo, CPF, e-mail, endereço e número de telefone, utilizando a biblioteca Faker e executado via terminal. O projeto tem como foco gerar dados brasileiros de maneira prática e automatizada para serem usados em testes de software ou simulações.
## Funcionalidades

O projeto **FakerGen** oferece as seguintes funcionalidades:

1. **Geração de Nome Completo**  
   - O programa gera nomes completos aleatórios usando a biblioteca Faker, com suporte à localidade brasileira.

2. **Geração de CPF Falso (Válido)**  
   - Gera um CPF falso com formatação e dígitos verificadores válidos usando uma lógica interna de cálculo.

3. **Geração de E-mail**  
   - Gera um e-mail fictício válido, com domínio aleatório.

4. **Geração de Endereço Completo**  
   - Gera um endereço completo, incluindo rua, número, cidade, estado e CEP.

5. **Geração de Número de Telefone**  
   - Gera um número de telefone brasileiro, com DDD e no formato comum do Brasil.

6. **Exibição de Todos os Dados**  
   - Exibe de forma estruturada todos os dados gerados (nome, CPF, e-mail, endereço e telefone).

## Requisitos

- Python 3.6 ou superior
- Biblioteca [Faker](https://faker.readthedocs.io/en/master/)

### Instalação das Dependências

Para instalar as dependências necessárias, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

## Como usar

1.Clone o repositório
Primeiro, você precisa clonar o repositório do projeto. Execute o seguinte comando no terminal:

```bash 
git clone https://github.com/Rodrigo-Bindewald/FakerGen.git
```

2. Navegue até a pasta do projeto
Depois de clonar o repositório, vá até o diretório do projeto com o comando:

```bash
cd FakerGen/src
```

3. Execute o script Python
Agora, para gerar os dados fictícios, execute o arquivo Python:

```bash
python faker_gen.py
```

Saída esperada
Quando o programa for executado, ele gerará e exibirá os seguintes dados fictícios no terminal:

```bash
Nome Completo: João da Silva  
CPF: 123.456.789-09  
E-mail: joaosilva@example.com  
Endereço Completo: Rua Exemplo, 123, São Paulo - SP, 01234-567  
Telefone: (11) 98765-4321
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
