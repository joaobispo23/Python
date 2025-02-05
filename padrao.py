def incluir_codigos(linha):
    # Remove espaços extras
    linha_sem_espacos = "".join(linha.split())
    
    # Divide a linha nas partes componentes
    cnpj = linha_sem_espacos[:14]
    cep = linha_sem_espacos[14:22]
    idade = linha_sem_espacos[22:24]
    estado = linha_sem_espacos[24:]
    
    # Cria a nova linha com "096" entre CNPJ e CEP e "011" entre o final do CEP e o início da idade
    nova_linha = f"{cnpj}096{cep}011{idade}{estado}"
    return nova_linha

linhas = [
    "12345678000190 01001000 35 SP",
    "98765432000198 22031030 28 RJ",
    "45678912000176 30301550 42 MG",
    "11223344000155 65030200 50 BA",
    "99887766000122 90850340 19 PR",
    "22334455000188 70040900 60 DF",
    "12345678000190 01001000 35 SP",
    "98765432000198 22031030 28 RJ",
    "45678912000176 30301550 42 MG",
    "11223344000155 65030201 50 RS",
    "99887766000128 90850349 19 PR",
    "22334455000189 70040900 60 SP"
]

# Cria um conjunto para armazenar as linhas únicas
linhas_unicas = set()

# Abre um arquivo txt para escrita e insere o cabeçalho
with open("resultados.txt", "w") as arquivo:
    # Escreve o cabeçalho
    arquivo.write("CNPJ | CEP | IDADE | ESTADO\n")
    
    for linha in linhas:
        nova_linha = incluir_codigos(linha)
        # Adiciona a nova linha ao conjunto
        linhas_unicas.add(nova_linha)
    
    # Escreve as linhas únicas no arquivo
    for linha_unica in linhas_unicas:
        arquivo.write(linha_unica + "\n")

print("Resultados salvos em 'resultados.txt'")
