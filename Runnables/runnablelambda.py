from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=""
)
def word_count(text):
    return len(text.split())
prompt=PromptTemplate(
     template='generate a joke on {topic}',
     input_variables=['topic']
)

parser=StrOutputParser()

joke_gen_chian=RunnableSequence(prompt,model,parser)

parallel_chian=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chian=RunnableSequence(joke_gen_chian,parallel_chian)

result=final_chian.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)