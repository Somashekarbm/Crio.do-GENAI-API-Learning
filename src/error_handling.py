import time
from openai import OpenAI

# Configure client
client = OpenAI(api_key="your_api_key")

def call_openai_safely(prompt, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            # Attempt API call
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except client.RateLimitError:
            # Handle rate limits with exponential backoff
            wait_time = (2 ** retries) * 1
            print(f"Rate limit hit. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
            retries += 1
        except client.APIError as e:
            # Handle API errors
            print(f"API error: {e}")
            retries += 1
        except Exception as e:
            # Catch other unexpected errors
            print(f"Unexpected error: {e}")
            return f"Error occurred: {str(e)}"
            
    return "Failed after multiple retries"
