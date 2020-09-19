#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Transformações Geométricas de Imagens

Em geometria, transformação se refere ao movimento de objetos no plano de coordenadas. Transformações envolvem mover um
objeto de sua posição original para uma nova posição. Cada ponto no objeto é mapeado para outro ponto na imagem. Dado
que imagens digitais são representadas na forma de matrizes de dados, conceitos de geometria e álgebra linear acabam
sendo aplicados no processamento de imagens naturalmente. 

Transformações geométricas são aplicadas a vários tipos de imagens com diferentes finalidades. Por exemplo, existem
transformações voltadas à correção de distorções, estimativa de movimento, criação de imagens panorâmicas, entre outros.

Neste tutorial veremos como o OpenCV executa os 4 principais tipos de transformações geométricas:
    - Translação;
    - Rotação;
    - Dilatação;
    - Reflexão.

Para executar este código, utilize o seguinte comando em seu terminal:
$ python transformation.py -i ../99_Images/summer.jpg

Referências:

Adrian Rosebrock. OpenCV Tutorial: a guide to learn OpenCV. PyImageSearch. Disponível em:
https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/. Acesso em: 08 set. 2020.

Ana Huamán. Affine Transformations. OpenCV Docs. Disponível em:
https://docs.opencv.org/4.0.0/d4/d61/tutorial_warp_affine.html. Acesso em: 15 set. 2020.

Ana Huamán. Remapping. OpenCV Docs. Disponível em:
https://docs.opencv.org/4.0.0/d1/da0/tutorial_remap.html. Acesso em: 15 set. 2020.

Fernando V. Paulovich. Transformações Geométricas 2D. Instituto de Ciências Matemáticas e de Computação (ICMC).
Disponível em: http://wiki.icmc.usp.br/images/a/a5/TransfGeometricas2D.pdf. Acesso em: 15 set. 2020.

