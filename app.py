from flask import Flask, render_template, request, jsonify
from models.gpt2_model import load_model, generate_story
from edgechains_integration.blockchain import store_transaction_on_chain
import time

app = Flask(__name__)

# Load the AI model
model, tokenizer = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "Please provide a prompt"}), 400
    
    # Generate the story
    story = generate_story(prompt, model, tokenizer)
    
    # Create transaction data
    transaction = {
        "prompt": prompt,
        "story": story,
        "timestamp": int(time.time())
    }
    
    # Store the prompt and story on the blockchain
    tx_hash = store_transaction_on_chain(transaction)
    
    if tx_hash:
        response = {
            "prompt": prompt,
            "story": story,
            "transaction_hash": tx_hash
        }
    else:
        response = {
            "prompt": prompt,
            "story": story,
            "error": "Failed to store the data on the blockchain."
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
