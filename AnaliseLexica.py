import os
import sys
			# python3 AnaliseLexica.py -lt test1.txt
try:
	class lexico:
		
		def __init__(self, arquivo_fonte):
			self.cabeca = 0
			self.fita = []
			self.numero_linha = 1
			self.tabela_simbolos = []
			self.lexema = ''
			self.fim_linha = '\n'
			self.especiais = ['+','-','*','/','(',')','=','>',':',';']
			self.arquivo = arquivo_fonte
			if not os.path.exists(self.arquivo):
				print("Erro Geral: arquivo {0} não foi encontrado.".format(self.arquivo))
				exit()
			else:
					#print('Revise')
				self.arquivo = open(self.arquivo, 'r')

		def avancar_cabeca(self):
			self.cabeca += 1

		def posicao_cabeca(self):
			return self.cabeca

		def atualizar_linha(self):
			self.numero_linha += 1

		def obter_caracter(self):
			if self.cabeca < len(self.fita):
				self.letra = self.fita[self.cabeca]
				self.avancar_cabeca()
				if self.letra != self.fim_linha or not self.letra.isspace():
					self.lexema += self.letra
					return self.letra
				else:
					return '\n'
		def tabela_tokens(self):

			for self.linha in self.arquivo:
				self.fita = list(self.linha)
				self.q0()
				self.atualizar_linha()
				self.cabeca = 0
			self.arquivo.close()
			return self.tabela_simbolos

		def q0(self):
			self.caracter = self.obter_caracter()
			if 'e' == self.caracter:
				self.q1()
			elif 'l' == self.caracter:
				self.q8()
			elif 'f' == self.caracter:
				self.q22()
			elif 's' == self.caracter:
				self.q30()
			elif ';' == self.caracter:
				self.q35()
			elif '(' == self.caracter:
				self.q36()
			elif ')' == self.caracter:
				self.q37()
			elif '+' == self.caracter:
				self.q38()
			elif '-' == self.caracter:
				self.q39()
			elif '*' == self.caracter:
				self.q40()
			elif '/' == self.caracter:
				self.q41()
			elif '=' == self.caracter:
				self.q42()
			elif '>' == self.caracter:
				self.q43()
			elif ':' == self.caracter:
				self.q45()
			elif 'i' == self.caracter:
				self.q48()
			elif self.caracter.isdigit():
				self.q46()
			elif self.caracter.islower():
				self.q47()
			elif self.fim_linha == self.caracter:
				pass
			elif self.caracter.isspace():
				self.lexema = ''
				self.q0()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado" .format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q1(self):
			self.caracter = self.obter_caracter()
			if 's' == self.caracter:
				self.q2()
			elif 'n' == self.caracter:
				self.q12()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q2(self):
			self.caracter = self.obter_caracter()
			if 'c' == self.caracter:
				self.q3()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q3(self):
			self.caracter = self.obter_caracter()
			if 'r' == self.caracter:
				self.q4()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q4(self):
			self.caracter = self.obter_caracter()
			if 'e' == self.caracter:
				self.q5()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q5(self):
			self.caracter = self.obter_caracter()
			if 'v' == self.caracter:
				self.q6()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q6(self):
			self.caracter = self.obter_caracter()
			if 'a' == self.caracter:
				self.q7()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q7(self): 
			'''Reconhece o comando todo ESCREVA'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["escreva", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["escreva", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["escreva", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q8(self):
			self.caracter = self.obter_caracter()
			if 'e' == self.caracter:
				self.q9()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q9(self):
			self.caracter = self.obter_caracter()
			if 'i' == self.caracter:
				self.q10()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q10(self):
			self.caracter = self.obter_caracter()
			if 'a' == self.caracter:
				self.q11()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q11(self): 
			'''Reconhece o comando todo LEIA'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["leia", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["leia", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["leia", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q12(self):
			self.caracter = self.obter_caracter()
			if 'q' == self.caracter:
				self.q13()
			elif 't' ==self.caracter:
				self.q19()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()
		def q13(self):
			self.caracter = self.obter_caracter()
			if 'u' == self.caracter:
				self.q14()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q14(self):
			self.caracter = self.obter_caracter()
			if 'a' == self.caracter:
				self.q15()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q15(self):
			self.caracter = self.obter_caracter()
			if 'n' == self.caracter:
				self.q16()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q16(self):
			self.caracter = self.obter_caracter()
			if 't' == self.caracter:
				self.q17()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q17(self):
			self.caracter = self.obter_caracter()
			if 'o' == self.caracter:
				self.q18()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q18(self): 
			'''Reconhece o comando todo ENQUANTO'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["enquanto", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["enquanto", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["enquanto", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q19(self):
			self.caracter = self.obter_caracter()
			if 'a' == self.caracter:
				self.q20()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q20(self):
			self.caracter = self.obter_caracter()
			if 'o' == self.caracter:
				self.q21()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q21(self): 
			'''Reconhece o comando todo ENTAO'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["entao", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["entao", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["entao", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()


		def q22(self):
			self.caracter = self.obter_caracter()
			if 'i' == self.caracter:
				self.q23()
			elif 'a' == self.caracter:
				self.q27()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q23(self):
			self.caracter = self.obter_caracter()
			if 'm' == self.caracter:
				self.q24()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q24(self): 
			'''Reconhece o comando todo FIM'''
			self.caracter = self.obter_caracter()
			if 's' == self.caracter:
				self.q25()
			elif self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["fim", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["fim", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["fim", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q25(self):
			self.caracter = self.obter_caracter()
			if 'e' == self.caracter:
				self.q26()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q26(self): 
			'''Reconhece o comando todo FIMSE'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["fimse", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["fimse", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["fimse", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q27(self):
			self.caracter = self.obter_caracter()
			if 'c' == self.caracter:
				self.q28()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q28(self):
			self.caracter = self.obter_caracter()
			if 'a' == self.caracter:
				self.q29()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q29(self): 
			'''Reconhece o comando todo FACA'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["faca", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["faca", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["faca", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q30(self):
			self.caracter = self.obter_caracter()
			if 'e' == self.caracter:
				self.q31()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()
		
		def q31(self): 
			'''Reconhece o comando todo SE'''
			self.caracter = self.obter_caracter()
			if 'n' == self.caracter:
				self.q32()
			elif self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["se", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["se", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["se", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q32(self):
			self.caracter = self.obter_caracter()
			if 'a' == self.caracter:
				self.q33()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q33(self):
			self.caracter = self.obter_caracter()
			if 'o' == self.caracter:
				self.q34()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q34(self): 
			'''Reconhece o comando todo SENAO'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["senao", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["senao", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["senao", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q35(self):
			self.tabela_simbolos.append([";", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()

		def q36(self):
			self.tabela_simbolos.append(["(", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()

		def q37(self):
			self.tabela_simbolos.append([")", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()


		def q38(self): 
			self.tabela_simbolos.append(["+", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()

		def q39(self):
			self.caracter = self.obter_caracter()
			self.tabela_simbolos.append(["-", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()


		def q40(self):
			self.tabela_simbolos.append(["*", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()


		def q41(self):
			self.tabela_simbolos.append(["/", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()


		def q42(self):
			self.tabela_simbolos.append(["=", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()


		def q43(self):
			self.tabela_simbolos.append([">", self.lexema, self.numero_linha, self.cabeca])
			self.lexema = ''
			self.q0()

			"""def q44(self):
				self.caracter = self.obter_caracter()
				if '-' == self.caracter:
					self.q45()
				else:
					print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
					exit()"""

		def q45(self): 
			"""atribuicao"""
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append([":", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append([":", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais or self.caracter.isdigit() or self.caracter.islower():
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append([":", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q46(self): 
			"""NUMERO"""
			self.caracter = self.obter_caracter()
			while self.caracter.isdigit():
				self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter: #fim linha
				self.tabela_simbolos.append(["numero", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
			elif self.caracter.isspace(): #proximo token sem quebra de linha
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.lexema = self.tabela_simbolos.append(["numero", self.lexema, self.numero_linha , self.cabeca -1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais:
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["numero", self.lexema, self.numero_linha, self.cabeca -1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q47(self): 
			'''ID''' 
			self.caracter = self.obter_caracter()
			while self.caracter.isdigit() or self.caracter.islower():
				self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter: #fim linha
				self.tabela_simbolos.append(["id", self.lexema, self.numero_linha, self.cabeca -1 ])
				self.lexema = ''
			elif self.caracter.isspace(): #proximo token sem quebra de linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["id", self.lexema, self.numero_linha , self.cabeca -1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais:
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.tabela_simbolos.append(["id", self.lexema, self.numero_linha , self.cabeca -1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()
				
		def q48(self):
			self.caracter = self.obter_caracter()
			if 'n' == self.caracter:
				self.q49()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q49(self):
			self.caracter = self.obter_caracter()
			if 'i' == self.caracter:
				self.q50()
			elif 't' == self.caracter:
				self.q54()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q50(self):
			self.caracter = self.obter_caracter()
			if 'c' == self.caracter:
				self.q51()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		def q51(self):
			self.caracter = self.obter_caracter()
			if 'i' == self.caracter:
				self.q52()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()


		def q52(self):
			self.caracter = self.obter_caracter()
			if 'o' == self.caracter:
				self.q53()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			elif self.caracter.isspace():
				self.lexema = self.lexema[:len(self.lexema) -1]
				self.cabeca -= 1
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()
		

		def q53(self): 
			'''Reconhece o comando todo INICIO'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["inicio", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["inicio", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["inicio", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()

		
		def q54(self): 
			'''Reconhece o comando todo int'''
			self.caracter = self.obter_caracter()
			if self.fim_linha == self.caracter:
				self.tabela_simbolos.append(["int", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
			elif self.caracter.isspace(): #deve ser lido o proximo token sem quebrar a linha
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["int", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.q0()
			elif self.caracter in self.especiais: #deve-se retornar a cabeça de leitura e descarte
				self.lexema = self.lexema[:len(self.lexema) - 1]
				self.tabela_simbolos.append(["int", self.lexema, self.numero_linha, self.cabeca - 1])
				self.lexema = ''
				self.cabeca -= 1
				self.q0()
			elif self.caracter.isdigit() or self.caracter.islower():
				self.q47()
			else:
				print("Erro Léxico ({0},{1}): Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
				exit()


	tabela_tokens = lexico(sys.argv[2]).tabela_tokens()

	if(sys.argv[1] == '-lt'):
		print("\n[TOKENS,LEXEMA,LINHA,COLUNA")
		for token in range(len(tabela_tokens)):
			print(tabela_tokens[token])
except:
	print('Seu codigo!')