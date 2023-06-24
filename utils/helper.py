import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import openai
from langchain import PromptTemplate, OpenAI, LLMChain, LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

import chainlit as cl

from dotenv import load_dotenv
load_dotenv()

# print(os.getenv("SERP_API_KEY"))