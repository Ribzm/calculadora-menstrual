print('Vamos calcular o dia da sua próxima menstruação')
dia = int(input('Digite o dia da sua última menstruação (apenas o dia): '))
mes = int(input('Agora, digite o mês (número): '))
proxdia = dia + 28
mes30 = [4, 6, 9, 11]
mes31 = [1, 3, 5, 7, 8, 10, 12]
if mes in mes30:
    if proxdia > 30:
        proxdia -= 30
        mes += 1
elif mes in mes31:
    if proxdia > 31:
        proxdia -= 31
        mes += 1
else:
    proxdia -= 28
    mes +=1
if mes == 13:
    mes -= 12
print('Sua próxima menstruação deverá começar no dia {}/{}'.format(proxdia, mes))