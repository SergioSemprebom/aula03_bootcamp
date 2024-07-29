# exemplo: verificar se um numero é positivo
numero = -5

if numero >= 0:
    print("O numero é positivo")
print("O programa continua")

print('============================================================================================')

funcionario = {

'nome' : "Sergio Semprebom",
'idade': 44,
'salario' : 7_500,
'cargo': 'Cientista de dados jr',
'tempo_de_casa': 5 # valor do tempoo de casa precisa >= a 5 para ser executado.

}

if funcionario['tempo_de_casa'] >=5:
    funcionario['salario'] *= 1.2
    print(f'Parabéns {funcionario["nome"]}, voce recebeu um aumento de 20%.')
print('============================================================================================')