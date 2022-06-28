
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
OPERADORES = set(['+','-','/','*'])
PRIORIDADE = {'+':1, '-':1, '*':2, '/':2, '^':3}  

 

def infixa_posfixa(expression):

    stack = []

    saida_posfixa = '' 

    for char in expression:

        if char in OPERADORES:
            saida_posfixa+=" "
                
        if char not in OPERATORS:  
            saida_posfixa+=" "+char

        elif char=='(':                
                stack.append('(')

        elif char==')':
            
            while stack and stack[-1]!= '(':
                saida_posfixa+=" "+stack.pop()

            stack.pop()

        else:

            while stack and stack[-1]!='(' and PRIORIDADE[char]<=PRIORIDADE[stack[-1]]:
                saida_posfixa+=" "+stack.pop() 

            stack.append(char)
        
    while stack:
        saida_posfixa+=" "+stack.pop()
    return saida_posfixa