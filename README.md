# Speech-Enabled Chatbot

This project is a speech-enabled chatbot built using Python. The chatbot listens to the user's voice input, processes it, and uses Google's search engine to retrieve relevant information based on the user's query. The chatbot also performs basic natural language processing, including tokenization and stemming, and responds to greetings and other common queries.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Speech Recognition**: The chatbot captures voice input using the microphone and recognizes speech using the Google Web Speech API.
- **Natural Language Processing**: User input is tokenized and stemmed using the NLTK library.
- **Google Search**: The chatbot performs Google searches and returns the top result for the user's query.
- **Basic Interactions**: The bot responds to greetings, questions about itself, and can exit the conversation upon user request.

## Requirements

- Python 3.x
- Required Python packages:
  - `SpeechRecognition`
  - `nltk`
  - `googlesearch-python`
  - `PyAudio` (required for `SpeechRecognition` to access the microphone)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shreyags831/speech-chatbot.git
   cd speech-chatbot
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data:**

   Run the following commands in Python to download the required NLTK data:

   ```python
   import nltk
   nltk.download('punkt')
   ```

## Usage

1. **Run the chatbot:**

   ```bash
   python chatbot.py
   ```

2. **Interact with the bot:**

   - The bot will listen for your voice input and process it.
   - It will respond to greetings, and if you ask it for information, it will perform a Google search and return the top result.
   - You can ask the bot to introduce itself or simply chat with it.
   - Say "exit" to stop the chatbot.

### Main Components:

1. **`chatbot.py`**: The main script that contains the chatbot logic. It handles speech recognition, natural language processing, and interaction with the user.
2. **`requirements.txt`**: The file that lists the required Python packages for the project.
3. **`README.md`**: Project documentation (this file).

## Troubleshooting

- **Microphone Issues**: If the chatbot is unable to detect audio input, ensure that your microphone is properly configured and that `PyAudio` is installed correctly.
- **Google Search Limitations**: If the bot does not return search results, you might be hitting rate limits or encountering other issues with the Google Search API.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
