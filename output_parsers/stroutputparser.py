from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1st prompt -> detailed report (Note: parameter name is 'input_variables' plural)
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd prompt (Fixed newline escape sequence from '/n' to '\n')
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text.\n{text}",
    input_variables=["text"],
)

# Fixed dictionary syntax for .invoke() and passed 'input' properly
prompt1 = template1.invoke({"topic": "blackhole"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt2)

# Printing the final summary result
print(result1.content)