import os

from login import Login


while True:
  print(31*"#")
  print('# Bem-vindo ao Mercado Livre! #')
  print(31*"#")
  print("1 - Entrar")
  print("0 - Sair")
  option = int(input("Digite a opção desejada: "))
  match(option):
    case 1:
      Login()
    case 0:
      os.system('cls' if os.name == 'nt' else 'clear')
      break
