import json
from openai import OpenAI

client = OpenAI(api_key="your_api_key")

def extract_article_data(article_text):
# Define the structure we want to extract
          tools = [
                  {
                  "type": "function",
                  "function": {
                  "name": "extract_article_info",
                  "description": "Extract key information from article",
                  "parameters": {
                  "type": "object",
                  "properties": {
                          "title": {"type": "string"},
                          "summary": {"type": "string"},
                          "key_points": {"type": "array", "items": {"type": "string"}},
                          "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]}
                          },
                  "required": ["title", "summary", "key_points", "sentiment"]
                  }
                  }
                  }
          ]
          response = client.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": f"Extract information: {article_text}"}],
              tools=tools,
              tool_choice={"type": "function", "function": {"name": "extract_article_info"}}
          )

          # Parse the structured JSON response
          function_call = response.choices[0].message.tool_calls[0]
          return json.loads(function_call.function.arguments)
