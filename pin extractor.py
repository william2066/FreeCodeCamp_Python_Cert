# 🛡️ Script: Extrator de PIN de Segurança (Labs freeCodeCamp)
# Objetivo: Aprender a lidar com loops aninhados e proteção de memória (Index Check)

def pin_extractor(poems):
    # Criamos uma lista vazia para armazenar os resultados de forma organizada
    secret_codes = [] 
    
    # Loop externo: Percorre cada 'poema' (ou bloco de dados) dentro da lista recebida
    for poem in poems:
        secret_code = ''  # Resetamos o código para cada novo poema
        lines = poem.split('\n')  # Quebra o texto em linhas individuais
        
        # Loop interno: Analisa linha por linha, rastreando o índice (posição)
        for line_index, line in enumerate(lines):
            words = line.split()  # Quebra a linha em palavras
            
            # 🛡️ VALIDAÇÃO DE SEGURANÇA (Crucial em Cyber):
            # Antes de acessar um índice, verificamos se a lista de palavras é grande o suficiente.
            # Isso evita o erro 'Index Out of Bounds' se a linha for muito curta.
            if len(words) > line_index:
                # Pega o comprimento da palavra que está na posição da linha atual
                secret_code += str(len(words[line_index]))
            else:
                # Se a linha for curta demais, preenchemos com '0' para manter o padrão
                secret_code += '0'
        
        # Adiciona o código gerado deste poema à nossa lista final de resultados
        secret_codes.append(secret_code)
                
    return secret_codes

# --- ÁREA DE TESTES (Simulação de inputs de dados) ---

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nnonce\nwas\nna\ndragon'

# Chamada da função passando a lista completa de "logs" (poemas)
print("--- RELATÓRIO DE CÓDIGOS EXTRAÍDOS ---")
print(pin_extractor([poem, poem2, poem3]))