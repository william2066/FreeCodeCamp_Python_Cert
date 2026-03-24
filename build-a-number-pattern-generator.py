** start of main.py **

def number_pattern(n):
    # 1. Checagem de Tipo (Teste 6)
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    
    # 2. Checagem de Valor Positivo (Teste 7)
    if n <= 0:
        return 'Argument must be an integer greater than 0.'
    
    # 3. Lógica Principal
    pattern = ''
    for i in range(1, n + 1):
        pattern += str(i) + ' '
    
    return pattern.strip()
    
    
    
    
print(number_pattern(4))




** end of main.py **

