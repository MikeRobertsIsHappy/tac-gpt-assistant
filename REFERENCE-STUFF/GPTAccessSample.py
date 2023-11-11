#!pip install os
#!pip install openapi

#  get  ChatGPT Plus Subscription with GPT-4 Code Interpreter or above models.
#  learn to see whole response, get HTML response from API
# https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor



import os
import openai

os.environ['OPENAI_API_KEY'] = "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"

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-4",
  max_tokens = 150,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "[Overall Rules to follow:\n   1. Use emojis to make the content engaging\n    2. Use bolded text to emphasize important points\n    3. compress your responses.] \n Tell me a joke"},
    {"role": "assistant", "content": "you always speak in rhyme"}
  ]
)
response = completion.choices[0].message
print(response)
#print("===============================================")
#print(response['content'])
print("===============================================")
#print(completion.choices[0].message['content'].strip())
