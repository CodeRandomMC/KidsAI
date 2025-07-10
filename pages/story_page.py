# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# pages/story_page.py
import gradio as gr
from ui.story_tab import create_story_tab

with gr.Blocks() as demo:
    gr.Markdown("# 📖 Story Time Adventure", elem_classes=["page-title"])
    gr.Markdown("Create magical stories with AI! Choose your hero, magical item, and adventure world.", elem_classes=["page-subtitle"])
    create_story_tab()

if __name__ == "__main__":
    demo.launch()
