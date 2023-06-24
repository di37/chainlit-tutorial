from utils import *

# Example 1 
# @cl.langchain_factory(use_async=True)
# def factory():
#     prompt = PromptTemplate(template=THINK_TEMPLATE, input_variables=["question"])
#     llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

#     return llm_chain

# Example 2
@cl.langchain_factory(use_async=False)
def load():
    llm = ChatOpenAI(temperature=0, streaming=True)
    llm1 = OpenAI(temperature=0, streaming=True)
    search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
    llm_math_chain = LLMMathChain(llm=llm, verbose=True)

    tools = [
        Tool(
            name="Search",
            func = search.run,
            description="useful for when you need to answer questions about current events."
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer question about math."
        )
    ]
    return initialize_agent(
        tools, llm1, agent="chat-zero-shot-react-description", verbose=True
    )