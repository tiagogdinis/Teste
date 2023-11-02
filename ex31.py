from datetime import datetime

print("Idade")

dn = input("Introduza a data de nascimento (YYYY-MM-DD): ")
dn = datetime.strptime(dn,'%Y-%m-%d')

da = datetime.now()

diferenca = da - dn

anos = diferenca.days // 365

print("Idade =",anos,"anos")