def verificar_parenteses(expressao):
    pilha = []
    
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha: 
                return False
            pilha.pop()
    return len(pilha) == 0

expressao = input('Digite uma expressão com parênteses:')
 
if verificar_parenteses(expressao):
    print('Os parênteses estão na ordem correta:')
else:
    print('Os parênteses não estão na ordem correta.')
     