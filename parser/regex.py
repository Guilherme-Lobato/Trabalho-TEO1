import ply.lex as lex

reservados = {
    'MES': 'MES',
    'SEMANA': 'SEMANA',
    'DIA': 'DIA',
    'REPETIR': 'REPETIR',
    'CORRER': 'CORRER',
    'DESCANSAR': 'DESCANSAR',
    'KM': 'KM',
    'MIN': 'MIN',
}

tokens = (
    'INTENSIDADE', 'TEXTO', 'NUMERO',
    'ABRE_CHAVES', 'FECHA_CHAVES'
) + tuple(reservados.values())

t_ABRE_CHAVES = r'\{'
t_FECHA_CHAVES = r'\}'

t_ignore = ' \t\r'

def t_TEXTO(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.value = str(t.value)[1:-1]
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservados.get(t.value.upper(), 'INTENSIDADE')
    return t

def t_nova_linha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

lexico = lex.lex()
