#1. Import syntax
import os
from openai import OpenAI 
from error_handling import call_openai_safely 
from structured_parser import extract_article_data
from content_generator import ContentGenerator

#2. Setup the client with your API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#3. Defining a class that implements the mutli-modal workflow
class SmartContentAssistant: 
    def init(self): 
        self.content_generator = ContentGenerator()

    def create_content_package(self, topic):
        # Step 1: Generate article text with error handling
        article = call_openai_safely(
            f"Write a short informative article about {topic}"
        )
        # Step 2: Extract structured data from the article
        structured_data = extract_article_data(article)
    
        # Step 3: Generate an illustrative image based on article title
        image_url = self.content_generator.generate_image(
            f"Create an illustrative image for: {structured_data['title']}"
        )
    
        # Step 4: Generate audio narration from summary
        audio_file = self.content_generator.generate_speech(
            structured_data['summary']
        )
    
        # Return complete content package
        return {
        "article": article,
        "structured_data": structured_data,
        "image": image_url,
        "audio": audio_file
        }

#4. Example usage to implement the above class
if name == "main": 
    assistant = SmartContentAssistant() 
    content = assistant.create_content_package(
    "renewable energy"
    ) 
    print(f"Created complete content package with text, data, image and audio")
