# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# pages/joke_page.py
import gradio as gr
from ui.joke_tab import create_joke_tab

with gr.Blocks() as demo:
    gr.Markdown("# 😂 Joke Factory", elem_classes=["page-title"])
    gr.Markdown("Let's make super silly jokes together! Pick two things and watch the magic happen.", elem_classes=["page-subtitle"])
    create_joke_tab()

if __name__ == "__main__":
    demo.launch()
