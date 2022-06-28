.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
LDR R0, =format2       @load addres of pattern number
LDR R1, =cont       @load addres of variable
BL scanf  @call function for leia
LDR R0, =cont      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for escreva
MOV R0, #69      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
LDR R0, =a      @load address
STR R1, [R0]      @store  result
MOV R0, #26      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
LDR R0, =b      @load address
STR R1, [R0]      @store  result
LDR R0, =a      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}          @pops R0
MOV R1, R0        @mov content for R1
LDR R0, =b      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
BGE L2      @case Val1<Val2
L1:      @label content se
LDR R0, =a      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack result content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for escreva
B L3      @jump for fimse
L2:      @label for senao
L6:      @label for `enquanto`
L4:      @label content `enquanto`
LDR R0, =b      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
MOV R0, #1      @load number
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
L6:      @label for fimEnquanto-Faca
LDR R0, =b      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack result content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for escreva
L5:      @label for fimse
pop {ip, pc}
.data
.balign 8
format: .asciz "%d\n" 
format2: .asciz "%d" 
.balign 8
cont: .word 0
.balign 8
a: .word 0
.balign 8
b: .word 0
.extern printf
.extern scanf
