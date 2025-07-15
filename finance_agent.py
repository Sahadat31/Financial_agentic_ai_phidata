import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

web_agent = Agent(
    name="Web Agent",
    role="A web search agent that can answer questions using the DuckDuckGo search engine.",
    description="This agent can search the web for information and provide answers based on the latest data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        DuckDuckGo()
    ],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="A finance agent that can answer questions regarding financial data using the YFinance API.",
    description="This agent can provide financial data and insights using the YFinance API",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(stock_price=True, company_info=True, analyst_recommendations=True, company_news=True)
    ],
    instructions=["Use Tables to diplay data"],
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use Tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("Summarize analyst recommendation and latest news for HDFC banks.",stream=True)