import os
def limpar_tela():
    os.system("cls || clear")


from dataclasses import dataclass
@dataclass 
class pessoa_funcionario:
    nome: str
    sobrenome: str
    idade: int
    cpf : float
    sexo : str
    salario : float
def calcular_salario(salario):
    if salario <= 1100.01 and salario <= 2203.48:
            salario * 0.09 
            return salario 
    if salario >= 2203.49 and salario <= 3305.22:
       salario * 0.12 
       return salario
    if salario >= 3305.22 and salario <= 6433.57:
         salario * 0.14
         return salario
    


# Solicite a matrícula e senha do funcionário para ter acesso aos seus dados.
# Solicite o salário base do funcionário. 
# #Pergunte se o funcionário deseja receber vale transporte (s/n). 
# Pergunte o valor do vale refeição fornecido pela empresa. 
# Calcule os descontos e acréscimos na folha de pagamento do funcionário. 
# Mostre o salário líquido do funcionário após os descontos e acréscimos.
#  Observações Considere que o funcionário possui apenas um dependente. 
# Considere que o salário base é o salário antes de quaisquer descontos ou acréscimos. 
# Considere que o salário base, o vale refeição e o plano de saúde são informados em reais (R$). 
# Exemplos de Cálculo Exemplo 1: Salário Baixo (R$ 1.412,00) com 0 Dependentes e Vale Transporte Salário Base:
#  R$ 1.412,00 Dependentes: 0 Vale Transporte: Sim Vale Refeição: R$ 300,00 Salário Líquido: R$ 1.161,38

#Exemplo 2: Salário Alto (R$ 10.000,00) com 2 Dependentes e Sem Vale Transporte Salário Base: R$ 10.000,00 Dependentes: 
# 2 Vale Transporte: Não Vale Refeição: R$ 500,00 Salário Líquido: R$ 6.400,92
matricula = int(input("Digite seu matricula: "))
senha = input("Digite sua senha: ")
limpar_tela()
while True:
    print("""
            ===BEM VINDO A RECEITA FEDERAL===       
    1 - Criar funcionario
    2 - consultar dados      """)   
     
    if senha == senha :
          salario = float(input("Digite seu salário: "))
          respota_transporte = input("Gostaria de receber auxilio transporte? (s/n)").lower()