from transformers import pipeline
import gradio as gr

TextGenerator = pipeline("text-generation",model="gpt2",num_return_sequences=1)

def text_gen(text):
    if len(text.strip())==0:
        return "Please enter a prompt"
    textgen = TextGenerator(text,max_length=100)
    return textgen[0]["generated_text"]

displayUI=gr.Interface(
    fn=text_gen,
    inputs=gr.Textbox(lines=10,placeholder="Enter prompt here"),
    outputs="text",
    title="Text Generator using AI",
    description="Enter a prompt and let AI generate the text"
)

displayUI.launch()