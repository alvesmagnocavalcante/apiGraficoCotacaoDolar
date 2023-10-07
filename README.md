# apiGraficoCotacaoDolar
# API de Cotação do Dólar - Aplicativo de Visualização

Este é um aplicativo Python que utiliza a biblioteca Tkinter para a interface gráfica e a biblioteca Matplotlib para exibir gráficos de cotações do dólar em relação ao real.
## Como usar o aplicativo

1. **Requisitos**:
   - Python 3.x
   - Bibliotecas `tkinter`, `matplotlib`, `requests` e `datetime`.

2. **Instalação**:
   - Instale as bibliotecas necessárias executando o comando:
     ```
     pip install tkinter matplotlib requests
     ```

3. **Executando o aplicativo**:
   - Execute o script `app.py` usando o Python:
     ```
     python app.py
     ```

4. **Interface**:
   - A interface contém:
     - Um campo de entrada para o número de dias de dados a serem exibidos.
     - Um botão "Mostrar" para atualizar o gráfico com o novo número de dias.
     - Um gráfico que mostra as cotações de compra, venda, mínimo e máximo do dólar em relação ao real.

## Funcionalidades

- O aplicativo permite ao usuário escolher quantos dias de dados deseja visualizar. Basta inserir o número desejado e clicar em "Mostrar".
- Os dados são obtidos de uma API pública que fornece informações de cotações do dólar em relação ao real.

## Sobre o Código

- O código está organizado em uma classe `App` que herda de `tk.Tk`. A interface gráfica é configurada dentro desta classe.
- A função `cmd_executar` é responsável por fazer a requisição à API, processar os dados e atualizar o gráfico.

