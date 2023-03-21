
import csv
codCargos = []
numeroVotavel = []
nomeVotavel = []
qtdVotos = []
ciro = 0
lula = 0
cao = 0
with open("C:/Users/laura/PycharmProjects/ApuracaoEleitoral/dadosRNcsv.csv", "r") as arquivo:
    arquivocsv = csv.reader(arquivo, delimiter=';')
    for linha in arquivocsv:
        codCargos.append(linha[16])
        #print(codCargos)
        numeroVotavel.append(linha[29])
        nomeVotavel.append(linha[30])
        qtdVotos.append(linha[31])
#agora sim eu tenho todas as listas com os valores que eu preciso

#Agora começa o tratamento desses dados
#retirando o elemento 0 dessas listas, porque ele é o nome da coluna
codCargos.pop(0)
numeroVotavel.pop(0)
nomeVotavel.pop(0)
qtdVotos.pop(0)

#convertendo os dados de string para inteiro usando list comprehesions
Intcodcargos = [int(v) for v in codCargos]
IntqtdVotos = [int(v) for v in qtdVotos]
IntnumeroVotavel = [int(v) for v in numeroVotavel]

#verificando o código do voto se ele é válido ou não
for i in Intcodcargos:
    if i == 1:
        print("presidente")
        if numeroVotavel[i] != 95:
            print("voto branco")
            print(numeroVotavel[i])
        if numeroVotavel[i] != 96:# com isso eu já sei que o voto não é branco nem nulo
                print("voto nulo")
        if numeroVotavel[i] == 12:
                    ciro += 1
        elif numeroVotavel[i] == 13:
                    lula += 1
        elif numeroVotavel[i] == 22:
                    cao += 1

#Verificando quem obteve mais votos e foi eleito
if( ciro > lula & lula > cao):
    print("Ciro presidente")
elif (lula > ciro & ciro > cao):
    print("lula presindete")
elif (cao > lula & lula > ciro):
    print("chegamos no inferno")
