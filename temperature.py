from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0)

result = model.invoke("write a 5 line poem on cricket")

print(result.content)
