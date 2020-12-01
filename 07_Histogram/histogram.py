#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Histogramas

Um histograma de imagem é um tipo de histograma que atua como uma representação gráfica da distribuição de cores em uma
imagem digital. Observando o histograma de uma imagem específica, é possível avaliar sua distribuição de cores de uma
maneira ainda mais simples de como realizamos no módulo 4 deste repositório.

O eixo horizontal do histograma representa as variações de tom de uma cor, enquanto o eixo vertical representa o número
total de pixels naquele tom específico.

O lado esquerdo do eixo horizontal representa as áreas escuras, o meio representa os valores de tons médios e o lado
direito representa as áreas claras. O eixo vertical representa o tamanho da área (número total de pixels) que é
capturado em cada uma dessas zonas.

Simplesmente examinando o histograma de uma imagem, você obtém uma compreensão geral sobre o contraste, brilho e
distribuição de intensidade. Assim, o histograma para uma imagem muito escura terá a maioria de seus pontos de dados no
lado esquerdo e no centro do gráfico. Por outro lado, o histograma para uma imagem muito clara com poucas áreas escuras
e/ou sombras terá a maioria de seus pontos de dados no lado direito e no centro do gráfico.

No campo da visão computacional, os histogramas de imagem podem ser ferramentas úteis para operações de thresholding.
Como as informações contidas no gráfico são uma representação da distribuição de pixels em função de sua variação de
cores, os histogramas da imagem podem ser analisados quanto a picos e/ou vales. Este valor limite pode então ser usado
para detecção de contornos, segmentação de imagens e matrizes de co-ocorrência.

Neste tutorial veremos mais detalhes sobre a criação de histogramas e algumas aplicações simples desta ferramenta.

Para executar este código, utilize o seguinte comando em seu terminal:
$ python histogram.py

Referências:

Adrian Rosebrook. Practical Python and OpenCV: an introductory, example driven guide to image processing and computer
vision. PyImageSearch, 2016.

Ana Huamán. Histogram Calculation. OpenCV Docs. Disponível em:
https://docs.opencv.org/4.0.0/d8/dbc/tutorial_histogram_calculation.html. Acesso em: 20 set. 2020.

Image histogram. Wikipedia. Disponível em: https://en.wikipedia.org/wiki/Image_histogram. Acesso em: 20 set. 2020.

Sean Mchugh. Camera Histograms: tones & contrast. Cambridge in Colour. Disponível em:
https://www.cambridgeincolour.com/tutorials/histograms1.htm. Acesso em: 20 set. 2020.

