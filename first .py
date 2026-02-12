#first file

from langchain.tools import tool
@tool
def search_database(query: str,limit: int =10)->str:
    """Search the database for relevant information."""
    # Simulate a database search
    results = f"Results for '{query}' with limit {limit}"
    return results


#for custom function name we need to do this


@tool("web_search")
def search_web(query:str)->str:
    """ Search the web for information"""
    return f"Results for web search of :{query}"

print(search_web.name)