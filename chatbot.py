import google.generativeai as genai
import os
import gradio


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

chat = model.start_chat()

response = chat.send_message("Responda em portugues")

def gradio_wrapper(message, history):
    text = message["text"]
    uploaded_files = []
    for file in message["files"]:
        # import pdb; pdb.set_trace()
        uploaded = genai.upload_file(file)
        uploaded_files.append(uploaded)
    prompt = [text]
    prompt.extend(uploaded_files)
    response = chat.send_message(prompt)
    return response.text



chat_interface = gradio.ChatInterface(fn=gradio_wrapper, multimodal=True, title="Chatbot")
chat_interface.launch()
