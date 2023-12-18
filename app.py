import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



genai.configure(api_key="")
model = genai.GenerativeModel('gemini-pro')
inp = input("Your prompt!")
response = model.generate_content(inp, stream=True)
for chunk in response:
  strr = chunk.text
  print(strr.replace("**", ""))
  print("_"*80)
