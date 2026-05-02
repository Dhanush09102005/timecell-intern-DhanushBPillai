from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

portfolio = {
    "BTC": 30,
    "NIFTY50": 40,
    "GOLD": 20,
    "CASH": 10
}

portfolio_str = "\n".join([f"{k}: {v}%" for k, v in portfolio.items()])

prompt = PromptTemplate(
    input_variables=["portfolio"],
    template="""
You are a financial advisor.

Given this portfolio:
{portfolio}

Provide:
1. 3-4 sentence risk summary (simple English)
2. One good thing
3. One improvement with reason
4. Final verdict: Aggressive, Balanced, or Conservative

Keep it concise and clear. Write in the tone of a friendly but honest financial advisor talking to a non-expert client. Format it properly so each point's answer is numbered and separated.
"""
)

llm = ChatGroq(model="llama-3.3-70b-versatile")

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run(portfolio=portfolio_str)

print(response)