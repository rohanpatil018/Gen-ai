from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=""
)

# Step 1: Prompt to generate the joke
prompt1 = PromptTemplate(
    template='Generate a joke on {topic}',
    input_variables=['topic']
)

# Step 2: Prompt to explain the joke (matches the variable name passed from the dictionary)
prompt2 = PromptTemplate(
    template='Explain the joke: {text}',
    input_variables=['text']
)

parser = StrOutputParser()

# 1. Create a chain that generates the initial joke string
joke_gen_chain = prompt1 | model | parser

# 2. Create a parallel block that passes the joke forward and generates an explanation
explanation_chain = prompt2 | model | parser

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': explanation_chain
})

# 3. Combine them sequentially: First get the joke, then feed it into the parallel/explanation block
final_chain = joke_gen_chain | parallel_chain

# Invoke the chain
result = final_chain.invoke({'topic': 'Movies'})

print("--- Joke ---")
print(result['joke'])

print("\n--- Explanation ---")
print(result['explanation'])