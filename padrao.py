
# Tenho a linha 
#   CNPJ           CEP      IDADE  ESTADO 
#  "12345678000190 01001000 35 SP"
# Preciso que este arquivo saia em um padrao 
# incluir 011 entre o final do cep e inicio da idade

# Tratar arquivo e gerar padrão saida como TXT 
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
    "22334455000188 70040900 60 DF"
]

# Abre um arquivo txt para escrita
with open("resultados.txt", "w") as arquivo:
    for linha in linhas:
        nova_linha = incluir_codigos(linha)
        arquivo.write(nova_linha + "\n")

print("Resultados salvos em 'resultados.txt'")

# A Saida do Arquivo ficaria assim 

# 123456780001900960100100001135SP
# 987654320001980962203103001128RJ
# 456789120001760963030155001142MG
# 112233440001550966503020001150BA
# 998877660001220969085034001119PR
# 223344550001880967004090001160DF
