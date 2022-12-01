#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Desenhando sobre Imagens

O OpenCV oferece várias funções para desenhar formas e linhas sobre imagens. Este conhecimento será muito útil mais
tarde, quando começarmos trabalhar com algoritmos de reconhecimento de imagens com OpenCV. Por exemplo, quando desejamos
desenhar um retângulo destacando os rostos ou objetos detectados em uma imagem processada.

As funções de desenho do OpenCV são fáceis de aprender pela semelhança entre suas interfaces. Os parâmetros para entrada
de uma imagem, cor e espessura estão presentes em todas as funções de desenho e possuem o mesmo comportamento.
Veremos mais detalhes sobre cada um destes parâmetros ao longo deste arquivo.

Neste tutorial, exploraremos algumas funções que podem nos ajudar a desenhar formas em imagens. São elas:
    - cv2.line();
    - cv2.rectangle();
    - cv2.circle();
    - cv2.ellipse();
    - cv2.putText().

Para executar este código, utilize o seguinte comando em seu terminal:
$ python drawing.py

Referências:

Adrian Rosebrock. OpenCV Tutorial: a guide to learn OpenCV. PyImageSearch. Disponível em:
https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/. Acesso em: 12 set. 2020.

Ana Huamán. Basic Drawing. OpenCV Docs. Disponível em:
https://docs.opencv.org/4.0.0/d3/d96/tutorial_basic_geometric_drawing.html. Acesso em: 12 set. 2020.

Ana Huamán. Random Generator and Text with OpenCV. OpenCV Docs. Disponível em:
https://docs.opencv.org/4.0.0/df/d61/tutorial_random_generator_and_text.html. Acesso em: 12 set. 2020.

Hmrishav Bandyopadhyay. Drawing in OpenCV. Medium. Disponível em:
https://medium.com/@hmrishavbandyopadhyay/drawing-in-opencv-4c688af5d642. Acesso em: 12 set. 2020.

"""

__author__ = "Eloi Giacobbo"
__copyright__ = 'Copyright 2020, OpenCV Python Tutorial'
__credits__ = ["Emili Bohrer"]
__license__ = "GPL-3.0"
__version__ = "0.1.2"
__maintainer__ = "Eloi Giacobbo"
__status__ = "Development"

# Em main, definimos a função principal do arquivo, onde as operações com imagens são executadas
def main():
    """ Desenhando sobre Imagens
    """

    # Primeiro, devemos incluir as bibliotecas necessárias.
    import numpy as np
    import cv2

    # Começaremos esta função criando uma imagem base, onde as funções de desenho serão utilizadas. Esta imagem nada
    # mais é que um ndarray de zeros com dimensões 300x300x3, para formar um fundo preto para as nossas operações. Não
    # esqueça que precisamos definir o tipo de variável como uint8, uma vez que este é o formato de dados padrão para
    # imagens do OpenCV.
    image = np.zeros((300, 300, 3), dtype="uint8")
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Agora, desenharemos manualmente uma borda sobre esta imagem, utilizando linhas. A função cv2.line recebe como
    # parâmetros principais a imagem onde a linha será desenhada, as coordenadas cartesianas (x, y) para o início e fim
    # desta linha, sua cor e espessura.
    cv2.line(image, (0, 0), (0, 300), (0, 0, 255), 10)
    cv2.line(image, (0, 300), (300, 300), (0, 0, 255), 10)
    cv2.line(image, (300, 300), (300, 0), (0, 0, 255), 10)
    cv2.line(image, (300, 0), (0, 0), (0, 0, 255), 10)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Como resultado um retângulo vermelho foi desenhado sobre a borda desta imagem. Logicamente, este efeito é mais
    # facilmente alcançado utilizando a função cv2.rectangle. Podemos então, por exemplo, sobrescrever a borda desenhada
    # anteriormente utilizando esta nova função. Novamente, inserimos como parâmetro de entrada uma imagem, as
    # coordenadas cartesianas (x, y) dos cantos superior esquerdo e inferior direito que formam o retângulo, sua cor e
    # espessura.
    cv2.rectangle(image, (0, 0), (300, 300), (255, 0, 0), 10)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Nossa próxima ação será desenhar círculos na nossa imagem, operação realizada pela função cv2.circle. Esta função
    # recebe como parâmetro de entrada uma imagem, as coordenadas cartesianas (x, y) do centro deste círculo, a
    # dimensão de seu raio, cor e espessura. Note que na operação a seguir estamos definindo a espessura deste círculo
    # como '-1'. Esta configuração nos garante que o objeto a ser desenhado será preenchido completamente pela cor
    # selecionada.
    cv2.circle(image, (150, 150), 20, (0, 0, 255), -1)
    cv2.circle(image, (172, 50), 10, (0, 255, 0), -1)
    cv2.circle(image, (257, 200), 10, (0, 255, 0), -1)
    cv2.circle(image, (45, 180), 10, (0, 255, 0), -1)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Outra função disponível neste pacote nos permite desenhar elipses em figuras. Para desenhar uma elipse, além de
    # inserir os parâmetros usuais, precisamos definir as coordenadas do seu centro, o comprimento de seus eixos
    # principal e secundário, seu ângulo de impressão e os ângulos de início e fim de seu arco elíptico. Através do
    # ângulo de impressão podemos rotacionar a elipse em seu centro, entre -360 à 360 graus do eixo horizontal. Já os
    # ângulos do arco elíptico definem se a elipse será desenhada por completo ou se apenas um arco será desenhado. Os
    # ângulos do arco podem variar entre 0 e 360 graus.
    cv2.ellipse(image, (150, 150), (120, 40), 90, 0, 360, (255, 0, 0), 2)
    cv2.ellipse(image, (150, 150), (120, 40), 25, 0, 360, (255, 0, 0), 2)
    cv2.ellipse(image, (150, 150), (120, 40), -25, 0, 360, (255, 0, 0), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Como a última operação, vamos escrever um texto sobre nossa imagem. A função cv2.putText recebe como parâmetros o
    # texto a ser escrito, sua posição de origem, definido como o ponto inferior esquerdo do texto, inserimos o tipo de
    # fonte para a escrita e o tamanho da fonte, além dos parâmetros usuais. Note que o OpenCV possui um padrão próprio
    # de fontes que pode ser consultado na documentação da biblioteca.
    cv2.putText(image, "OpenCV", (190, 285), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


# Para finalizar, realizamos a chamada da função main
if __name__ == '__main__':
    main()
