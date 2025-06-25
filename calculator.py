import math
import ui
#função que lê o arquivo com as operações e retorna um array de arrays
#com 0 ou várias operações já formatadas
#[['1', '+', '1'], ['2', '+', '2']]
def read_calcs(path):
  try:
    calculator_file = open(path, "r")
    expression = calculator_file.read().split("\n")
    calcs = []
    for calc in expression:
      calcs.append(calc.strip())
    return calcs
  except FileNotFoundError:
    ui.loading_animation("Arquivo não encontrado - Criando arquivo...", 10, "YELLOW")
    calculator_file = open(path, "w")
    calculator_file.write("1 + 1")
    calculator_file.close()
    ui.print_colored_green("Arquivo criado com sucesso.")
    return read_calcs(path)
  finally:
    calculator_file.close()

#função que itera sobre o array com as operações e realiza o cálculo
def calculator(calcs):
  result = []
  for calc in calcs:
    try:
      #eval(1 + 1) - Método Python que avalia se uma expressão é valida e a executa
      calc_eval = eval(calc)
    except ZeroDivisionError:
      result.append("Erro: Divisão por zero.")
      continue
    except SyntaxError:
      result.append("Erro: Expressão inválida.")
      continue
    else:
      #utilizando o range [0:] evita erros caso uma expressão tenha somente um operando
      result.append(f"{calc} = {calc_eval}")
  return result

#função que salva os resultados em um novo arquivo
def save_results(results):
  try:
    calculator_file = open(f"calculadora_resultados.txt", "w")
    for result in results:
      calculator_file.write(str(result) + "\n")
  except FileNotFoundError:
    ui.print_colored_yellow("Arquivo não encontrado.")
  finally:
    calculator_file.close()