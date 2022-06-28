import argparse
from AnaliseLexica import lexico
from AnaliseSintatica import sintatico
from AnaliseSemantica import semantico
from Codigo_Intermediario import intermediario
from Codigo_Final import codigo_Final

def analise_lexica(args):
    tabela_tokens = lexico(args).tabela_tokens()
    return tabela_tokens

def analise_sintatica(args):
    tokens = analise_lexica(args)
    analisador_sintatico = sintatico(tokens)
    analisador_sintatico.verificacao_sintatica()
    return analisador_sintatico

def analise_semantica(args):
    tokens = analise_lexica(args)
    analise_sintatica(args)
    analisador_semantico = semantico(tokens)
    analisador_semantico.analysis()
    return analisador_semantico 

def tabela_simbolos_semantico(args):
    analisador_semantico = analise_semantica(args)
    analisador_semantico.table_symbol()
    print("Fim tabela de simbolos.....")

def cod_intermediario(args):
    tokens = analise_lexica(args)
    analise_sintatica(args)
    analisador_semantico = semantico(tokens)
    lista_id = analisador_semantico.analysis()
    cod_intermediario = intermediario(tokens, lista_id)
    cod_intermediario.inicia_geracao()
    return cod_intermediario

def cod_final(args, name):
    cod_intermediario(args)
    codigo_final = codigo_Final("./arquivo_intermediario.txt", name)
    codigo_final.inicia_geracao()
    return codigo_final

def log_lexico(args):
    tabela_tokens = analise_lexica(args)
    print(" -=-"*20)
    print("\t\t\t       Análise Lexica")
    print(" -=-"*20)
    print("\n[TOKENS,LEXEMA,LINHA,COLUNA]")
    for token in range(len(tabela_tokens)):
        print(tabela_tokens[token])
    print('Termino Execução da Análise Léxica.......')

def log_sintatico(args):
    print(" -=-"*20)
    print("\t\t\t       Análise Sintática")
    print(" -=-"*20)
    analisador_sintatico = analise_sintatica(args)
    analisador_sintatico.log_operacoes()
    print('Termino da Execução da Análise Sintática.....')

def log_semantico(args):
    print(" -=-"*20)
    print("\t\t\t       Análise Semantica")
    print(" -=-"*20)
    analisador_semantico = analise_semantica(args)
    analisador_semantico.log_operacoes()
    print('Termino da Execução da Análise Semantica.....')

def log_cod_intermediario(args):
    print(" -=-"*20)
    print("\t\t\t       Log Codigo Intermediario")
    print(" -=-"*20)
    cod_intermed = cod_intermediario(args)
    cod_intermed.log_intermediary()
    print("Fim log intermediario....")
    print(" -=-"*20)
    print("\t\t\t       Codigo Intermediario")
    print(" -=-"*20)
    arquivo_intermediario = open("arquivo_intermediario.txt","r")
    for line in arquivo_intermediario:            
        print(line, end='')
    arquivo_intermediario.close()  
    print("Fim codigo intermediario....")


def log_cod_final(args, name):
    print(" -=-"*20)
    print("\t\t\t       Log Codigo Final")
    print(" -=-"*20)
    codigo_final = cod_final(args, name)
    codigo_final.log_finalCode()
    print("Fim log Final.....")


def log_final(args, name):
    log_cod_intermediario(args)
    log_cod_final(args,name)


def log_tudo(args, name):
    log_lexico(args)
    log_sintatico(args)
    log_semantico(args)
    tabela_simbolos_semantico(args)
    log_cod_intermediario(args)
    log_cod_final(args, name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Compilador VIN',description=" Compilador em Fase de Construção")
    parser.add_argument('-ls', '--ls', help="Mostra o log do analisador sintático")
    parser.add_argument('-tudo', '--tudo',  nargs=2, help="Mostra todas as listagens do Compilador")
    parser.add_argument('-lt', '--lt', help="Mostra a lista de tokens do analisador lexico")
    parser.add_argument('-lse', '--lse', help="Mostra o log do analisador semantico")
    parser.add_argument('-ts', '--ts', help="Exibe a tabela de simbolos")
    parser.add_argument('-lgcI', '--lgcI', help="Exibe o log do codigo intermediario ")
    parser.add_argument('-lgcF', '--lgcF', nargs=2, help="Exibe o log do codigo final ")
    parser.add_argument('-lgc', '--lgc', nargs=2, help="Exibe o log do codigo final ")
    parser.add_argument('default', type=str, nargs='*', help="Caso nao haja nenhum argumento")
        
args = parser.parse_args()

if args.ls:
    log_sintatico(args.ls)
elif args.tudo:
    log_tudo(args.tudo[0], args.tudo[1])
elif args.lt:
    log_lexico(args.lt)
elif args.lse:
    log_semantico(args.lse)
elif args.ts:
    tabela_simbolos_semantico(args.ts)
elif args.lgcI:
    log_cod_intermediario(args.lgcI)
elif args.lgcF:
    log_cod_final(args.lgcF[0], args.lgcF[1])
elif args.lgc:
    log_final(args.lgc[0], args.lgc[1])
elif args.default:
    log_tudo(args.default[0], args.default[1])