"""

__author__ = "Eloi Giacobbo"
__copyright__ = 'Copyright 2020, OpenCV Python Tutorial'
__credits__ = ["Emili Bohrer"]
__license__ = "GPL-3.0"
__version__ = "0.1.0"
__maintainer__ = "Eloi Giacobbo"
__status__ = "Development"

# Em main, definimos a função principal do arquivo, onde as operações com imagens são executadas


def main(image_path, verbose=False):
    """ Transformações Geométricas de Imagens

    Args:
        image_path (str): Endereço da imagem a ser manipulada.
        verbose (bool, optional): Modo verbose. Desativado por padrão.
    """

    # Primeiro, devemos incluir as bibliotecas necessárias.
    import cv2
    import errno
    import numpy as np
    import os
    import imutils

    # Utilizando o parâmetro image_path, a imagem selecionada é carregada através do comando cv2.imread.
    original = cv2.imread(image_path)

    # Check if a valid image was read
    if (original is None):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image_path)

    # Vamos imprimir a imagem original como referência
    cv2.imshow("Original", original)

    # Em seguida, registramos as dimensões da imagem
    (height, width) = original.shape[:2]

    # Inicialmente, veremos como realizar translações. O OpenCV realiza transformações geoméricas através da função
    # cv2.warpAffine. Esta função recebe como parâmetro de entrada a imagem original, a matriz de transformação desejada
    # e as dimensões da imagem de saída. A matriz transformação deve possuir dimensões 2 x 3 e tipo de dado float32.
    # Pela teoria de transformações geométricas, temos que matrizes de transformação 2D possuem dimensões 3 x 3. Porém,
    # a terceira linha destas matrizes é sempre constante e o OpenCV nos oferece uma abstração desta informação através
    # da função cv2.warpAffine. Se estiver interessado, confira o material disponibilizado pelo Professor Fernando V.
    # Paulovich para relembrar um pouco mais sobre transformaçoes geométricas.

    # Dito isto, podemos seguir para nossa implementação da operação de translação em imagens. Primeiro definioms as
    # coordenadas a serem utilizadas na translação e, em seguida, definimos as duas primeiras linhas da matriz de
    # translação. Para executar esta operação, lembre-se de como o sistema de coordenadas de imagens é definido pelo
    # OpenCV. Sendo assim, valores de positivos de translação em X movimentam uma imagem para direita e valores
    # negativos movimentam uma imagem para esquerda. Valores de positivos de translação em Y movimentam uma imagem para
    # baixo e valores negativos movimentam uma imagem para cima.
    Tx = 50
    Ty = 100
    M = np.float32([[1, 0, Tx],
                    [0, 1, Ty]])
    translated = cv2.warpAffine(original, M, (width, height))

    # Agora, imprimimos o resultado da translação da imagem que movimenta a imagem em 50 pixels para a direita e 100
    # pixels para baixo.
    cv2.imshow("Translated", translated)
    cv2.waitKey(0)

    # Nesta segunda operação, movimantamos a imagem em 100 pixles para a esquerda e 50 pixels para cima. Note que parte
    # da imagem do conteúdo da imagem foi perdido na operação anterior, pois parte dos dados foi transladado além dos
    # limites da imagem.
    Tx = -100
    Ty = -50
    M = np.float32([[1, 0, Tx],
                    [0, 1, Ty]])
    translated = cv2.warpAffine(translated, M, (width, height))
    cv2.imshow("Translated", translated)
    cv2.waitKey(0)

    # Para evitar esta perda de informações, podemos aumentar o tamanho da imagem de saída conforme necessário.
    M = np.float32([[1, 0, 50], [0, 1, 100]])
    translated = cv2.warpAffine(original, M, (width + 50, height + 100))
    cv2.imshow("Translated", translated)
    cv2.waitKey(0)

    M = np.float32([[1, 0, -50], [0, 1, -100]])
    translated = cv2.warpAffine(translated, M, (width, height))
    cv2.imshow("Translated", translated)
    cv2.waitKey(0)

    # Para facilitar a execução de translações, podemos utilizar a função disponível na biblioteca imutils. Esta
    # biblioteca possui uma série de funções que facilita a execução diversas operações sobre imagens. A função
    # imutils.translate, por exemplo, necessita receber a imagem original e as coordenadas de translação para executar
    # esta transformação. Devemos apenas tomar cuidado com a perda de informações ao usar a translação de imutils.
    translated = imutils.translate(original, Tx, Ty)
    cv2.imshow("Translated", translated)
    cv2.waitKey(0)
    cv2.destroyWindow("Translated")

    # A segunda transformação que veremos neste tutorial é a de rotação. Através de uma matriz de rotação somos capazes
    # de rotacionar uma imagem em torno da origem do sistema de coordenadas. Para esta operação, utilizamos a matriz
    # de transformação apresentada abaixo para rotacionar a imagem original em 45 graus.
    teta = np.deg2rad(45)
    M = np.float32([[np.cos(teta), -np.sin(teta), 0],
                    [np.sin(teta), np.cos(teta), 0]])
    rotated = cv2.warpAffine(original, M, (width, height))
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)

    # Podemos perceber que esta já é uma operação um pouco mais complexa. Para executar uma rotação precisamos utilizar
    # funções de cálculo seno, cosseno e conversões entre graus e radianos. Ainda assim, percebemos que o resultado
    # desta operação não foi satisfatório, pois parte dos dados da imagem foi perdido. Para facilitar o uso desta
    # operação, podemos fazer uso de uma função utilitária do OpenCV, a função cv2.getRotationMatrix2D. Esta função
    # recebe como parâmetros as coordenadas do eixo de rotação desejado, o ângulo de rotação e um fator de escala para
    # redimensionamento da imagem. Sendo assim, na operação iremos rotacionar a imagem original em 45 graus mais uma
    # vez. Porém, agora tomaremos o eixo de rotação como o centro da imagem.
    center = (width // 2, height // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1)
    rotated = cv2.warpAffine(original, M, (width, height))
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)

    # Como resultado, temos novamente a imagem rotacionada em 45 graus. Como esta imagem foi rotacionada em torno de seu
    # centro, a perda de informações um pouco menor e somos capazes de enchergar uma área maior da imagem rotacionada.
    # Note que esta rotação foi realizada no sentido anti-horário. A função getRotationMatrix2D considera ângulos
    # positivos como rotações no sentido anti-horário e ângulos negativos como rotações no sentido horário. Agora nos
    # resta apenas resolver o problema da perda de informações para completarmos uma rotação perfeita.

    # Para evitar a perda de informações em uma rotação, não basta simplesmente aumentar o tamanho da imagem de saída.
    # Precisamos efetuar uma série de operações. Primeiro, precisamos cálcular a largura e altura da imagem de saída
    # utilizando trigonometria. Em seguida, temos que transladar a imagem para o seu novo ponto central e, finalmente,
    # podemos seguir para a operação de rotação.

    # Cálculo das dimensões finais
    teta = 45
    teta_rad = np.deg2rad(teta % 90)
    width_r = int(np.ceil(width * np.cos(teta_rad) + height * np.sin(teta_rad)))
    height_r = int(np.ceil(width * np.sin(teta_rad) + height * np.cos(teta_rad)))
    center_r = (width_r // 2, height_r // 2)

    # Translação inicial
    M = np.float32([[1, 0, (center_r[0] - center[0])], [0, 1, (center_r[1] - center[1])]])
    rotated = cv2.warpAffine(original, M, (width_r, height_r))

    # Rotação
    M = cv2.getRotationMatrix2D(center_r, teta, 1)
    rotated = cv2.warpAffine(rotated, M, (width_r, height_r))
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)

    # Uma vez que vimos todos os detalhes sobre operações de rotação, podemos utilizar novamente uma função disponível
    # na biblioteca imutils para facilitar nosso trabalho. Podemos utilizar a função imutils.rotate para executar
    # rotações simples, fornecendo apenas a imagem a ser rotacionada e o ângulo de rotação. Ou então, podemos utilizar a
    # função imutils.rotate_bound quando desejamos rotacionar uma imagem sem nos preocuparmos com perda de informações.
    # Infelizmente, o parâmetro de ângulo destas funções não foi padronizado e precisamos ter cuidado com o sentido de
    # rotação de imagens ao usar a biblioteca imutils. imutils.rotate rotaciona imagens no sendido horário quando
    # inserimos ângulos positivos, enquanto imutils.rotate_bound rotaciona imagens no sentido anti-horário.
    rotated = imutils.rotate(original, 45)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)
    rotated = imutils.rotate_bound(original, -45)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)
    cv2.destroyWindow("Rotated")

    # A próxima transformação que vamos abordar neste tutorial é a dilatação. Em outras palavras, veremos como
    # redimensionar imagens através do OpenCV. No código a seguir a matriz de dilatação é implementada. Esta é uma
    # transformações bastante simples de se definir, precisamos apenas ter o cuidado de manter as dimensões da imagem
    # com valores inteiros.
    scale = 0.5
    width_r = int(np.ceil(width * scale))
    height_r = int(np.ceil(height * scale))
    M = np.float32([[1 * scale, 0, 0], [0, 1 * scale, 0]])
    resized = cv2.warpAffine(original, M, (width_r, height_r))
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)

    # Ainda assim, o OpenCV nos oferece também a função cv2.resize que facilita a execução desta operação. O uso da
    # função resize é ainda mais simples, precisamos apenas inserir a imagem original e o tamanho desejado para realizar
    # o redimensionamento.
    resized = cv2.resize(original, (width * 2, height * 2))
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)

    # Opcionalmente, podemos definir o parâmetro de interpolação para definir o método de redimensionamento utilizado.
    resized = cv2.resize(original, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)
    cv2.destroyWindow("Resized")

    # A última transformação que abordaremos neste arquivo é a chamada reflexão. Esta operação nos permite espelhar uma
    # imagem sobre o eixo X e/ou Y do sistema de coordenadas. No entanto, não podemos utilizar a matriz de transformação
    # usual para implementar esta operação. Ao refletirmos uma imagem sobre um eixo, nossa imagem deixaria de estar
    # presente no primeiro quadrante do sistema de coordanadas. Como sabemos, não somos capazes de efetivamente definir 
    # coordenadas negativas em um ndarray. Felizmente, o OpenCV nos oferece também uma função para realizar operações de
    # reflexão. O método cv2.flip recebe como parâmetro a imagem original e uma variável de seleção do tipo de reflexão.
    # Quando inserido o valor 1 a imagem de entrada será refletida na horizontal, com o valor 0 a imagem será refletida
    # na vertical e quando inserimos -1 a reflexão ocorre em ambas as direções.
    reflected = cv2.flip(original, 0)
    cv2.imshow("Reflected", reflected)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


# Para finalizar, realizamos a chamada da função main, que receberá parâmetros a partir da linha de comandos
if __name__ == '__main__':
    # Construção e execução do decodificador parâmetros de linha de comando
    import argparse
    parser = argparse.ArgumentParser(description="Transformações Geométricas de Imagens")
    parser.add_argument("-i", "--image", required=True, help="Endereço de Imagem")
    parser.add_argument("-v", "--verbose", default=False, help="Modo Verbose")
    args = parser.parse_args()
    # Chamada da função main, que recebe os comandos de linha
    main(args.image, args.verbose)
