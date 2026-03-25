from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from agent.tools import tools
from agent.prompts import SYSTEM_PROMPT
import os

class AirportCRMAgent:
    def __init__(self, api_key: str, model: str = "gpt-4-turbo-preview", provider: str = "openai"):
        """
        Initialize the Airport CRM Agent
        
        Args:
            api_key: API key for the LLM provider
            model: Model name to use
            provider: Either 'openai' or 'anthropic'
        """
        
        # Initialize LLM based on provider
        if provider.lower() == "openai":
            os.environ["OPENAI_API_KEY"] = api_key
            self.llm = ChatOpenAI(model=model, temperature=0.3)
        elif provider.lower() == "anthropic":
            os.environ["ANTHROPIC_API_KEY"] = api_key
            self.llm = ChatAnthropic(model=model, temperature=0.3)
        else:
            raise ValueError("Provider must be either 'openai' or 'anthropic'")
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        # Initialize memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create agent
        self.agent = create_openai_functions_agent(
            llm=self.llm,
            tools=tools,
            prompt=self.prompt
        )
        
        # Create executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=tools,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )
    
    def chat(self, user_input: str) -> str:
        """
        Process user input and return agent response
        
        Args:
            user_input: The user's message
            
        Returns:
            The agent's response
        """
        try:
            response = self.agent_executor.invoke({"input": user_input})
            return response["output"]
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try rephrasing your question."
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.memory.clear()
