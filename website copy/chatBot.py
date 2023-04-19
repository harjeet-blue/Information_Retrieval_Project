import openai

openai.api_key = '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'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

def generate_ans_chatbot(user_input):
    message=user_input
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    return reply

