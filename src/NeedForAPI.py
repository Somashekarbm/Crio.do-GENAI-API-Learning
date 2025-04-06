# Simple static system approach-

responses = {
"hello": "Hi there!",
"how are you": "I'm good, thanks for asking!",
# Limited predefined responses
}

def get_response(question):
    return responses.get(question.lower(), "I don't know.")


# v/s OpenAI API approach

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(question):
    # Access powerful pre-trained models through API
    response = client.chat.completions.create( model="gpt-3.5-turbo",  #model to use for inference
                                               messages=[{"role": "user", "content": question}]
                                             )
    # Extract the generated text response
    return response.choices[0].message.content
