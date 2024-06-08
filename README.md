# Multi-Functional Console Application with AI Integration

## Overview

This is a console-based application that uses the Hugging Face API to perform various text-based tasks:

- Text Summarization
- Text Translation
- Text Expansion
- Fact-Checking

Additionally, it supports:

- Summarizing multiple paragraphs individually.
- Saving output (summarized text, translated text, expanded text, or fact-checked information) to a file.

## Features

1. **Text Summarization**: Summarizes input text to provide a concise version.
2. **Text Translation**: Translates text to a specified target language.
3. **Text Expansion**: Expands the input text by adding more context or details.
4. **Fact-Checking**: Checks the factual accuracy of a statement.
5. **Multiple Paragraph Summarization**: Allows summarizing multiple paragraphs separately.
6. **File Saving**: Saves the generated text to a file with options to append or overwrite.

## Evaluation Criteria

### 1. Correctness

- **Input Capture**: The application accurately captures user input for each task.
- **API Interaction**: It effectively communicates with the Hugging Face API to perform the selected operations.
- **Output Display**: Results from API calls are displayed correctly in the console.

### 2. Code Quality

- **Clean Code**: The code is written in a clean and readable manner.
- **Organization**: It follows a logical structure, separating concerns appropriately between different modules (`main.py` for user interaction and `helper.py` for API calls).
- **Comments**: Includes comments where necessary to explain complex logic or functionality.

### 3. Error Handling

- **Graceful Handling**: The application handles errors gracefully, such as network issues or invalid API responses.
- **User Feedback**: Provides clear feedback to the user when errors occur, without crashing or producing unexpected behavior.

### 4. User Experience

- **Ease of Use**: Offers a straightforward and user-friendly interface for interacting with the application.
- **Clear Instructions**: Provides clear and concise instructions for each available task.
- **Feedback**: Offers immediate feedback on the progress and results of the selected operations.

## Getting Started

### Prerequisites

- Python 3.8 or above
- Hugging Face API Key

### Installation

1. **Clone the Repository**

   `git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name`

2. **Create a Virtual Environment (Optional but Recommended)**

   `python -m venv env
 source env/bin/activate`

3. **Install Dependencies**

   `pip install -r requirements.txt`

4. **Set Up Environment Variables**

   `touch .env`
   Add the following line to the .env file:
   `HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here`

5. **Usage**

- Run the Application
  `python main.py`
- Interact with the Console : Follow the on-screen prompts to select tasks, input text, and choose options for saving outputs.

6. **Example Usage**

   Summarize Text:

   - Enter a single paragraph or multiple paragraphs separated by two newlines.
   - Get a concise summary for each paragraph.

   Translate Text:

   - Input the text and specify the target language code.
   - Receive the translated text in the specified language.

   Expand Text:

   - Enter a text to expand.
   - Receive an expanded version with added context.

   Fact-Check Text:

   - Input a statement to fact-check.
   - Receive information about the factual accuracy of the statement.

   Saving Output:

   - Save to File: Input a file name or use the default. Choose to append to or overwrite the file.
