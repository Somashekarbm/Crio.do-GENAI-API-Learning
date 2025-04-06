import os
from openai import OpenAI

# Setup API key using environment variable (security best practice)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ContentGenerator:
    def generate_text(self, prompt):
        # Generate text content using chat completions API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def generate_image(self, prompt):
        # Generate image using DALL-E API
        response = client.images.generate(
            model="dall-e-2",  # Using DALL-E 3 model
            prompt=prompt,
            size="1024x1024",  # Setting image dimensions
            n=1  # Generate one image
        )
        # Return the URL of the generated image
        return response.data[0].url

    def generate_speech(self, text):
        # Convert text to speech using TTS API
        response = client.audio.speech.create(
            model="tts-1",  # Text-to-speech model
            voice="alloy",  # Voice type
            input=text  # Input text to convert
        )
        # Save the audio to a file
        speech_file = "output.mp3"
        response.stream_to_file(speech_file)
        return speech_file
