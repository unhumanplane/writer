# Intelligent Article Editor

## Description

This project is an intelligent article editor that leverages multiple Large Language Models (LLMs) to collaboratively edit and refine articles. It provides a user-friendly interface to input text, select different LLM services, and view a comparison of the content before and after modifications, highlighting the changes made.

## Features

*   **Rich Text Editing:** Uses Quill.js for a rich text input experience.
*   **LLM Integration:**
    *   Supports multiple LLM services (currently Mock and OpenAI GPT models).
    *   Allows users to select their preferred LLM service via a dropdown menu.
*   **Backend API:** Built with Flask, providing an endpoint for article editing.
*   **Change Tracking & Diffing:**
    *   Calculates the differences between the original and LLM-edited HTML content.
    *   Displays a side-by-side HTML diff view using Python's `difflib`.
*   **Configurable API Key:** OpenAI API key is managed via an environment variable (`OPENAI_API_KEY`) for security.

## Project Structure

```
.
├── article_editor/
│   ├── __init__.py
│   ├── app.py            # Main Flask application, API endpoints
│   ├── llm_services.py   # LLM service abstractions (Base, Mock, OpenAI)
│   ├── static/
│   │   └── style.css     # Basic styles
│   └── templates/
│       └── index.html    # Main HTML page with editor and diff view
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scriptsctivate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Environment Variables:**
    To use the OpenAI LLM service, you need to set the `OPENAI_API_KEY` environment variable.
    ```bash
    export OPENAI_API_KEY="your_openai_api_key_here"
    # On Windows (Command Prompt): set OPENAI_API_KEY="your_openai_api_key_here"
    # On Windows (PowerShell): $env:OPENAI_API_KEY="your_openai_api_key_here"
    ```
    If this key is not set, the OpenAI service will not be available, but the Mock LLM service will still work.

## Usage

1.  **Run the Flask Application:**
    Navigate to the `article_editor` directory (if you are in the root) and run the Flask app:
    ```bash
    # From the project root directory:
    python -m article_editor.app 
    # Or, if you are inside the article_editor directory:
    # python app.py 
    ```
    The application will typically start on `http://127.0.0.1:5001`.

2.  **Open in Browser:**
    Open your web browser and go to `http://127.0.0.1:5001`.

3.  **Using the Editor:**
    *   Enter or paste your article text into the rich text editor.
    *   Select the desired LLM service from the dropdown menu (e.g., "Mock LLM" or "OpenAI LLM").
    *   Click the "Edit with LLM" button.
    *   The original text (as processed), the edited text (from the LLM), and a detailed comparison (diff) will be displayed below.
```
