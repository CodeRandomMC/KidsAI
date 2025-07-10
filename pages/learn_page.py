# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# pages/learn_page.py
import gradio as gr
from ui.learn_tab import create_learn_tab

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Fun Learning Adventures", elem_classes=["page-title"])
    gr.Markdown("Turn any topic into an exciting adventure! Learn through amazing stories.", elem_classes=["page-subtitle"])
    create_learn_tab()

if __name__ == "__main__":
    demo.launch()
