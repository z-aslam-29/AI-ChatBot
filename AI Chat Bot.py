import openai

openai.api_key = "Your API key"

model_engine = "text-davinci-002"

while True:
    prompt = input("You : ")


    response = openai.Completion.create(


        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )


    message = response["choices"][0]["text"]
    message = message[message.index("\n") + 1:]

    print("Bot: " + message)