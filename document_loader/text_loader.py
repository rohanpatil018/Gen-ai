from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt=PromptTemplate(
    template='Write a Summary of the following poem- \n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

chain=prompt|model|parser

loader = TextLoader("cricket.txt", encoding="utf-8")


docs = loader.load()

print(chain.invoke({'poem':docs[0].page_content}))