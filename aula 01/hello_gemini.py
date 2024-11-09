import google.generativeai as genai
import os

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Comecei a estudar sobre Inteligência Artificial, me fale sobre Geminai e como posso utilizar gratuitamente.")
print (response.text)