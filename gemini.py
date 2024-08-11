from dotenv import load_dotenv
import google.generativeai as genai
import requests
import os

# Load my .env file with my api key
load_dotenv()

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
    system_instruction="You are a causal expert. Using your deduction skills you are going to help the user discover the causal relationships that exist, based on the casual event they input.\nYou will determine 3 causes which resulted in the users causal event alongside 3 possible effects stemming from the users causal event.\nOnly generate causal events once you have sufficiently understood what is the users causal event. Enusre all cauaul evnets are distinct and insightful.\nThink slowly and efficiently.",
)

history=[
    {
        "role": "model",
        "parts": [
        "Please tell me the causal event you would like me to analyze. I'm ready to put my deduction skills to work!  🧠 \n\nFor example, you could say: \"My car wouldn't start this morning.\"  \n\nOnce you provide the event, I will give you 3 possible causes and 3 possible effects. \n",
        ],
    },
]

chat_session = model.start_chat(
    history=history
)





# def user_query_gemini(query):
#     # print(query)
#     response = "Your response!"
#     return response


def user_chat_response(query):
    response = chat_session.send_message(query)

    model_response = response.text

    history.append({"role": "user", "parts": [query]})
    history.append({"role": "model", "parts": [model_response]})

    return model_response


if __name__ == "__main__":



    print("Hello Main!")

    while True:
        user_input = input("You: ")
        print(user_chat_response(user_input))
        print()

    # texts = ["Hello", "Goodbye", "Hi"]
    # result = genai.embed_content(
    #     model="models/text-embedding-004", content=texts, output_dimensionality=2
    # )
    # print(result)

    # while True:

    #     user_input = input("You: ")

    #     chat_session = model.start_chat(
    #     history=history
    #     )

    #     response = chat_session.send_message(user_input)

    #     model_response = response.text

    #     print(model_response)
    #     print()

    #     history.append({"role": "user", "parts": [user_input]})
    #     history.append({"role": "model", "parts": [model_response]})


# response = chat_session.send_message("INSERT_INPUT_HERE")

# print(response.text)


#     print("What is your event query?")

#     user_input = input("\n What you want to know?")

#     response_data = user_query_gemini(user_input)

#     api= f'my api is ={os.getenv("API_KEY")}'

    
