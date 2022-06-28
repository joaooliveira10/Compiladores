from infixa_posfixa import infixa_posfixa

class intermediario:
    def __init__(self, list_tokens, list_id):
        self.lista_tokens = list_tokens
        self.lista_id = list(list_id.keys())
        self.cod_intermediario = []
        self.op_logico = ['>', '=']
        self.log_intermediario = open("log_intermediario.txt","w")

    def inicia_geracao(self):
        #Declarações de variaveis
        for id in self.lista_id:
           self.cod_intermediario.append(f'_Var {id}')
           self.log_intermediario.write(f'Declarado variavel {id}\n')
        #Gramática
        i=0
        for token in self.lista_tokens:

            if token[0] == 'leia' :
               self.cod_intermediario.append(f'leia {self.lista_tokens[i+2][1]}')
               self.log_intermediario.write(f'Comando de leitura da variavel {self.lista_tokens[i+2][1]} \n') 
            
            elif token[0] == 'escreva':
                self.cod_intermediario.append(f'escreva {self.lista_tokens[i+2][1]}')
                self.log_intermediario.write(f'Comando de escrita da variavel {self.lista_tokens[i+2][1]}\n') 


            elif token[0] == ':':
                j=i+1
                atribuicao =""
                while self.lista_tokens[j][0] != ';':
                    atribuicao += " "+self.lista_tokens[j][1]
                    stack = atribuicao.split(' ')
                    j+=1
                  
                self.cod_intermediario.append(f'{self.lista_tokens[i-1][1]} = {infixa_posfixa(stack)}')     
                self.log_intermediario.write(f'Atribuido a {self.lista_tokens[i-1][1]} a expressao {infixa_posfixa(stack)}\n ') 

            elif token[0] == 'enquanto':
                self.cod_intermediario.append("enquanto")
                self.log_intermediario.write("Comando de repeticao `enquanto` reconhecido\n ") 

                
            elif token[0] == 'faca':
                j=i+1                         
                condicao = " "
                exp = ""
                
                while self.lista_tokens[j][0] != ';':                   
                    
                    if self.lista_tokens[j][0] in self.op_logico:
                        if self.lista_tokens[j-1][0] == "id":
                            condicao+= self.lista_tokens[j-1][1] +" "+ self.lista_tokens[j][1]
                            exp= ""
                        else:    
                            condicao += infixa_posfixa(exp) + " "+self.lista_tokens[j][1]
                            exp = ""
                        j+=1

                    if self.lista_tokens[j][0] != '(' and self.lista_tokens[j][0] != ')':
                        exp += " "+self.lista_tokens[j][1]                        
                    j+=1 
                if exp.islower(): 
                    condicao += exp     
                else: 
                    condicao += infixa_posfixa(exp)   
                              
         
                self.cod_intermediario.append(f'faca {condicao}')
                self.log_intermediario.write("Comando de repeticao `faca` reconhecido\n ") 

            elif token[0] == 'se':
                j=i+1                         
                condicao = " "
                exp = ""
                
                while self.lista_tokens[j][0] != 'entao':     
                    if self.lista_tokens[j][0] in self.op_logico:
                        if self.lista_tokens[j-1][0] == "id":
                            condicao+= self.lista_tokens[j-1][1] +" "+ self.lista_tokens[j][1]
                            exp= ""
                        else:               
                            condicao += infixa_posfixa(exp) + " "+self.lista_tokens[j][1]
                            exp = ""
                        j+=1

                    if self.lista_tokens[j][0] != '(' and self.lista_tokens[j][0] != ')':
                        exp += " "+self.lista_tokens[j][1]                        
                    j+=1 
                if exp.islower(): 
                    condicao += exp     
                else: 
                    condicao += infixa_posfixa(exp)                 
         
                self.cod_intermediario.append(f'se {condicao} entao')
                self.log_intermediario.write("Comando condicional `se` reconhecido\n ") 

            elif token[0] == 'fimse':
                self.cod_intermediario.append("fimse")     
                self.log_intermediario.write("Comando fim de condicional `fimse` reconhecido\n ") 

            elif token[0] == 'senao':
                self.cod_intermediario.append("senao")
                self.log_intermediario.write("Comando condicional `senao` reconhecido\n ") 


            i+=1
        
        self.log_intermediario.close()  
        self.getIntermediario() 
       
    def getIntermediario(self):
        arquivo_intermediario = open ("arquivo_intermediario.txt","w")
        for line in self.cod_intermediario:            
            arquivo_intermediario.write(line+"\n")
        arquivo_intermediario.close()    

    def log_intermediary(self):
        log_int = open("log_intermediario.txt","r")
        for log in log_int:
            print(log)
        log_int.close()