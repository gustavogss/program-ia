import google.generativeai as genai
import os

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Estou estudando para um concurso da Dataprev, me fale sobre Spring Cloud.")
print (response.text)