from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)


prompt2=PromptTemplate(
    template='Explain the joke {text}',
    input_variables=['text']
)

model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=""
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2, model,parser)

print(chain.invoke({'topic':'AI'}))

