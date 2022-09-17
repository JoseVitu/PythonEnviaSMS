import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5adbb4fa0f1ed6448c52e23d234367a4"
# Your Auth Token from twilio.com/console
auth_token  = "b9d2952638b1019d80dd3081c63ce216"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas["Vendas"] > 55000,"Vendas"].values[0]
        print(f"No mes {mes} o vendedor {vendedor} vendeu mais de 55000 ele vendeu no total {vendas}")
        message = client.messages.create(
            to="+5544998087606",
            from_="+13393297356",
            body=f"No mes {mes} o vendedor {vendedor} vendeu mais de 55000 ele vendeu no total {vendas}")

        print(message.sid)

