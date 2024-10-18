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

import os
from dataclasses import dataclass

def limpar_tela():
    os.system("cls || clear)

@dataclass 
class PessoaFuncionario:
    nome: str
    sobrenome: str
    idade: int
    cpf: float
    sexo: str
    salario: float
    dependentes: int = 0
    vale_transporte: str 
    vale_refeicao: float = 0.0

def calcular_desconto(salario):
    if salario <= 1100.01:
        return salario * 0.09
    elif salario <= 2203.48:
        return salario * 0.09
    elif salario <= 3305.22:
        return salario * 0.12
    elif salario <= 6433.57:
        return salario * 0.14
    return 0

def calcular_salario_liquido(funcionario: PessoaFuncionario):
    desconto_inss = calcular_desconto(funcionario.salario)
    vale_transporte = funcionario.salario * 0.06 if funcionario.vale_transporte == 's' else 0
    dependentes_deduzidos = funcionario.dependentes * 189.59

    salario_liquido = (funcionario.salario - desconto_inss - vale_transporte + dependentes_deduzidos - funcionario.vale_refeicao)
    return salario_liquido

matricula = int(input("Digite sua matrícula: "))
senha = input("Digite sua senha: ")
limpar_tela()

while True:
    print("""
            === BEM VINDO À RECEITA FEDERAL ===       
    1 - Criar funcionário
    2 - Consultar dados
    3 - Sair
    """)   

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do funcionário: ")
        sobrenome = input("Digite o sobrenome: ")
        idade = int(input("Digite a idade: "))
        cpf = float(input("Digite o CPF: "))
        sexo = input("Digite o sexo: ")
        salario = float(input("Digite o salário: "))
        
        dependentes = int(input("Digite o número de dependentes: "))
        
        vale_transporte = input("Gostaria de receber auxílio transporte? (s/n): ").lower()
        
        vale_refeicao = float(input("Digite o valor do vale refeição: "))
        
        funcionario = PessoaFuncionario(nome, sobrenome, idade, cpf, sexo, salario, dependentes, vale_transporte, vale_refeicao)
        
        salario_liquido = calcular_salario_liquido(funcionario)
        print(f"Salário líquido do funcionário {nome}: R$ {salario_liquido:.2f}")
    
    elif opcao == "2":
        print("Consultar dados ainda não implementado.")
    
    elif opcao == "3":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
