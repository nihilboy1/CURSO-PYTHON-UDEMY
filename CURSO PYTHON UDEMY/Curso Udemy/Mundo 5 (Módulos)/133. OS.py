import os

caminho_procura = input('Informe um caminho: ')
termo_procura = input('Informe um termo de busca: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        texto = 'B'
    if tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


c = 0
for raiz, pastas, arquivos in os.walk(caminho_procura):
    '''
    com o método walk eu consigo percorrer pelas pastas do pc
    raiz é o local geral
    pastas são as pastas no local
    e arquivos são os arquivos em cada pasta
    '''
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                c += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome do arquivo: ', nome_arquivo)
                print('Extensão do arquivo: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print(f'Tamanho real: {formata_tamanho(tamanho)}')
            except PermissionError as e:
                print('Sem permissão')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro!')
print('Arquivos encontados: ', c)
