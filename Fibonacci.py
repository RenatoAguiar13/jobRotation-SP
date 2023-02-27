number = int(input("Escreva um número para verificar se faz parte da sequência de Fibonacci: "))

# Pelo que entendi a fórmula para a sequência é Fn=F(n-1)+F(n-2), onde 'n' seria o valor correspondente à variável 'number' então:

fn = 0
f1 = 0
f2 = 1

while fn < number:
    fn = f1 + f2
    f1 = f2
    f2 = fn

if fn == number:
    print(number, "Pertence à sequência.")
else:
    print(number, "Não pertence à sequência.")
