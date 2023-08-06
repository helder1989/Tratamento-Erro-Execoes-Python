try:
    a = int(input('Numerador:' ))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError): # dois tipos de exeções
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar seus dados!')
else:
    print(f'O resultado é {r}')
finally:
    print('Agradeço e volte sempre!!!')


