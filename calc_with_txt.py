import calculator as calc
import ui
import calc_with_voice as c

def txt_calculator():
  try:
    calcs = calc.read_calcs("calculadora_calculos.txt")
    results = calc.calculator(calcs)
    calc.save_results(results)
    ui.print_colored_green("Calculos realizados com sucesso! Verifique o arquivo com os resultados.")
    c.os_speaking("Calculos realizados com sucesso! Verifique o arquivo com os resultados.")
  except Exception:
    ui.print_colored_red("Erro ao ler o arquivo de calculos.")
    c.os_speaking("Erro ao ler o arquivo de calculos.")