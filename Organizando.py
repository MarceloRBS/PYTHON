# Cada linha desse algorítimo foi baseado em um vídeo que assistir no YouTube
# O canal é Programação Dinâmica
# https://www.youtube.com/watch?v=5vdEb_pitfc&lc=Ugzjd5XWzlVWNx2csPV4AaABAg.96yOET3N6IM97-MX-s9lV2
import os

# 1 Criar pastas: imagens, áudios, documentos, vídeos, outros
# 2 Pegar o nome dos arquivos
# 3 Pegar a extensão dos arquivos para determinar o tipo
# 4 Mover arquivos para as pastas correspondentes

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf']


def pegar_extensao(nome):
    index = nome.rfind(".")
    return nome[index:]


def organizar(diretorio):
    AUDIOS_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    DOCS_DIR = os.path.join(diretorio, "documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    OUTROS_DIR = os.path.join(diretorio, "outros")
    
    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIOS_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # Extensãp do arquivo em letras minúsculas
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = AUDIOS_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR
            # Move o arquivo para a pasta correspondente
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print(f'Moveu: {velho} -> {novo}')

# Atenção, certifíque-se de que este arquivo esteja no diretório que sofrerá as alterações
if __name__ == "__main__":
    organizar('Downloads')
