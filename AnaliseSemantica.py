import sys

class semantico:
    def __init__ (self, tokens):
        self.tokens = list(tokens)
        self.symbol_table = {} #inicia a tabela de simbolos
        self.arquivo = open("log_operacoes.txt",'w')
        #print(self.tokens)
    def analysis(self):
        lista = []
        i = 0
        
        for lista in self.tokens:
            atribuicao = ""           

            if(lista[0] == 'int'):                    
                self.verifica_declaracao(self.tokens[i+1])

            elif lista[0] == ':':   
                self.search(self.tokens[i-1])                
                c = i +1
                while self.tokens[c][1] != ';':
                    atribuicao += ""+ self.tokens[c][1] 
                    c+=1    
  
                self.update(self.tokens[i-1], atribuicao)                                     
                                    
            elif lista[1] == "/":  
                self.divisao_zero(self.tokens[i+1])
            elif lista[0] == 'id':
                self.search(lista)                                   
            i+=1 
        self.arquivo.close()
        return self.symbol_table
        
    def table_symbol(self):
        print(" -=-"*20)
        print("\t\t\t       Tabela de Simbolos")
        print(" -=-"*20)
        print("\n[Variaveis, VALOR]")
        for key, value in self.symbol_table.items():
           print("{0} - {1} ".format(key, value[2]))
        
        
    #Método responsavel por verificar se a variavel existe.
    def search(self, value):
        #print(value[1])
        if self.symbol_table.get(value[1]):
            return 1                                  
        else:
            print("Erro Semântico: variavel '{0}' nao declarada [linha {1}:coluna {2}]".format(value[1], value[2], value[3]))
            sys.exit()

    #Método responsavel por verificar se já existe declarado  a variavel
    def verifica_declaracao(self, var):
       
        if self.symbol_table.get(var[1]):
            print("Erro Semântico: variavel '{0}' já declarada [linha {1}:coluna {2}]".format(var[1], var[2], var[3] ))
            sys.exit()
        else:
            self.insert(var)

    #Método responsavel por insert dados na tabela
    def insert(self, token):        
        self.symbol_table[token[1]] = [token[0], 1, 0]
        self.reg_operacao(1, token[1], token[2])
    
    #Método responsavel por atualizar valores de atribuição das variaveis
    def update (self, val, atribuicao ):        
                                      
        list_temp =  self.symbol_table[val[1]]               
        list_temp[2] = self.search_atribuition(atribuicao)             
        self.symbol_table[val[1]]= list_temp            
      
                                
        self.reg_operacao(2,val[1], atribuicao)

    #Método responsavel por buscar as atribuições das variaveis
    def search_atribuition(self, value):
        
        #Enquanto o valor nao receber um digito, ou seja ser um id  
        while (not value.isdigit() ):
            #Se não estiver contido na tabela de simbolos apenas retorna o valor
            if( self.symbol_table.keys() != value):
                return value
            #crio uma lista temporaria para receber os valores da chave
            list_temp = self.symbol_table[value]
            value = str(list_temp[2])               
                
            #Se a atribuicao for um numero
            if value.isdigit():                    
                return value
        
        return value

    #Método responsavel por verificar se é uma divisão por zero
    def divisao_zero(self, value):
        #caso digito
        if value[1].isdigit():
            if self.search_atribuition(value[1]) == '0':
                print("Erro Semântico: divisão por zero não permitida [linha {0}:coluna {1}]".format(value[2], value[3]))            
                sys.exit()
        else:
            #caso variavel
            self.search(value)
            if self.search_atribuition(value[1]) == '0' or self.symbol_table[value[1]][2] == '0':
                print("Erro Semântico: divisão por zero não permitida [linha {0}:coluna {1}]".format(value[2], value[3]))            
                sys.exit()
            
    #Método que escreve o log em um arquivo de texto   
    def reg_operacao(self, val, variavel, value = None):        
        if (val ==1):
           self.arquivo.write("Variavel '{0}' declarada\n".format(variavel))

        elif (val == 2):
            self.arquivo.write("Variavel '{0}' atualizada o valor para '{1}'\n".format(variavel, value))
    
    #Método que imprimri o resultado
    def log_operacoes(self):
        arquivo = open("log_operacoes.txt","r")
        print(" -=-"*20)
        print("\t\t\t   LOG DE OPERACOES SEMANTICA")
        print(" -=-"*20)
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()    
            