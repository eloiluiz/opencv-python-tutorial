#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Operações Básicas com Imagens em Python

Imagens são representadas pelo OpenCV na forma de vetores Numpy com 3 dimensões. Cada imagem é composta por linhas e
colunas de pixels e cada pixel é representado por um vetor que define sua cor.

Este tutorial tem como objetivo apresentar métodos bastante comuns de manipulação de imagens. Cada uma destas
ferramentas possuem utilidade no ramo de visão computacional. Porém, tais aplicações não serão abordadas neste primeiro
momento. As operações apresentadas neste arquivo estão principalmente relacionadas ao uso da biblioteca Numpy, ao invés
do OpenCV. Um bom conhecimento de Numpy é necessário para escrever códigos mais otimizados com OpenCV.

Neste primeiro tutorial veremos como:
    - Visualizar propriedades de imagens;
    - Acessar e manipular pixels;
    - Definir regiões de imagem (ROI - Region of Image);
    - Criar bordas em imagens.
    - Manipular escalas de cores;
    - Dividir e combinar canais de cores.

Para executar este código, utilize o seguinte comando em seu terminal:
$ python image.py -i ../99_Images/summer.jpg

As interpretações e comentários realizados ao longo deste arquivo tomam por base o uso da imagem "summer.jpg", presente
no diretório ../99_Images.

Referências:

Adrian Rosebrock. OpenCV Tutorial: a guide to learn OpenCV. PyImageSearch. Disponível em:
https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/. Acesso em: 08 set. 2020.

Alexander Mordvintsev; Abid K. Basic Operations on Images. OpenCV-Python Tutorials. Disponível em:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html. Acesso em:
08 set. 2020.

argparse: parser for command-line options, arguments and sub-commands. Python Software Foundation. Disponível em:
https://docs.python.org/3/library/argparse.html. Acesso em: 08 set. 2020.

Mohammed Innat. Basic Image Processing In Python: part 1. Codementor Community. Disponível em:
https://www.codementor.io/@innat_2k14/image-data-analysis-using-numpy-opencv-part-1-kfadbafx6. Acesso em: 11 set. 2020.

