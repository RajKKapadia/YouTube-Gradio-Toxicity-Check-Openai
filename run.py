from fastapi import FastAPI
from fastapi.responses import FileResponse
import gradio as gr

from gradio_ui import demo

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.png')

app = gr.mount_gradio_app(app, demo, path='/gradio')
