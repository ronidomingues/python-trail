import yfinance as yf
import matplotlib
import datetime
import pandas as pd
import pyautogui
import pyperclip
import webbrowser
from time import sleep

# Gerando o Relatório
ticker = input("Digite o código da ação: ") or "PETR4.SA"
start_date = input("Digite a data inicial (aaaa-mm-dd): ") or "2020-01-01"
end_date = input("Digite a data final (aaaa-mm-dd): ") or "2020-12-31"
data = yf.Ticker(ticker)
table = data.history(start=start_date, end=end_date)
print(table.head())

# Selecionando apenas a coluna de fechamento
closing = table.Close
print(closing)

# Gerando um gráfico de linha (usa a biblioteca matplotlib)
closing.plot(title=f"Fechamento da ação {ticker} de {start_date} a {end_date}")

# Gerando estatísticas descritivas
max_price = round(closing.max(), 2)
min_price = round(closing.min(), 2)
average_price = round(closing.mean(), 2)

# Exportando para um arquivo excel

# Se o índice for datetime com timezone
if hasattr(table.index, "tz") and table.index.tz is not None:
    table.index = table.index.tz_localize(None)

# Exportando ...
excel_file_name = "aula_02.xlsx"
table.to_excel(excel_file_name, index=True)
print(f"Arquivo {excel_file_name} salvo com sucesso!")

# Enviando o e-mail de forma automatizada

# Posicione o cursor do mouse sobre o botão "Escrever" deixe-o lá vá no terminal e rode o código:
# print(pyautogui.position()) e anote as coordenadas exibidas (x, y), em seguida,
# faça a mesma coisa sobre o botão "Enviar", você também precisará dessas coordenadas para
# ordenar que o pyautogui clique nesses botões.

recipient = "ronidomingues@poli.ufrj.br"
subject = "Análise de Projeto 2020"

message = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Análise de Ações</title>
</head>
<body>
    <h1>Relatório de Análise de Ações</h1>
    <p>Bom dia,</p>
    <p>Segue abaixo as análises da ação {ticker} do período solicitado: {start_date} a {end_date}</p>
    <ul>
        <li>Cotação máxima: {max_price}</li>
        <li>Cotação mínima: {min_price}</li>
        <li>Valor médio: {average_price}</li>
    </ul>
</body>
</html>
"""

# Configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 3

# Abrir o navegador e acessar o Gmail
webbrowser.open("https://mail.google.com/")
sleep(3)

# Clicar no botão "Escrever"
pyautogui.click(x=73, y=209)

# Preencher Para
pyperclip.copy(recipient)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Preencher Assunto
pyperclip.copy(subject)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Preencher Corpo do e-mail
pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão Enviar
pyautogui.click(x=1304, y=1013)

# Fechar a aba
pyautogui.hotkey("ctrl", "w")

print("E-mail enviado com sucesso!")