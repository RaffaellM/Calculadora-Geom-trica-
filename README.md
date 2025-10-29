# 📐 Calculadora Geométrica em Python

Um script de console (CLI) simples, desenvolvido em Python, para calcular propriedades de diferentes formas geométricas. O programa guia o usuário através de um menu interativo e inclui validação de dados para garantir que apenas valores válidos sejam processados.

## ✨ Funcionalidades

O script atualmente suporta os seguintes cálculos:

* **Área do Retângulo (2D):**
    * Solicita ao usuário o **comprimento** e a **largura**.
    * Calcula a área: $A = comprimento \cdot largura$.
    * **Recurso Bônus:** O programa identifica e informa ao usuário se as dimensões inseridas formam um quadrado (comprimento == largura).

* **Área do Círculo (2D):**
    * Solicita ao usuário o **raio**.
    * Calcula a área usando a biblioteca `math` para precisão: $A = \pi \cdot r^2$.

* **Volume do Tetraedro Regular (3D):**
    * Solicita ao usuário o comprimento da **aresta**.
    * Calcula o volume usando a fórmula: $V = \frac{aresta^3}{6 \cdot \sqrt{2}}$.

### Principais Recursos do Código

* **Menu Interativo:** Um loop principal (`while`) que permite ao usuário realizar múltiplos cálculos sem reiniciar o script.
* **Validação de Entrada:** Cada função possui um loop `while True` com blocos `try-except ValueError` para garantir que a entrada seja um número.
* **Verificação de Números Positivos:** O código também verifica se os números inseridos (comprimento, largura, raio, aresta) são maiores que zero, solicitando uma nova entrada caso não sejam.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Módulo `math`**: (Nenhuma biblioteca externa é necessária).

Deseja fazer outro cálculo? (s/n): n

Obrigado por usar a calculadora!
