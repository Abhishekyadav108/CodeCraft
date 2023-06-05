import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Your AI Solutions"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "CodeCraft: Your AI Companion for Seamless Coding Solutions")

demo.launch(share=True)