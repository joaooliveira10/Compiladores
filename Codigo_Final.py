import re
import os

class codigo_Final:

    def __init__(self, cod_intermediario, name):
        self.codigo_final = []         
        self.variaveis = []
        self.addr_var = []
        self.name = name
        self.cont_label = 0
        self.label_if= 0 
        self.label_endif = 0
        self.label_else = 0
        self.stack_label = []
        self.codigo_intermediario = []
        self.log_final = open("log_final.txt","w")
        self._arquivo = open(cod_intermediario, "r")

        for line in self._arquivo:
            self.codigo_intermediario.append(line)
        self._arquivo.close()

        

    def inicia_geracao(self):
        """Variaveis"""
        self.obter_tabela_variaveis()           #Obtem as variaveis 
        self.getAddr_var()                      #Cria endereços para as variaveis
        self.log_final.write("Declaracao de variaveis realizada\n")

        self.codigo_final.append(".global main")
        self.codigo_final.append("{0}       @empilhamento endereco de retorno".format("main:\npush {ip, lr}"))
        self.log_final.write("Empilhamento de endereco de retorno\n")

        for line in  self.codigo_intermediario:
            if line.split()[0] == 'leia':
                    self.log_final.write("Comando leia executado\n")
                    self.codigo_final.append("{0}       @load addres of pattern number".format("LDR R0, =format2"))
                    self.codigo_final.append("{0}       @load addres of variable".format("LDR R1, ="+line.split()[1]))
                    self.codigo_final.append("BL scanf  @call function for leia")                    
            elif line.split()[0] == 'escreva':
                self.log_final.write("Comando escreva executado\n")
                self.codigo_final.append("{0}           @load addres of pattern number".format("LDR R0, ="+self.getAddr_var(line.split()[1:len(line.split())])))
                self.codigo_final.append("BL printf      @call function for escreva")
                    
            elif line.split()[0] == 'se':
                self.log_final.write("Comando se executado\n")
               
                self.label_if = self.getLabel()
                self.label_else = self.getLabel() 
                self.label_endif = self.getLabel()         
                self.stack_label.append(self.label_else) #Label for endif

                exp = []

                for atr in line.split()[1:len(line.split())-1]:
                    exp.append(atr)         
                self.calc_expLogic(exp, 'se')

                self.stack_label.append(self.label_else)
                self.codigo_final.append("{0}:      @label content se".format(self.label_if))

            elif line.split()[0] == 'fimse':
                self.log_final.write("Fim do comando se \n")

                self.codigo_final.append("{0}:      @label for fimse".format(self.stack_label.pop()))
  
            elif  line.split()[0] == 'senao':
                self.log_final.write("Comando senao executado\n")
                self.codigo_final.append("B {0}      @jump for fimse".format(self.label_endif))
                self.codigo_final.append("{0}:      @label for senao".format(self.stack_label.pop()))
                self.stack_label.append(self.label_endif)                

            elif line.split()[0] == "enquanto": 
                self.log_final.write("Comando `enquanto` executado\n")

                self.label_if = self.getLabel()                
                self.label_else = self.getLabel()         
                self.stack_label.append(self.label_else) #Label for endif
                label_do = self.getLabel()
                self.stack_label.append(label_do)

                self.codigo_final.append("{0}:      @label for `enquanto`".format(label_do))
                self.codigo_final.append("{0}:      @label content `enquanto`".format(self.label_if))
          

            elif line.split()[0] == "faca": 
                self.log_final.write("Comando faca executado\n")
                exp = []
                for atr in line.split()[1:len(line.split())]:
                    exp.append(atr)                             
               
                self.calc_expLogic(exp, 'faca')

                self.codigo_final.append("{0}:      @label for fimEnquanto-Faca".format(self.stack_label.pop()))

            elif  line.split()[1] == '=':
                self.log_final.write("Atribuicoes de variaveis executado\n")
                self.calcula_expressao(line.split(" ",2)[2].strip())
                self.codigo_final.append("pop {R1}          @pops in R1")
                self.codigo_final.append("LDR R0, ={0}      @load address".format(line.split()[0]))
                self.codigo_final.append("STR R1, [R0]      @store  result")
        
        self.codigo_final.append("pop {ip, pc}")
        self.addr_var.append(".extern printf")
        self.addr_var.append(".extern scanf")

        self.log_final.close()
        self.getFinal()          
        print("Codigo Final gerado com sucesso.")
        
        
    def getFinal(self):
        arquivo_final = open (self.name,"w")
        for line in self.codigo_final:            
            arquivo_final.write(line+"\n")
        for line in self.addr_var:            
            arquivo_final.write(line+"\n")    
        arquivo_final.close() 

    def log_finalCode(self):
        log_f = open("log_final.txt","r")
        for log in log_f:
            print(log)
        log_f.close()

    def calc_expLogic(self, exp, value):
        i=0
        expressao= ""      
        c_log = ""
        while i != len(exp):         
            
            if exp[i] == '>':                
                self.calcula_expressao(expressao)
                self.codigo_final.append("pop {R0}          @pops R0")        
                self.codigo_final.append("MOV R1, R0        @mov content for R1")                
                c_log = exp[i]
                expressao = ""

            elif exp[i] == "=":                
                self.calcula_expressao(expressao)
                self.codigo_final.append("pop {R0}          @pops R0")        
                self.codigo_final.append("MOV R1, R0        @mov content for R1")                
                c_log = exp[i]
                expressao = ""

            expressao +=" "+exp[i]                      
            i+=1

        self.calcula_expressao(expressao)
        self.codigo_final.append("pop {R0}      @pops R0")   
        self.codigo_final.append("MOV R2, R0        @mov content for r2")
        self.codigo_final.append("CMP R1, R2        @compar contents")     
        if value == 'se':          
            self.getExpBool(c_log)
        else:
            self.getExpBool2(c_log)
                                                                                                                                    
    def getExpBool(self, conector):        
        if conector == ">":
            self.codigo_final.append("BGE {0}      @case Val1<Val2".format(self.stack_label.pop()))
        elif conector == "=":                
            self.codigo_final.append("NE {0}      @case Val1!=Val2".format(self.stack_label.pop()))                                

    def getExpBool2(self, conector):        
        if conector == ">":
            self.codigo_final.append("BGT {0}      @case Val1>Val2".format(self.stack_label.pop()))
        elif conector == "=":                
            self.codigo_final.append("EQ {0}      @case Val1=Val2".format(self.label_else))


    #Metodo para obter variaveis
    def obter_tabela_variaveis(self):        
        for line in self.codigo_intermediario:                     
            if re.search("^_Var", line):               
                self.variaveis.append(line.split()[1])


    def getAddr_var(self, atr = None):
        
        #Chamado apenas uma vez no inicio, cria todos as variaveis
        if atr == None:
            self.addr_var.append(".data")
            self.addr_var.append(".balign 8")
            self.addr_var.append("format: .asciz \"%d\\n\" ")
            self.addr_var.append("format2: .asciz \"%d\" ")

            for var in self.variaveis:                
                self.addr_var.append(".balign 8")
                self.addr_var.append("{0}: .word 0".format(var.strip()))
        #caso seja uma atribuicao ja declarada
        else:
            self.calcula_expressao(atr[0])
            self.codigo_final.append("pop {R1}         @pops in R1")
            return "format"
            
    def getLabel(self):
        self.cont_label +=1
        return "L{0}".format(self.cont_label)

    def calcula_expressao(self, expressao):        
        
        _expressao =[]
        _expressao.append(expressao)      

        if len(expressao) > 1:
            for atr in _expressao[0].split(" "): 
                
                if atr.strip().islower():
                    self.codigo_final.append("LDR R0, ={0}      @load addres for variable".format(atr.strip()))
                    self.codigo_final.append("LDR R0, [R0]      @load data of variable")
                    self.codigo_final.append("push {R0}         @stack variable content")
                elif atr.strip().isdigit():
                    self.codigo_final.append("MOV R0, #{0}      @load number".format(atr.strip()))
                    self.codigo_final.append("push {R0}         @stack variable content")
                elif atr.strip() == "+":
                    self.codigo_final.append("pop {R1}          @pops in R1")
                    self.codigo_final.append("pop {R0}          @pops in R0")
                    self.codigo_final.append("ADD R0, R0, R1    @sum operation")
                    self.codigo_final.append("push {R0}         @stack result content")
                elif atr.strip() == "-":
                    self.codigo_final.append("pop {R1}          @pops in R1")
                    self.codigo_final.append("pop {R0}          @pops in R0")
                    self.codigo_final.append("SUB R0, R0, R1    @subtraction operation")
                    self.codigo_final.append("push {R0}         @stack result content")   
                elif atr.strip() == "*":
                    self.codigo_final.append("pop {R1}          @pops in R1")
                    self.codigo_final.append("pop {R0}          @pops in R0")
                    self.codigo_final.append("MUL R0, R0, R1    @multiplication operation")
                    self.codigo_final.append("push {R0}         @stack result content")
                elif atr.strip() == "/":   
                    self.codigo_final.append("pop {R2}          @pops in R1")
                    self.codigo_final.append("pop {R1}          @pops in R2")
                    self.codigo_final.append("MOV R0, #0        @init variable for resultable")
                    self.codigo_final.append("_division:        @create label")
                    self.codigo_final.append("SUBS R1, R1, R2   @subtraction operation")
                    self.codigo_final.append("ADD R0, R0,#1     @result division")
                    self.codigo_final.append("BHI _division     @jump case R1>R2")
                    self.codigo_final.append("push {R0}         @stack result content")
        else:
            if expressao.isdigit():           
                self.codigo_final.append("MOV R0, #{0}      @load addres for variable".format(expressao))              
                self.codigo_final.append("push {R0}         @stack result content")

            else:
                self.codigo_final.append("LDR R0, ={0}      @load addres for variable".format(expressao))
                self.codigo_final.append("LDR R0, [R0]      @load data of variable")
                self.codigo_final.append("push {R0}         @stack result content")