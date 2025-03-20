# Voice Assistant

A Python-based voice assistant that responds to voice commands, performs system operations, and provides AI-powered responses through an LLM integration.

## Features

- **Voice Recognition**: Listens to voice commands using the speech_recognition library
- **Text-to-Speech**: Responds verbally using pyttsx3 with configurable voice settings
- **System Commands**:
  - Open/close applications (Google, Spotify, VSCode, Discord, etc.)
  - Control system volume
  - Restart/shutdown computer
  - Exit program
- **AI Integration**: Uses Ollama to provide AI-powered responses with the llama3.2 model

## Getting Started

### Prerequisites

- Python 3.x
- The following Python libraries:
  - speech_recognition
  - pyttsx3
  - keyboard
  - comtypes
  - pycaw
  - ollama

### Installation

1. Clone this repository
2. Create and Activate a Virtual Environment

- Create a virtual environment:
`python -m venv .venv`
- Activate the virtual environment:
- For Windows:
`.venv\Scripts\activate`
- This activates the virtual environment and should look like (venv) directory/of/your/project>
- Install Requirements

3. Install all the requirements given in requirements.txt by running the command
  `pip install -r requirements.txt`
4. Ensure Ollama is installed and has the llama3.2 model available

### Usage

1. Run the program:
   ```
   python main.py
   ```
2. The assistant will greet you based on the time of day
3. Press the `/` key to activate listening mode
4. Speak your command after the "Listening..." prompt
5. Press `ESC` at any time to exit the program

## Commands

- **Open Application**: "open [app_name]" (e.g., "open google", "open spotify")
- **Close Application**: "close [app_name]" (e.g., "close notepad", "close calculator")
- **Volume Control**: "change volume" (followed by a number when prompted)
- **System Control**:
  - "restart computer"
  - "shutdown computer"
  - "exit program"
- **AI Assistant**: Say "free" to activate the AI assistant mode and ask any question

## Supported Applications

- Google Chrome
- Spotify
- Visual Studio Code
- Discord
- Notepad
- Calculator
- Steam
- GitHub Desktop
- File Explorer

## Customization

- Change the greeting name by modifying the `greeting` variable
- Adjust TTS voice settings in the `tts()` function
- Add more applications by updating the `apps` dictionary in the `open_app()` and `close_app()` functions

## Hotkeys

- `/` - Activate listening mode
- `ESC` - Exit the program

## Future Improvements

- Add more voice commands and integrations
- Implement wake word detection
- Add support for more applications
- Enhance AI response capabilities

## License

[Your License Here]

## Acknowledgments

- This project uses the Ollama library for AI integration
- Speech recognition powered by Google's speech recognition API
 
