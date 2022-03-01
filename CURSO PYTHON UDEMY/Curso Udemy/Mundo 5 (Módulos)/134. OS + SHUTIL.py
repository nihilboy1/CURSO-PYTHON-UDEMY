import os
import shutil

caminho_original = 'I:\Downloads\exercicio_poo_banco'
caminho_novo = 'I:\Downloads\exercicio_poo_banco2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe!')

for root, dirs, files, in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        print(old_file_path)

        '''shutil.move(old_file_path, new_file_path)
        print(f'Arquivo{file} movido com sucesso')
        #mover arquivos
        '''
        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo{file} copiado com sucesso')

        '''
        com os.remove() eu consigo apagar os arquivos de uma pasta
        '''