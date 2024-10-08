
totalMeses = 0
somaTemperaturas = 0
mesesmais33graus = 0
temperaturaMaisEscaldante = 0
temperaturaMenosQuente = 50


# Entrada de informação do usuário sobre o mês
while totalMeses<=11:
  print("Para encerrar basta colocar um mês negativo.")
  mes = int(input("> Informe um mês usando valor númerico de 1 a 12 representando (janeiro a dezembro): "))
  if mes<0:
    break

# Validação do mês
  while mes<=0 or mes>=13:
    print(">> Erro, mês inválido. O mês deve estar no intervalo de [1;12]")
    mes = int(input("> Informe novamente um mês usando valor númerico de 1 a 12 representando (janeiro a dezembro): "))

# Entrada de informação do usuário e validação sobre a temperatura
  temperatura = float(input("> Informe em Celsius a temperatura máxima do mês: "))
  while temperatura<=-61 or temperatura>=51:
    print(">> Erro, temperatura inválida. A temperatura deve estar no intervalo de [-60;50].")
    temperatura = float(input("> Informe em Celsius a temperatura máxima do mês: "))

# Mês númerico para extenso
  if mes == 1:
    mesExtenso = "Janeiro"
  elif mes == 2:
    mesExtenso = "Fevereiro"
  elif mes == 3:
    mesExtenso = "Março"
  elif mes == 4:
    mesExtenso = "Abril"
  elif mes == 5:
    mesExtenso = "Maio"
  elif mes == 6:
    mesExtenso = "Junho"
  elif mes == 7:
    mesExtenso = "Julho"
  elif mes == 8:
    mesExtenso = "Agosto"
  elif mes == 9:
    mesExtenso = "Setembro"
  elif mes == 10:
    mesExtenso = "Outubro"
  elif mes == 11:
    mesExtenso = "Novembro"
  else:
    mesExtenso = "Dezembro"

# Media das temperaturas
  totalMeses = totalMeses + 1
  somaTemperaturas = somaTemperaturas + temperatura

# Quantidade meses escaldantes
  if temperatura>33:
    mesesmais33graus = mesesmais33graus + 1

# Mês mais escaldante
  if temperatura > temperaturaMaisEscaldante:
    temperaturaMaisEscaldante = temperatura
    mesMaisEscaldante = mesExtenso

# Mês menos quente
  if temperatura <= temperaturaMenosQuente:
    temperaturaMenosQuente = temperatura
    mesMenosQuente = mesExtenso

  #Resultados
  mediaTemperatura = somaTemperaturas / totalMeses

print("fim do programa")
print("=" * 90)
if totalMeses == 0:
  print("Dados não informados.")
else:
  print(f"Temperatura média máxima anual: {mediaTemperatura:.2f}")
  print(f"Quantidade de meses escaldantes: {mesesmais33graus}")
  print(f"Mês mais escaldante do ano: {mesMaisEscaldante}, Temeperatura de: {temperaturaMaisEscaldante}")
  print(f"Mês menos quente do ano: {mesMenosQuente}, Temperatura de: {temperaturaMenosQuente}")
