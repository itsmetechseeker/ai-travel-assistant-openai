import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

conversation = [
    { "role": "system", "content": "You are a helpful travel assistant who answers questions about Paris for tourists"}    
]

questions = [
     "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
     "Where is the Arc de Triomphe?",
     "What are the must-see artworks at the Louvre Museum?"
]

for question in questions:
    conversation.append({"role":"user","content": question})

    #need to append the response from the model now
    response = client.chat.completions.create(
     model = model,
     messages = conversation,
     temperature = 0.0,
     max_tokens = 100
    )
    response_from_model = response.choices[0].message.content
    conversation.append({"role":"assistant","content": response_from_model})

print(conversation)
print(response.choices[0].message.content)
    
