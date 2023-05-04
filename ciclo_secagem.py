'''
A ideia inicial é apenar tentar caulcular o ciclo inicial de secagem
'''
import math

def ajuste_capacidade (capacidadenominalcamara,numerodecamara,fatordecorrecao):
    return(capacidadenominalcamara*numerodecamara)*fatordecorrecao

def calculo_tempo_secagem (dryrate,umidadecolheita,umidadealvo):
    diferenca_de_umidade = umidadecolheita - umidadealvo
    return diferenca_de_umidade * dryrate

def ciclo_de_secagem (temposecagem,tempoabastecimento,tempoesperadebulhe,tempodebulhando):
    return temposecagem+tempoabastecimento+tempoesperadebulhe+tempodebulhando


'''
def numero_de_cargas (volumecampo,volumeporcarga):
    return math.ceil(volumecampo/volumeporcarga)

def quantidade_camaras_necessarias (volumecampo):
    capacidade_nominal_camara = 120000
    return math.ceil(volumecampo / capacidade_nominal_camara)


volumedacarreta = int(input ('Qual o volume médio de cada carga em kg ? '))
expectativa_volume_cliente = int(input ('Qual o volume experado para o campo kg ? '))
#a= quantidade_camaras_necessarias(expectativa_volume_cliente)
#b = numero_de_cargas(expectativa_volume_cliente,volumedacarreta)
'''
'''
dry_rate_medio = float(input('Qual o dry ratting médio? '))
target_de_secagem = float(input('Qual target de umidade de secagem? '))
umidade_colheita_esperada = float(input("Qual a umidade de colheita esperada? "))
ta = float(input('Qual tempo médio de descarga ? '))
ted = float(input('Qual tempo médio de espera para debulha ? '))
td = float(input('Qual tempo médio de debulha ? '))
tds = calculo_tempo_secagem(dry_rate_medio,umidade_colheita_esperada,target_de_secagem)
'''
tds = calculo_tempo_secagem(5,29,11)
x = ciclo_de_secagem(temposecagem= tds,tempoabastecimento=6,tempoesperadebulhe=15.9,tempodebulhando=8.6)
csd = x/24 #ciclo de secagem em dias
fator_correcao = 7/csd
a = ajuste_capacidade (120000,12,fator_correcao)
print(a)