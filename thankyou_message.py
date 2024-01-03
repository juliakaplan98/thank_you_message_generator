import openai
import key
# prompt to generate thank you message to guest
thank_you_message_prompt = [
    {"role": "system", "content": "write a short thank you note"},
    {"role": "system", "content": "make the note 200 words or less"},
]
# import openai api_key
openai.api_key = key.x

# use gpt-3.5-turbo model to generate a thank you message
thank_you_message = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=thank_you_message_prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.7)

message = thank_you_message.choices[0].message.content
print(message)