"""

__author__ = "Eloi Giacobbo"
__copyright__ = 'Copyright 2020, OpenCV Python Tutorial'
__credits__ = ["Emili Bohrer"]
__license__ = "GPL-3.0"
__version__ = "0.1.0"
__maintainer__ = "Eloi Giacobbo"
__status__ = "Development"

# Em main, definimos a função principal do arquivo, onde as operações com imagens são executadas
def main():
    """ Histogramas
    """

    # Primeiro, devemos incluir as bibliotecas necessárias.
    import cv2
    import errno
    import numpy as np
    import os
    from matplotlib import pyplot as plt

    # Utilizando o parâmetro caminho relativo para as imagens "contrast1.jpg" e "contrast2.jpg", presente na pasta
    # 99_Images deste repositório, a imagem selecionada é carregada através do comando imread do módulo cv2.
    image1_path = "../99_Images/contrast1.jpg"
    low_contrast = cv2.imread(image1_path)
    image2_path = "../99_Images/contrast2.jpg"
    high_contrast = cv2.imread(image2_path)

    # Para garantir a correta execução deste código, verificamos se as imagens anteriores foram carregadas corretamente
    if (low_contrast is None):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image1_path)
    if (high_contrast is None):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image2_path)

    # Para fins simples, o OpenCV implementa a função cv.calcHist que calcula o histograma de um conjunto de matrizes
    # (geralmente imagens ou planos de imagens). Como parâmetros de entrada, esta função recebe uma lista de imagens,
    # uma lista com índices dos canais de cores que compõem as imagens de entrada, uma máscara para delimitar a região
    # da imagem a partir de onde o histograma será calculado, uma lista com o número de intervalos/barras para a
    # montagem do histograma e o intervalo de valores possíveis para os pixels da imagem.

    # Dito isto, começaremos elaborando um histograma para a imagem "contrast1.jpg" em escala de cinza. Primeiro,
    # convertemos a imagem original para escala de cinza e a imprimimos em tela.
    cv2.imshow("Low Contrast", low_contrast)
    low_contrast_gray = cv2.cvtColor(low_contrast, cv2.COLOR_BGR2GRAY)

    # Em seguida, calculamos seu histograma. Por se tratar de uma imagem em escala de cinza, o índice de seu canal é 0.
    # Não aplicaremos nenhuma máscara, então este parâmetro recebe o valor None. O número de intervalos será 256, um
    # para cada valor de intensidade dos pixels e seu intervalo de intensidades está entre 0 e 256.
    low_contrast_hist = cv2.calcHist([low_contrast_gray], [0], None, [256], [0, 256])

    # Realizado o cálculo do histograma, apresentamos o gráfico em tela.
    plt.figure()
    plt.title("Histograma de uma Imagem Escala de Cinza de Baixo Contraste")
    plt.xlabel("Intervalos")
    plt.ylabel("Número de Pixels")
    plt.plot(low_contrast_hist)
    plt.xlim([0, 256])

    # Através do histograma podemos observar que esta imagem possui, principalmente, tons de cores intermediários, pois
    # a grande maioria dos pixels desta imagem estão entre os intervalos de intensidade 100 e 150. Em outras palavras,
    # temos poucas sombras (pixels pretos) e poucas fontes de brilho (pixels com intensidade máxima de cor). Neste
    # histograma temos, basicamente, um pico estreito, indicando que temos uma imagem de baixo contraste. O contraste
    # pode ter um impacto visual significativo em uma imagem, enfatizando sua textura. Nota-se facilmente como há poucos
    # detalhes nesta imagem, onde observamos uma faixa de água com poucas oscilações.

    # Em comparação, observaremos agora o histograma da imagem "contrast2.jpg". Para isto, a mesma sequência de comandos
    # é realizada para calcular o histograma desta imagem e apresentá-lo em tela.
    cv2.imshow("High Contrast", high_contrast)
    cv2.waitKey(0)
    high_contrast_gray = cv2.cvtColor(high_contrast, cv2.COLOR_BGR2GRAY)
    high_contrast_hist = cv2.calcHist([high_contrast_gray], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Histograma de uma Imagem Escala de Cinza de Alto Contraste")
    plt.xlabel("Intervalos")
    plt.ylabel("Número de Pixels")
    plt.plot(high_contrast_hist)
    plt.xlim([0, 256])
    plt.show()
    cv2.destroyAllWindows()

    # Nesta segunda imagem temos uma segunda representação da mesma faixa de água apresentada anteriormente. Porém,
    # nesta imagem conseguimos perceber ondulações na superfície da água com facilidade. Este efeito se reflete em seu
    # histograma como uma maior distribuição dos pixels que compõem a imagem. Ainda temos uma imagem composta
    # principalmente por tons de cores intermediários e um único pico em sua forma de onda. Porém, este pico de
    # concentração de pixels está mais distribuído, indicando o maior nível de contraste que esta imagem possui. Em
    # resumo, contraste é medido através da diferença de brilho entre as áreas claras e escuras de uma imagem.
    # Histogramas com maior distribuição de pixels ao longo dos intervalos de intensidade refletem uma imagem com
    # contraste significativo, enquanto os histogramas com maiores concentrações de pixels refletem menos contraste e
    # podem representar imagens planas ou opacas.

    # O contraste também pode variar para diferentes regiões de uma mesma imagem. Para observar este efeito, iremos
    # analisar a imagem "contrast3.jpg". Esta imagem foi dividida em três regiões de contraste distintas. Através do uso
    # de máscaras, iremos avaliar cada uma destas regiões separadamente.
    image3_path = "../99_Images/contrast3.jpg"
    variable_contrast = cv2.imread(image3_path)
    if (variable_contrast is None):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image3_path)

    # Apresentamos a imagem em tela
    cv2.imshow("Variable Contrast", variable_contrast)
    cv2.waitKey(0)

    # Começamos pela definição das três mascaras necessárias. A máscara deve possuir apenas um canal e tipo de dados
    # uint8. A região avaliada em cada histograma é definida pela atribuição das regiões com valor 255.
    (heigh, width) = variable_contrast.shape[:2]
    mask1 = np.zeros((heigh, width), dtype = "uint8")
    mask2 = np.zeros((heigh, width), dtype = "uint8")
    mask3 = np.zeros((heigh, width), dtype = "uint8")
    mask1[:99, :] = 255
    mask2[102:288, :] = 255
    mask3[291:, :] = 255

    # Em seguida, calculamos cada um dos histogramas em escala de cinza
    variable_contrast_gray = cv2.cvtColor(variable_contrast, cv2.COLOR_BGR2GRAY)
    variable_contrast_hist1 = cv2.calcHist([variable_contrast_gray], [0], mask1, [256], [0, 256])
    variable_contrast_hist2 = cv2.calcHist([variable_contrast_gray], [0], mask2, [256], [0, 256])
    variable_contrast_hist3 = cv2.calcHist([variable_contrast_gray], [0], mask3, [256], [0, 256])

    # Para finalizar esta operação, criamos um subplot para apresentar os três histogramas em tela
    fig, axis = plt.subplots(3)
    fig.suptitle("Histograma de uma Imagem Escala de Cinza de Contraste Variável")
    axis[0].plot(variable_contrast_hist1)
    axis[1].plot(variable_contrast_hist2)
    axis[2].plot(variable_contrast_hist3)
    axis[1].set(ylabel='Número de Pixels')
    axis[2].set(xlabel='Intervalos')
    plt.show()
    cv2.destroyAllWindows()

    # A região superior contém o maior contraste de todas as três imagens por ser criada diretamente a partir de uma
    # fonte de luz que não foi refletida pela superfície de água. Isso produz sombras mais profundas sob o barco e suas
    # saliências, além de realces mais fortes nas áreas voltadas para cima e diretamente expostas. As regiões central e
    # inferior são produzidas inteiramente a partir de uma luz refletida e, portanto, têm contraste inferior. As
    # condições na região inferior criam realces mais pronunciados, mas ainda carecem das sombras profundas da região
    # superior. Da mesma forma, estas características de contraste variável entre as regiões da imagem estão
    # representadas nas formas de onda de cada um dos histogramas apresentados.

    # Os histogramas que elaboramos até o momento são comumente chamados de histogramas de luminosidade. Além de
    # fornecer informações referentes ao contraste de uma imagem, também podemos avaliar seu nível de brilho, ou,
    # luminosidade. Isto se deve pela forma com que o OpenCV realiza a conversão de uma imagem para escala de cinza.
    # Esta conversão executa uma média ponderada entre os canais de cores de uma imagem, atribuindo diferentes pesos
    # para cada canal. Esta ponderação assume que o canal de cor verde representa 59% da luminosidade percebida,
    # enquanto os canais vermelho e azul representam apenas 30% e 11%, respetivamente. O cálculo de luminosidade leva em
    # consideração o fato de que o olho humano é mais sensível à luz verde do que à luz vermelha ou azul. Sendo assim,
    # quanto maior a predominância de pixels em intervalos de intensidade maiores, maior será o nível de brilho de uma
    # imagem. Assim como, quanto maior a predominância de pixels em intervalos de intensidade menores, menor será o
    # nível de brilho de uma imagem.

    # Seguindo em frente, avaliaremos agora o histograma de imagens coloridas. Para avaliar imagens coloridas na forma
    # de histogramas, primeiro precisamos elaborar o histograma de cada um dos canais de cores separadamente. Este
    # resultado pode ser somado para formar um histograma RGB ou avaliados individualmente.

    # Para esta etapa vamos carregar a apresentar em tela a imagem "bgr-led.jpg".
    image4_path = "../99_Images/bgr-led.jpg"
    image = cv2.imread(image4_path)
    if (variable_contrast is None):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), image4_path)
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    # Executamos a separação desta imagem em seus canais de cores e elaboramos três histogramas, um para cada canal de
    # cor. Em seguida, somamos o resultado destes três histogramas para formar um histograma RGB.
    channels = cv2.split(image)
    blue_hist = cv2.calcHist([channels[0]], [0], None, [256], [0, 256])
    green_hist = cv2.calcHist([channels[1]], [0], None, [256], [0, 256])
    red_hist = cv2.calcHist([channels[2]], [0], None, [256], [0, 256])
    rgb_hist = blue_hist + green_hist + red_hist

    # Em comparação, elaboramos e imprimimos em tela um histograma de luminosidade desta mesma imagem
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    fig, axis = plt.subplots(1, 3)
    axis[0].set_title("Histograma de Luminosidade")
    axis[0].plot(image_hist)
    axis[0].set(ylabel="Número de Pixels", xlim=[0, 256], ylim =[0, 5000])

    # Imprimimos também o histograma RGB da imagem
    axis[1].set_title("Histograma RGB")
    axis[1].plot(rgb_hist)
    axis[1].set(xlabel="Intervalos", xlim=[0, 256], ylim =[0, 5000])

    # Imprimimos em tela os histogramas de cada um dos canais de cores
    axis[2].set_title("Histograma de Canais")
    axis[2].plot(blue_hist, color = "b")
    axis[2].plot(green_hist, color = "g")
    axis[2].plot(red_hist, color = "r")
    axis[2].set(xlim=[0, 256], ylim =[0, 5000])
    plt.show()
    cv2.destroyAllWindows()

    # Uma diferença importante para tirar do cálculo acima é que, enquanto os histogramas de luminosidade rastreiam a
    # localização de cada pixel de cor, os histogramas RGB descartam essas informações. Um histograma RGB produz três
    # histogramas independentes e os soma, independentemente de cada cor vir ou não do mesmo pixel.

    # A partir do histograma de luminosidade temos que a imagem "bgr-led" possui bom contraste e, de uma forma geral,
    # pouco brilho. Também é possível observar grande predominância dos pixels pretos que compõem o fundo da imagem. Ao
    # observarmos o histograma RGB é possível notar estas mesmas características sobre a imagem dos LEDs. Adicionalmente,
    # o histograma RGB nos mostra que há uma concentração considerável de pixels com maior intensidade de cor. Estes 
    # pixels podem ser encontrados principalmente no centro dos LEDs azul e vermelho, onde é possível perceber que temos
    # duas manchas com tonalidades próximas ao branco. Por fim, ao plotarmos o histograma de cada um dos canais de cores
    # individuais, podemos observar que são exatamente as cores azul e vermelha que apresentam maior quantidade de
    # pixels com elevadas intensidades nesta imagem.

    # Note que diferentes características de uma imagem são apresentadas em cada um destes histogramas. Enquanto o
    # histograma de luminosidade nos apresenta um diagrama mais voltado à nossa percepção das cores, os demais gráficos
    # representam a distribuição de cores de uma forma mais direta. Dependendo dos objetivos de sua análise, a escolha
    # do tipo de histograma trás diferentes informações sobre as características de uma imagem.


# Para finalizar, realizamos a chamada da função main
if __name__ == '__main__':
    main()
