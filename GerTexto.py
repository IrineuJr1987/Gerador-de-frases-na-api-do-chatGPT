import os
import openai
import datetime
import time

openai.api_key = ""

# O assunto que você deseja gerar texto
assunto = "frase motivacional"


def gerar_texto():
    # Gere o texto usando a API do ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        #prompt=f"Me forneça 5 curiosidades aleatorias sobre {assunto} em formato de roteiro para fazer um video pro tiktok com titulo pro video e antes de cada curiosidade dizer a ordem: ",
        prompt=f"Me forneça uma {assunto} de autor conhecido: ",
        max_tokens=1024,
        temperature=0.9,
    )

    # Armazene o texto gerado em uma variável
    texto_gerado = response["choices"][0]["text"]

    # Caminho para a pasta "videos" na unidade D
    caminho_pasta = r"E:\Conteudo\videos\Motivacional\Frases"

    # Nome do arquivo
    nome_arquivo = "texto_gerado"

    # Obtenha a data e hora atuais
    agora = datetime.datetime.now()

    # Formate a data e hora como uma string no formato "ano-mês-dia_hora-minuto-segundo"
    data_hora_formatada = agora.strftime("%Y-%m-%d_%H-%M-%S")

    # Adicione a data e hora ao nome do arquivo
    nome_arquivo_completo = f"{nome_arquivo}_{data_hora_formatada}.txt"

    # Junte o caminho da pasta e o nome do arquivo usando os.path.join
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo_completo)


    # Abra o arquivo usando o caminho completo
    with open(caminho_completo, "w") as f:
        f.write(texto_gerado)

    print(f"Texto gerado sobre o assunto {assunto}:")
    print(texto_gerado)
    time.sleep(3)

for i in range(5):
    gerar_texto()