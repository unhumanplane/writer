from flask import Flask, render_template, request, jsonify
from .llm_services import MockLLMService, OpenAILLMService
import difflib # Add this import

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit', methods=['POST'])
def edit_text():
    data = request.get_json()
    original_text = data.get('text') # This is HTML from Quill
    service_type = request.args.get('service', 'mock')

    if original_text is None:
        return jsonify({'error': 'No text provided'}), 400

    llm_service = None
    # LLM service selection logic
    if service_type == 'openai':
        try:
            llm_service = OpenAILLMService()
            if not llm_service.api_key: # Check if API key was loaded
                 return jsonify({'error': 'OpenAI API key not configured. OpenAILLMService cannot operate.'}), 500
        except Exception as e: # Catch any other unexpected errors during instantiation
             return jsonify({'error': f'Failed to initialize OpenAILLMService: {str(e)}'}), 500
    else: # Default to mock
        llm_service = MockLLMService()
    
    edited_text = llm_service.edit(original_text) # This is HTML from LLM

    # Handle potential errors from the LLM service itself (e.g., API key error during edit)
    if service_type == 'openai' and edited_text.startswith("Error:"):
        return jsonify({'error': edited_text}), 500

    # Generate HTML diff
    # Split the HTML content into lines for difflib
    original_lines = original_text.splitlines()
    edited_lines = edited_text.splitlines()

    # HtmlDiff constructor can take tabsize and wrapcolumn
    # wrapcolumn is how many characters wide the text is before wrapping (default 80)
    html_diff_generator = difflib.HtmlDiff(wrapcolumn=80) 
    diff_table = html_diff_generator.make_table(
        original_lines,
        edited_lines,
        fromdesc='Original Text',
        todesc='Edited Text',
        context=False, # Set to False for full diff without context lines
        numlines=0     # Number of context lines (irrelevant if context=False)
    )

    return jsonify({
        'original_text': original_text,
        'edited_text': edited_text,
        'html_diff': diff_table # Add the diff table to the response
    })

if __name__ == '__main__':
    # Ensure the app runs on a port that's unlikely to be blocked if run in some environments.
    # For local development, debug=True is fine.
    app.run(debug=True, port=5001)
