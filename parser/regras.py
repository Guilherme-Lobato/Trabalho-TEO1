import ply.yacc as yacc
from regex import tokens

# A saída padrão do programa é construída no topo da árvore de regras
def p_planilha(p):
    '''planilha : lista_meses'''
    km_total, min_total = p[1]
    p[0] = f"""=====================
Planilha de Treino
=====================
Preparado para o seu novo ciclo de treinos?
Aqui esta o resumo da sua jornada:

- Distancia Total Estimada: {km_total:.2f} km
- Tempo Total de Recuperacao: {min_total:.2f} min


=======================
Input de entrada aceito
======================="""

def p_mesUnico(p):
    '''lista_meses : bloco_mes'''
    p[0] = p[1]

def p_mesMultiplo(p):
    '''lista_meses : lista_meses bloco_mes'''
    p[0] = (p[1][0] + p[2][0], p[1][1] + p[2][1])

def p_mesNormal(p):
    '''bloco_mes : MES TEXTO ABRE_CHAVES lista_semanas FECHA_CHAVES'''
    p[0] = p[4]

def p_repetirMes(p):
    '''bloco_mes : REPETIR NUMERO ABRE_CHAVES mes_sem_nome FECHA_CHAVES'''
    p[0] = (p[4][0] * p[2], p[4][1] * p[2])

def p_mesSemNome(p):
    '''mes_sem_nome : MES ABRE_CHAVES lista_semanas FECHA_CHAVES'''
    p[0] = p[3]

def p_semanaUnica(p):
    '''lista_semanas : bloco_semana'''
    p[0] = p[1]

def p_semanaMultipla(p):
    '''lista_semanas : lista_semanas bloco_semana'''
    p[0] = (p[1][0] + p[2][0], p[1][1] + p[2][1])

def p_semanaNormal(p):
    '''bloco_semana : SEMANA NUMERO ABRE_CHAVES lista_dias FECHA_CHAVES'''
    p[0] = p[4]

def p_repetirSemana(p):
    '''bloco_semana : REPETIR NUMERO ABRE_CHAVES semana_sem_numero FECHA_CHAVES'''
    p[0] = (p[4][0] * p[2], p[4][1] * p[2])

def p_semanaSemNumero(p):
    '''semana_sem_numero : SEMANA ABRE_CHAVES lista_dias FECHA_CHAVES'''
    p[0] = p[3]

def p_diaUnico(p):
    '''lista_dias : bloco_dia'''
    p[0] = p[1]

def p_diaMultiplo(p):
    '''lista_dias : lista_dias bloco_dia'''
    p[0] = (p[1][0] + p[2][0], p[1][1] + p[2][1])

def p_diaNormal(p):
    '''bloco_dia : DIA TEXTO ABRE_CHAVES lista_treinos FECHA_CHAVES'''
    p[0] = p[4]

def p_repetirDia(p):
    '''bloco_dia : REPETIR NUMERO ABRE_CHAVES dia_sem_nome FECHA_CHAVES'''
    p[0] = (p[4][0] * p[2], p[4][1] * p[2])

def p_diaSemNome(p):
    '''dia_sem_nome : DIA ABRE_CHAVES lista_treinos FECHA_CHAVES'''
    p[0] = p[3]

def p_treinoUnico(p):
    '''lista_treinos : comando'''
    p[0] = p[1]

def p_treinoMultiplo(p):
    '''lista_treinos : lista_treinos comando'''
    p[0] = (p[1][0] + p[2][0], p[1][1] + p[2][1])

def p_correr(p):
    '''comando : CORRER NUMERO KM INTENSIDADE'''
    p[0] = (float(p[2]), 0.0)

def p_descansar(p):
    '''comando : DESCANSAR NUMERO MIN'''
    p[0] = (0.0, float(p[2]))

def p_repetirTreino(p):
    '''comando : REPETIR NUMERO ABRE_CHAVES lista_treinos FECHA_CHAVES'''
    p[0] = (p[4][0] * p[2], p[4][1] * p[2])

def p_error(p):
    if p:
        raise SyntaxError(f"Token inesperado '{p.value}' (tipo {p.type}) na linha {p.lineno}.")
    else:
        raise SyntaxError("Fim de arquivo inesperado. Talvez voce tenha esquecido de fechar uma chave '}'.")

analisador_sintatico = yacc.yacc()
