'''
A ideia inicial é apenar tentar caulcular o ciclo inicial de secagem
'''
import math

def tempo_abastecimento(camaras_necessarias,numero_de_cargas_esperado,tempo_medio_descarga):
    return round((numero_de_cargas_esperado/camaras_necessarias)*tempo_medio_descarga)


def ajuste_capacidade (capacidadenominalcamara,numerodecamara,fatordecorrecao):
    return(capacidadenominalcamara*numerodecamara)*fatordecorrecao

def calculo_tempo_secagem (dryrate,umidadecolheita,umidadealvo):
    diferenca_de_umidade = umidadecolheita - umidadealvo
    return diferenca_de_umidade * dryrate

def ciclo_de_secagem (temposecagem,tempoabastecimento,tempoesperadebulhe,tempodebulhando):
    return temposecagem+tempoabastecimento+tempoesperadebulhe+tempodebulhando

def numero_de_cargas (volumecampo,volumeporcarga):
    return math.ceil(volumecampo/volumeporcarga)

def quantidade_camaras_necessarias (volumecampo,capacidade_nominal):
    return math.ceil(volumecampo / capacidade_nominal)


def monta_a_string(camaras_necessarias,numero_de_cargas_esperado):
    previsao_quantidade_de_camara = numero_de_cargas_esperado/camaras_necessarias
    return print(f'O campo possui iria ter aproxidamamente {numero_de_cargas_esperado} carretas,\n \
irá utilizar aproximadamente {camaras_necessarias} câmaras,\n  \
e é esperador que coloquemos {math.ceil(previsao_quantidade_de_camara)} carretas/cam.')


capacidade_nominal_das_camaras = int(input('Qual a capacidade nominal das câmaras? '))
numero_de_camaras = int(input('Qual o número de câmaras do secador? '))
volume_da_carreta = int(input ('Qual o volume médio de cada carga em kg ? '))
expectativa_volume_cliente = int(input ('Qual o volume experado para o campo kg ? '))
dry_rate_medio = float(input('Qual o dry ratting médio? '))
target_de_secagem = float(input('Qual target de umidade de secagem? '))
umidade_colheita_esperada = float(input("Qual a umidade de colheita esperada? "))
tmdescarga = float(input('Qual tempo médio de descarga ? '))
ted = float(input('Qual tempo médio de espera para debulha ? '))
td = float(input('Qual tempo médio de debulha ? '))
camaras_necessarias=quantidade_camaras_necessarias(expectativa_volume_cliente,capacidade_nominal_das_camaras)
numero_de_cargas_esperado = numero_de_cargas(expectativa_volume_cliente,volume_da_carreta)
tempo_abastecendo = tempo_abastecimento(camaras_necessarias,numero_de_cargas_esperado,tmdescarga)
monta_a_string(camaras_necessarias,numero_de_cargas_esperado)
tds = calculo_tempo_secagem(dry_rate_medio,umidade_colheita_esperada,target_de_secagem)
x = ciclo_de_secagem(temposecagem= tds,tempoabastecimento=tempo_abastecendo,tempoesperadebulhe=ted,tempodebulhando=td)
csd = x/24 #ciclo de secagem em dias
fator_correcao = 7/csd