import main
import ollama

def ai_response():

    prompt = main.listen()

    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'system',
            'content': 'Respond with very short responses and you are an advanced ai assistant.',
        },
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    print(response['message']['content'])
    main.tts(response['message']['content'])