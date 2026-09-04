from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=""
)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a lindken post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'lindken': prompt2 | model | parser
})

result = parallel_chain.invoke({'topic': 'AI'})

print(result)