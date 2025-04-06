
def get_structured_chat_response(chat_history):
        try:
                #1. Make the API call to the LLM here-
                (Note: The code for setting up an API call is 
                already shown in activity #2.)
        
                #2. Responses fetched from the LLM request 
                     are parsed below as such
                structured_turns = []
                for choice in response.choices:
                    role = choice.message.role
                    content = choice.message.content.strip()
                    structured_turns.append(
                    {"role": role, "message": content})
                return structured_turns
        
        #3. if an error occurs
         except Exception as e: 
                return [{"role": "system",
                "message": f"Error occurred: {str(e)}"}]

#4. Example usage of the same
chat_history = [
    {"role": "user", "content": "Hi!"},
    {"role": "assistant", "content": "Hello! How can I help you?"},
    {"role": "user", "content": "What's the weather in Paris today?"}
]

#5. Display the AI agent’s role and its message here
for turn in get_structured_chat_response(chat_history):
    print(f"{turn['role'].capitalize()}: {turn['message']}")
