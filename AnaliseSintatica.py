import sys

		# python3 Compilador.py -ls test1.txt

try:    
    class sintatico:
        def __init__(self, tokens):
            
            
            self.pilha = ['$', 'PROGRAMA']

            self.tokens = list(tokens)
            self.tokens.append('$') #add ao final pra poder comparar com a pilha

            #mostrar os logs
            self.empilhamento = 0
            self.desempilhamento = 0
            self.reducao_pilha_lista = 0
            self.producoes_aplicadas = []

            self.arquivo = open("log_operacoes.txt",'w')

            self.producoes = {
                0 : ['inicio', ';' , 'LIST_CODIGO', 'fim', ';'],
                1 : ['CODIGO', ';', 'LIST_CODIGO'],
                2 : [],
                3 : ['VARIAVEIS'],
                4 : ['ESCREVA'],
                5 : ['LEIA'],
                6 : ['CONDICIONAL'],
                7 : ['REPETICAO'],
                8 : ['EXPRESSAOMAT'],
                9 : [':', 'VALOREXPRESSAO'],
                10 : ['numero'],
                11 : [],
                12 : ['numero','OPERADORESARITMETICO'],
                13 : ['id','OPERADORESARITMETICO'],
                14 : ['(','VALOREXPRESSAO', ')', 'OPERADORESARITMETICO'],
                15 : ['+','VALOREXPRESSAO'],
                16 : ['-', 'VALOREXPRESSAO'],
                17 : ['*', 'VALOREXPRESSAO'],
                18 : ['/', 'VALOREXPRESSAO'],
                19 : [],
                20 : ['int', 'id', 'ATRIBUICAO'],
                21 : ['id', 'ATRIBUICAO'],
                22 : ['escreva', '(', 'id', ')'],  
                23 : ['leia', '(', 'id', ')'],
                24 : ['id'],
                25 : ['numero'],
                26 : ['='],
                27 : ['>'],
                28 : ['MISTO', 'OPERADORESLOGICO','MISTO'],
                29 : ['SE' , 'ENTAO' ,'SENAO' ,'FIMSE'],
                30 : ['se', '(', 'LOGICA', ')'],
                31 : ['entao','LIST_CODIGO'],
                32 : ['senao', 'LIST_CODIGO'],
                33 : [],
                34 : ['fimse'],
                35 : ['faca', '(', 'MISTO', 'OPERADORESARITMETICO', ')'],
                36 : ['enquanto', '(', 'LOGICA', ')'],
                37 : ['ENQUANTO', 'FACA']
            }

            self.nao_terminais = {
                'PROGRAMA' : [0],
                'LIST_CODIGO' : [1, 2],
                'CODIGO' : [3, 4, 5, 6, 7, 8],
                'ATRIBUICAO' : [9, 10, 11],
                'VALOREXPRESSAO' : [12, 13, 14],
                'OPERADORESARITMETICO' : [15, 16, 17, 18, 19],
                'VARIAVEIS' : [20],
                'EXPRESSAOMAT' : [21],
                'ESCREVA' : [22],
                'LEIA' : [23],
                'MISTO' : [24,25],
                'OPERADORESLOGICO' : [26, 27],
                'LOGICA' : [28],
                'CONDICIONAL' : [29],
                'SE' : [30],
                'ENTAO' : [31],
                'SENAO' : [32,33],
                'FIMSE' : [34],
                'FACA' : [35],
                'ENQUANTO' : [36],
                'REPETICAO' : [37]
            }

            self.terminais = {
                ';' : [11,19],
                '(' : [14],   
                ')' : [19],
                '+' : [15],
                '-' : [16],
                '*' : [17],
                '/' : [18],
                '=' : [26],
                '>' : [27],
                ':' : [9],
                'numero' : [28,10,12,25],
                'id' : [1, 8, 21, 28, 24,13],
                'inicio': [0],
                'fim': [2],
                'int': [1, 3, 20],
                'leia' : [1 ,5, 23],
                'escreva' : [1, 4, 22],
                'se' : [1, 6, 29, 30],
                'entao' : [31],
                'senao' : [2, 32],
                'fimse' : [2, 33, 34],
                'enquanto' : [1, 7, 37, 36],
                'faca' : [35] 
            }

        def verificacao_sintatica(self):      
            while( len(self.tokens) != 0 and len(self.pilha) != 0):
                
                if len(self.tokens) == 1 and len(self.pilha) > 1:
                  
                    print("Erro Sintático: Pilha sintática possui dados e lista sintática  está vazia [erro ao executar análise] ", self.pilha )
                    sys.exit()   
                if len(self.tokens) > 1 and (self.pilha) == 1:   
                    print("Erro Sintático: Lista sintática possui dados e pilha sintatica vazia [erro ao executar análise]", self.tokens)               
                    sys.exit()
                if self.tokens[0][0] == self.pilha[-1]:
                    
                    self.reg_operacoes(3,-1)
                    del self.tokens[0]  
                    self.pilha.pop()  
                    self.reducao_pilha_lista += 1
                    self.desempilhamento += 1    
                else:
                    self.tabela_sintatica()            
            #print("Analise Sintática Executada Corretamente!")
            self.arquivo.close()

        #Método para verificar regras de produção
        def tabela_sintatica(self):
            try:
                producao = self.verifica_producao()
                

            except:
                #print('Erro Sintático: era esperado o valor {0} na linha {1} coluna {2}'.format(self.pilha[-1], self.tokens[0][2], self.tokens[0][3]))
                print("Erro Sintático: não possível encontrar uma producao válida para o valor '{0}' na linha {1} e coluna {2}.[erro ao executar análise]".format(self.tokens[0][1], self.tokens[0][2], self.tokens[0][3]))
                sys.exit()
            else:
                self.aplica_producao(producao)

        #Metodo reponsavel por verificar se existe producao válida
        def verifica_producao (self):
            
            producao = []  

            x, y = self.valor_producao()            

            producao = list(set(x).intersection(y)) 
          
            
            return producao[0]
        
   
        #Método responsabel por retornar a chave dos dicionarios.
        def valor_producao(self):        
            key_stack  = [-1] 
            key_list = [-1]  

            #Procurando na Pilha       
            for i in self.nao_terminais.keys():  
                if i == self.pilha[-1]:           
                    key_stack = self.nao_terminais[i]               
        
            #Procurando na Lista.       
            for j in self.terminais.keys():        
                if j == self.tokens[0][0]:
                    key_list = self.terminais[j]
                    
            return (key_stack,key_list)       
                    
        
        def aplica_producao(self, producao):
            try:
                valor_producao = self.producoes[producao]



                self.producoes_aplicadas.append(producao)            
            
                self.reg_operacoes(1, producao)
                self.pilha.pop()  
                self.desempilhamento += 1

                #producoes vazias 2, 12, 20, 33
                if any([valor_producao != 2, valor_producao != 12, valor_producao != 20, valor_producao != 33]):                     
                    
                    for i in reversed(valor_producao):                    
                        self.pilha.append(i)
                        self.empilhamento += 1
                        self.reg_operacoes(2, producao)
                
            except:
                print("Erro Sintático: nao foi possivel encontrar uma producao valida para o valor  {0} na linha {1} e coluna {2}. [erro ao executar análise]".format(self.tokens[0][1], self.tokens[0][2], self.tokens[0][3]))            
            
        def reg_operacoes(self,n, producao):
        
            #Desempilhamento
            if n == 1:
                self.arquivo.write("DESEMPILHANDO:...... Topo Pilha: {0} ->  producao a ser inserida {1}. \n".format(self.pilha[-1], producao))
            #Empilhamento
            elif n == 2:
                self.arquivo.write("EMPILHANDO:......... Topo Pilha: {0} -> producao aplicada {1}. \n".format(self.pilha[-1], producao))
            #Reducao
            elif n ==3:  
                self.arquivo.write("REDUCAO APLICADA:.... Topo Pilha: {0} First List: {1}\n".format(self.pilha[-1],self.tokens[0][0] ))
        
            
        def log_operacoes (self):
            #self.verificacao_sintatica()
            print(" -=-"*20)
            print("\t\t\t       LOG DE OPERACOES")
            print(" -=-"*20)
            print("Empilhamentos.........................:",self.empilhamento)
            print("Desempilhamento.......................:", self.desempilhamento)
            print("Producoes utilizadas..................:", self.producoes_aplicadas)
            print("Redução de Pilha e Lista..............:", self.reducao_pilha_lista)
            print("Quantidade de producoes utilizadas ...:", len(self.producoes_aplicadas))
            print(" -=-"*20)
            arquivo = open("log_operacoes.txt","r")
            for linha in arquivo:
                linha = linha.rstrip()
                print (linha)
            arquivo.close()
except:
    print('Deu Ruim')


