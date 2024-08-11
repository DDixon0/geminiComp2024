from dotenv import load_dotenv
import google.generativeai as genai
import requests
import os

# Load my .env file with my api key
load_dotenv()


def user_query_gemini(query):
    # print(query)
    response = "Your response!"
    return response

if __name__ == "__main__":


    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    #system_instruction="",
    )

    history=[]

    while True:

        user_input = input("You: ")

        chat_session = model.start_chat(
        history=history
        )

        response = chat_session.send_message(user_input)

        model_response = response.text

        print(model_response)
        print()

        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "model", "parts": [model_response]})


# response = chat_session.send_message("INSERT_INPUT_HERE")

# print(response.text)


#     print("What is your event query?")

#     user_input = input("\n What you want to know?")

#     response_data = user_query_gemini(user_input)

#     api= f'my api is ={os.getenv("API_KEY")}'

    


   
