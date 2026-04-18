#first file

from langchain.tools import tool
@tool
def search_database(query: str,limit: int =10)->str:
    """Search the database for relevant information."""
    # Simulate a database search
    results = f"Results for '{query}' with limit {limit}"
    return results


#for custom function name we need to do this
"""
langchain takes help of this tool to access databases ,searcher web,
connects apis etc so LLM s are like brain and tools are like hands 
langchaib reads the function name ,reads type hints query:str,limit:int 
and docstring and then it can call the function with the right parameters
Tool(
    name="search_database",
    description="Search the database for relevant information.",
    args_schema=...
)


int this web_search the name of the tool becomes web_Search custom name,
"""
@tool("web_search")
def search_web(query:str)->str:
    """ Search the web for information"""
    return f"Results for web search of :{query}"

print(search_web.name)





import pydantic import BaseModel,Field
from typing import Literal
#pydanti is used to define structures data with validation ,basemodel is a data scheme
# base model generates data schema generaates JSON schema
class WeatherInput(BaseModel):
    """
    input for weather queries
    """
    location:str=Field(description="City name or coordinates")
    units:Literal["celsius","fahrenheit"]=Field(
        default="celsius",
        description="Units for temperature")



@tool(args_schema=WeatherInput)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Get current weather and optional forecast."""
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result




# Langchain+langgraph