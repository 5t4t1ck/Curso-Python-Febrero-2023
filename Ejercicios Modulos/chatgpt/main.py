import openai
from decouple import config

openai.api_key = config("api_key")

while True:
    
    prompt = input("Introduce una pregunta: ")

    if prompt == "salir":
        break

    completion = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024
    )

    print(completion.choices[0].text)
