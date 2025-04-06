import json  # Import the JSON module for parsing structured data
from openai import OpenAI  # Import the OpenAI class to interact with the API

client = OpenAI(api_key="your_api_key")  # Initialize the OpenAI client with your API key

def extract_article_data(article_text):  # Define a function to extract structured info from article text

    # Define the expected structure of the response using a tool/function schema
    tools = [
        {
            "type": "function",
            "function": {
                "name": "extract_article_info",  # Name of the function tool
                "description": "Extract key information from article",  # Description of what it does
                "parameters": {
                    "type": "object",  # Expect an object/dictionary as a result
                    "properties": {
                        "title": {"type": "string"},  # Article title
                        "summary": {"type": "string"},  # Short summary of the article
                        "key_points": {"type": "array", "items": {"type": "string"}},  # List of key points
                        "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]}  # Sentiment value
                    },
                    "required": ["title", "summary", "key_points", "sentiment"]  # These fields are mandatory
                }
            }
        }
    ]

    # Send the article text to the API, requesting structured extraction using the defined tool
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[{"role": "user", "content": f"Extract information: {article_text}"}],  # User prompt
        tools=tools,  # Include the tool definition
        tool_choice={"type": "function", "function": {"name": "extract_article_info"}}  # Select the function to run
    )

    # Extract the tool call result and parse it as JSON
    function_call = response.choices[0].message.tool_calls[0]  # Get the tool call result
    return json.loads(function_call.function.arguments)  # Convert the argument string to a Python dictionary
