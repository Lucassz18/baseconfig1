print("=-="*40)
print("Olá, bem vindo ao LulusSystem!")
print("=-="*40)

a = ""
b = ""
c = ""
d = ""

a = str(input("Digite o nome do autuado: "));
b = str(input("Digite o auto: "));
c = str(input("Digite o CEP: "));
d = str(input("Digite o endereço: "));
e = str(input("Digite o número da casa: "));
f = str(input("Possui complemento: [S/N]\n").lower());
if f == "s":
    g = str(input("Digite o complemento: "))
    print(f'autuado: {a},auto: {b}, CEP: {c}, endereço: {d}, número da casa: {e}, complemento: {g}\n\n')
else:
    print(f'autuado: {a},auto: {b}, CEP: {c}, endereço: {d}, número da casa: {e}\n\n')