from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

# GPT-3.5 model prompt
model_prompt = ">>> "


userInputs = []
modelOutputs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Combine user input with model prompt
    chat_input = model_prompt + user_input

    # Generate a response from the model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=chat_input,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated response
    model_output = response.choices[0].text.strip()
    
    if user_input and model_output:
        userInputs.append(user_input)
        modelOutputs.append(model_output)
            
    return render_template('index.html', user_input=userInputs, 
                           model_output=modelOutputs, zip=zip)

if __name__ == '__main__':
    app.run(debug=True)

