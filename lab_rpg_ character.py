# Variáveis de estilo (Escopo Global)
full_dot = '●'
empty_dot = '○'

def create_character(name, STR, INT, CHAR):
    # 1. Validações do Nome
    if not isinstance(name, str):
        return 'The character name should be a string.'
    
    if name == '':
        return 'The character should have a name.'
    
    if len(name) > 10:
        return 'The character name is too long.'
    
    if ' ' in name:
        return 'The character name should not contain spaces.'

    # 2. Validação de Tipo (Apenas Inteiros)
    if not (isinstance(STR, int) and isinstance(INT, int) and isinstance(CHAR, int)):
        return 'All stats should be integers.'

    # 3. Validação de Valor Mínimo
    if STR < 1 or INT < 1 or CHAR < 1:
        return 'All stats should be no less than 1.'

    # 4. Validação de Soma (Checksum de 7 pontos)
    if STR + INT + CHAR != 7:
        return 'The character should start with 7 points.'

    # 5. Construção da Ficha Visual (Interface)
    # Note o uso de 'CHA' conforme a regra do lab
    line1 = name
    line2 = f"STR {full_dot * STR}{empty_dot * (10 - STR)}"
    line3 = f"INT {full_dot * INT}{empty_dot * (10 - INT)}"
    line4 = f"CHA {full_dot * CHAR}{empty_dot * (10 - CHAR)}"

    return f"{line1}\n{line2}\n{line3}\n{line4}"

# --- Exemplo de uso para teste ---
if __name__ == "__main__":
    # Criando um personagem equilibrado (2+2+3 = 7)
    print(create_character("Link", 2, 2, 3))