"""

__author__ = "Eloi Giacobbo"
__copyright__ = 'Copyright 2020, OpenCV Python Tutorial'
__credits__ = ["Emili Bohrer"]
__license__ = "GPL-3.0"
__version__ = "0.1.2"
__maintainer__ = "Eloi Giacobbo"
__status__ = "Development"

# Em main, definimos a função principal do arquivo, onde as operações com imagens são executadas
def main(image_path, verbose=False):
    """ Operações Básicas com Imagens

    Args:
        image_path (str): Endereço da imagem a ser manipulada.
        verbose (bool, optional): Modo verbose. Desativado por padrão.
    """

    # Primeiro, devemos incluir as bibliotecas necessárias.
    import numpy as np
    import cv2
    import errno
    import os
    import matplotlib.pyplot as plt

    # Utilizando o parâmetro image_path, a imagem selecionada é carregada através do comando imread do módulo cv2.
    image = cv2.imread(image_path)

    # Check if a valid image was read
    if (image is None):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image_path)

    # Ao imprimir o objeto image, vemos que este se trata de uma matrix de arrays.
    print("Image =\n", image)

    # Podemos agora imprimir algumas propriedades deste objeto
    # shape apresenta as dimensões da imagem carregada, onde:
    # height representa o número de linhas ou a altura da imagem
    # width representa o número de colunas ou a largura da imagem
    # dept representa o número de canais de cores da imagem (e.g Grayscale, RGB, etc.).
    (height, width, depth) = image.shape
    print("\nImage Shape = (height = ", height, ", width = ", width, ", depth = ", depth, ")", sep="")

    # O tipo de dados padrão de imagens do OpenCV é uint8, visto que pixels são representados por valores entre 0 e
    # 255. Um grande número de erros no OpenCV é causado pela definição incorreta do tipo de dados de imagens.
    print("\nImage Dtype =", image.dtype)

    # A função imshow do módulo cv2 cria uma nova janela e imprime em tela o conteúdo da imagem.
    cv2.imshow("Image", image)

    # A função waitkey do módulo cv2 executa uma pausa na execução do código e aguarda que uma tecla seja pressionada em
    # uma janela do OpenCV. Note que o OpenCV não possui interface com o console, apenas com as janelas criadas pelo
    # próprio módulo. Seu parâmetro de entrada define o tempo que será aguardado para a captura de teclas, em
    # milisegundos. Caso o valor de entrada seja zero, esta pausa será por tempo indeterminado, até que uma tecla seja
    # pressionada. Esta função retorna o valor ASCII da tecla pressionada ou -1 se nenhuma teca for pressionada. O uso
    # da função waitKey é especialmente importante para a impressão de imagens através do módulo cv2. O módulo cv2 não
    # pausa a execução de um código quando imagens são impressas em tela. Quando a execução de um código chega ao final,
    # todas as imagens impressas em tela são encerradas automaticamente. Sem o uso de pausas, um usuário pode ter
    # dificuldades em visualizar o conteúdo de imagens.
    cv2.waitKey(0)

    # O valor de um pixel específico ou um intervalo de pixels podem ser selecionados através de índices de vetor:
    print("\nPixel =", image[0, 0])
    print("\nPixel Interval =\n", image[300:302, 50:52])

    # Como parte dos atributos de ndarray, uma cópia do conteúdo de uma imagem pode ser obtida através do método copy.
    # Utilizaremos esta cópia para alterar o conteúdo da imagem original.
    copy = image.copy()

    # O mesmo método utilizado para o acesso de pixels pode ser utilizado também para redefinir os pixels de uma imagem.
    # Nas operações a seguir, redefinimos o pixel de coordenada (0, 0) para a cor vermelha e uma área da imagem entre as
    # cordenadas (250:300, 50:100) para a cor azul.
    copy[0, 0] = (0, 0, 255)
    copy[250:300, 50:100] = (255, 0, 0)

    # Para imprimir a imagem original e sua cópia lado-a-lado, o método hstack pode ser utilizado para empilhar imagens
    # horizontalmente.
    stacked = np.hstack((image, copy))
    cv2.imshow("Image", stacked)
    cv2.waitKey(0)

    # Outra operação comum no processamento de imagem é a definições de regiões de imagem (ROI). Através deste método
    # somos capazes de separar regiões de interesse em uma imagem maior, podendo tratá-las separadamente. Para executar
    # esta operação, iremos recorrer novamente ao método de acesso às regiões de pixel desejadas.
    roi = image[50:149, 87:189]

    # Ao atribuir esta região de imagem a uma nova variável somos capazes de criar uma nova imagem.
    cv2.imshow("Image", roi)
    cv2.waitKey(0)

    # Quando desejado, podemos ainda inserir molduras em uma imagem com a função copyMakeBorder do módulo cv2. Esta
    # recebe como argumento a largura de cada seção moldura (top, botton, left, right) e o tipo de moldura.
    constant = cv2.copyMakeBorder(roi, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 255])
    reflect = cv2.copyMakeBorder(roi, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    replicate = cv2.copyMakeBorder(roi, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    wrap = cv2.copyMakeBorder(roi, 10, 10, 10, 10, cv2.BORDER_WRAP)
    padding = np.hstack((constant, reflect, replicate, wrap))
    cv2.imshow("Image", padding)
    cv2.waitKey(0)

    # Quando necessário, o método destroyAllWindows do módulo cv2 pode ser chamado para encerrar todas as janelas
    # abertas pelo OpenCV.
    cv2.destroyAllWindows()

    # Como alternativa ao imshow do OpenCV, outras bibliotecas de impressão podem ser utilizadas, como o Matplotlib.
    # Diferente do módulo cv2, o Matplotlib pausa automaticamente a execução de um código enquanto sua janela estiver
    # aberta. Para seguir com a execução de um código, seu usuário precisa fechar a janela da imagem.
    plt.figure()
    plt.axis('off')
    plt.imshow(image)
    plt.show()

    # Note que há uma grande diferença entre o padrão de cores da imagem gerada pelo OpenCV e pelo Matplotlib. As
    # bibliotecas do OpenCV estão em desenvolvimento desde o ano 2000. Nesta época o padrão de cores mais utilizado
    # era o BGR, não o RGB que conhecemos hoje. Para manter a compatibilidade da biblioteca com sistemas mais antigos,
    # o OpenCV mantém até hoje o BGR como escala de cores padrão. Por esta razão, devemos tomar cuidado ao manipular
    # cores de imagens e sempre ter em mente qual padrão de cores está em uso numa aplicação. Felizmente, o OpenCV nos
    # oferece ferramentas que nos permitem converter o padrão de cores em imagens com facilidade. Podemos, por exemplo,
    # converter o padrão de cores do objeto stacked para RGB e possibilitar sua correta impressão via Matplotlib.
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Após sua conversão, as funções de impressão do Matplotlib são chamadas novamente.
    plt.figure()
    plt.axis('off')
    plt.imshow(rgb)
    plt.show()

    # Para exercitar os métodos que vimos até o momento, podemos criar uma única imagem com diferentes padrões de cores
    # ao utilizar o método de conversão de cores em partes separadas de uma mesma imagem.
    color = image.copy()
    color[0:160, 161:320] = cv2.cvtColor(color[0:160, 161:320], cv2.COLOR_BGR2RGB)
    color[161:320, 0:160] = cv2.cvtColor(color[161:320, 0:160], cv2.COLOR_BGR2HLS)
    color[161:320, 161:320] = cv2.cvtColor(color[161:320, 161:320], cv2.COLOR_BGR2LAB)
    cv2.imshow("Image", color)
    cv2.waitKey(0)

    # Ainda sobre conversões de padrões de cores, devemos nos atentar ao número de canais que cada padrão de cores
    # possui. Ao convertermos uma imagem para escala de cinza, por exemplo, é possível verificar que o número de canais
    # da imagem é reduzido para apenas 1. Uma vez convertida para escala de cinza, uma imagem não podera ser facilmente
    # retornada para padrões com múltiplos canais, pois informações foram perdidas na conversão.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("\nGray Shape =", gray.shape)
    cv2.imshow("Image", gray)
    cv2.waitKey(0)

    # Perceba que ao converter uma imagem em escala de cinza novamente para BGR, o número de canais da imagem volta a
    # ser 3. Porém, a imagem permanace com sua coloração em escala de cinza.
    bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    print("\nBGR Shape =", bgr.shape)
    cv2.imshow("Image", bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Ao analisar os dados contidos nos objetos de imagem, é possível observar a redução no número de canais da imagem
    # após a conversão para escala de cinza. Também observamos que a conversão seguinte cria cópias deste único canal
    # para completar os canais faltantes do padrão BGR e não é capaz retornar a imagem para o estado original.
    print("\nImage Data =\n", image[100:105, 240])
    print("\nGray Data =\n", gray[100:105, 240])
    print("\nBGR Data =\n", bgr[100:105, 240])

    # Os canais BGR de uma imagem podem ser divididos em planos individuais quando necessário. Esta separação nos
    # permite avaliar o quanto cada componente de cor está presente em uma imagem. Em seguida, os canais individuais
    # podem ser mesclados novamente para formar uma imagem BGR.
    (b, g, r) = cv2.split(roi)
    merged = cv2.merge((b, g, r))
    stacked = np.hstack((roi, merged))
    cv2.imshow("ROI-Merged", stacked)
    stacked = np.hstack((b, g, r))
    cv2.imshow("Blue-Green-Red", stacked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Como você deve ter notado, o resultado da separação dos canais resulta mais uma vez em imagens em escala de cinza.
    # Após a separação de canais, temos 3 novos objetos com um único canal de cor. Por padrão, o OpenCV interpreta
    # imagens com um único canal em escala de cinza. E como devemos interpretar estas imagens? Quanto mais próximo da
    # cor branca um pixel estiver, maior é a presença do canal de cor ele representa sobre a imagem original. Quanto
    # mais próximo da cor preta um pixel estiver, menor é a presença do canal de cor ele representa sobre a imagem
    # original.

    # Para facilitar a identificação de cada canal e a interpretação de sua imagem, podemos agora ajustar estes objetos
    # para uma representação em 3 canais, preenchendo os canais faltantes com zeros. Desta forma teremos uma visão mais
    # clara da participação de cada canal de cor na formação da imagem original.
    (height, width, depth) = roi.shape
    zeros = np.zeros((height, width), dtype="uint8")
    b = cv2.merge((b, zeros, zeros))
    g = cv2.merge((zeros, g, zeros))
    r = cv2.merge((zeros, zeros, r))
    stacked = np.hstack((roi, b, g, r, merged))
    cv2.imshow("ROI-Blue-Green-Red-Merged", stacked)
    cv2.waitKey(0)

    # Como resultado, fica evidente qual canal de cor cada uma destas imagens representa, assim como sua interpretação.
    # Quanto mais próximo um pixel estiver da cor de seu canal, maior é a presença desta cor sobre a imagem original.
    # Quanto mais próximo da cor preta um pixel estiver, menor é a presença do canal de cor ele representa sobre a
    # imagem original. Note, por exemplo, como o fundo de todas as imagens é representado pela cor pura de seu canal.
    # Isto se deve pelo fato de que o fundo desta imagem é branco. Observe também as diferenças entre os canais nos
    # contornos e a no preenchimento deste sol. As bordas possuem pouca presença de cada canal, por ser desenhada na cor
    # preta. Já o preenchimento do sol possui certa presença dos canais verde e vermelho para formar os tons de laranja
    # desta imagem.

    # Uma vez que todas todas as operações com imagens deste tutorial foram apresentadas, podemos finalizar a execução
    # main ao salvar nossa última em imágem em disco. O método imwrite do módulo cv2 é capaz de realizar a escrita de um
    # objeto de imagem no caminho indicado.
    cv2.imwrite("output_image.jpg", stacked)
    cv2.destroyAllWindows()


# Para finalizar, realizamos a chamada da função main, que receberá parâmetros a partir da linha de comandos
if __name__ == '__main__':
    # Construção e execução do decodificador parâmetros de linha de comando
    import argparse
    parser = argparse.ArgumentParser(description="Operações Básicas com Imagens")
    parser.add_argument("-i", "--image", required=True, help="Endereço de Imagem")
    parser.add_argument("-v", "--verbose", default=False, help="Modo Verbose")
    args = parser.parse_args()
    # Chamada da função main, que recebe os comandos de linha
    main(args.image, args.verbose)
