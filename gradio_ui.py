import gradio as gr

from utils import check_toxicity

demo  = gr.Interface(
    fn=check_toxicity,
    inputs=gr.components.Textbox(label='Input'),
    outputs=gr.components.Label(label='Output'),
    allow_flagging='never'
)
