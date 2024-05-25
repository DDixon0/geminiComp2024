from dotenv import load_dotenv
import requests
import os

# Load my .env file with my api key
load_dotenv()


def user_query_gemini(query):
    print(query)
    response = "Your response!"
    return response

if __name__ == "__main__":
    print("What is your event query?")

    user_input = input("\n What you want to know?")

    response_data = user_query_gemini(user_input)

