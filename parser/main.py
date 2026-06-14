import sys
from regex import lexico
from regras import analisador_sintatico

def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]
    caminho_saida = sys.argv[2]

    try:
        with open(caminho_entrada, 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
            
        lexico.lineno = 1
        resultado = analisador_sintatico.parse(dados, lexer=lexico)
        
        if resultado is not None:
            texto_saida = resultado
            aceito = True
        else:
            texto_saida = """=====================
Planilha de Treino (REJEITADA)
=====================
Ocorreu um erro ao processar a planilha. Entrada invalida.

=======================
Input de entrada contem erros estruturais.
======================="""
            aceito = False
            
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto_saida)
            
        if aceito:
            print(f"[ACEITO] O arquivo {caminho_entrada} foi processado com sucesso!")
        else:
            print(f"[REJEITADO] O arquivo {caminho_entrada} possui erros de sintaxe.")

    except Exception as erro:
        texto_saida = f"""=====================
Planilha de Treino (REJEITADA)
=====================
Ocorreu um erro ao processar a planilha:
{str(erro)}

=======================
Input de entrada contem erros estruturais.
======================="""
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto_saida)
        print(f"[REJEITADO] Erro ao processar {caminho_entrada}: {erro}")

if __name__ == '__main__':
    main()
