# import openai
#
# openai.api_key = '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'
#
# response = openai.Completion.create(
#   model="gpt-3.5-turbo", # or another model like gpt-3.5-turbo
#   prompt="Paraphrase the following text: 'This is an example sentence that needs to be rephrased.'",
#   temperature=0.7,
#   max_tokens=60
# )
#
# print(response.choices[0].text.strip())

import  os
from openai import OpenAI

def paraphrase(text):
  os.environ["OPENAI_API_KEY"] = "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"
  # api_key = os.environ.get("OPENAI_API_KEY")
  # print(api_key)
  client = OpenAI()
  completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "You are a helpful assistant to do the elabrate into 100 words of the given text. Avtive voice"},
      {"role": "user", "content": text }
    ]
  )

  return completion.choices[0].message.content