import os
from dotenv import load_dotenv
from google import genai



def main():
    initialize_from_persist_environment()
    #This is the main game loop, as of not the global DB will be used.
    while True:
     #This will halt until user input is received
     process_user_input()
     update_environment()
     generative_content()
     persist_environment()

    
def initialize_from_persist_environment():
    #Get secrets from .env 
    load_dotenv()
    #Not needed?
    gemini_api_key = os.getenv(GEMINI_API_KEY)
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2,0-flash", contents="Respond with 123"
    )
    print(response.text)

def process_user_input():
    pass

def update_environment():
    pass

def generative_content():
    pass

def persist_environment():
    pass

if __name__ == "__main__":
    main()