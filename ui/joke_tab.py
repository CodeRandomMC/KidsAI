# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# ui/joke_tab.py
import gradio as gr
from logic.llm_interface import JOKE_SUBJECTS_1, JOKE_SUBJECTS_2, safe_generate_joke

# Joke subject icons for visual recognition
SUBJECT1_ICONS = {
    "Animals": "🐾",
    "Food": "🍕", 
    "School": "🏫",
    "Space": "🚀",
    "Pirates": "🏴‍☠️",
    "Robots": "🤖",
    "Sports": "⚽",
    "Music": "🎵"
}

SUBJECT2_ICONS = {
    "Dancing": "💃",
    "Flying": "✈️",
    "Cooking": "👨‍🍳",
    "Swimming": "🏊‍♀️",
    "Singing": "🎤",
    "Sleeping": "😴",
    "Playing": "🎮",
    "Reading": "📚"
}

def get_joke_icon(subject, icon_dict):
    """Get appropriate icon for joke subject"""
    for key, icon in icon_dict.items():
        if key in subject:
            return icon
    return "😄"

def create_joke_tab():
    """Creates the UI for the Joke Factory tab with guided step-by-step interface."""
    
    # State variables to track selections and current step
    selected_subject1 = gr.State("")
    selected_subject2 = gr.State("")
    current_step = gr.State(1)  # 1=first subject, 2=second subject, 3=ready
    
    # Progress indicator
    progress_indicator = gr.HTML(value="""
        <div class="progress-container">
            <div class="progress-step active" id="step1">1. 😄 First Thing</div>
            <div class="progress-step" id="step2">2. 🎭 Second Thing</div>
            <div class="progress-step" id="step3">3. 🤣 Joke Time!</div>
        </div>
    """)
    
    # First subject selection (initially visible)
    subject1_section = gr.Column(visible=True)
    with subject1_section:
        gr.Markdown("### **What should we start our joke with?**")
        gr.Markdown("*Pick anything you find interesting - we'll make it funny!*")
        with gr.Row():
            subject1_buttons = []
            for subject in JOKE_SUBJECTS_1:
                icon = get_joke_icon(subject, SUBJECT1_ICONS)
                btn = gr.Button(
                    f"{icon} {subject}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["subject-button"]
                )
                subject1_buttons.append(btn)
    
    # Second subject selection (initially hidden)
    subject2_section = gr.Column(visible=False)
    with subject2_section:
        gr.Markdown("### **What should we mix it with?**")
        gr.Markdown("*Choose an action or activity to create something silly!*")
        with gr.Row():
            subject2_buttons = []
            for subject in JOKE_SUBJECTS_2:
                icon = get_joke_icon(subject, SUBJECT2_ICONS)
                btn = gr.Button(
                    f"{icon} {subject}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["theme-button"]
                )
                subject2_buttons.append(btn)
    
    # Summary and create button (initially hidden)
    summary_section = gr.Column(visible=False)
    with summary_section:
        gr.Markdown("### **🎉 Perfect! Let's see what funny thing happens when we mix:**")
        selection_summary = gr.Markdown("")
        create_btn = gr.Button("🤣 Tell Me The Joke!", variant="primary", size="lg")
    
    # Loading animation (initially hidden)
    loading_html = gr.HTML(visible=False, value="""
        <div style="text-align: center; padding: 30px;">
            <div style="display: inline-block; font-size: 4em;" class="pulse-animation">😂</div>
            <div style="margin-top: 15px; font-size: 1.3em; color: #0ea5e9; font-weight: bold;">Cooking up something hilarious...</div>
            <div style="margin-top: 10px; font-style: italic; color: #666;">Our AI comedian is crafting the perfect joke!</div>
        </div>
    """)
    
    # Joke output (initially hidden)
    joke_output = gr.Textbox(
        label="🎭 Your Hilarious Joke", 
        interactive=False, 
        lines=6, 
        visible=False
    )
    
    # Joke rating section (initially hidden)
    joke_rating_section = gr.Column(visible=False)
    with joke_rating_section:
        gr.Markdown("### **How funny was that? Rate your joke!**")
        with gr.Row():
            rating_buttons = []
            emojis = ["😍", "😂", "😄", "😊", "😐"]
            labels = ["Hilarious!", "Very Funny!", "Pretty Good!", "Okay!", "Try Again!"]
            for emoji, label in zip(emojis, labels):
                btn = gr.Button(f"{emoji} {label}", variant="secondary", size="sm")
                rating_buttons.append(btn)
    
    # Audio controls for joke (initially hidden)
    joke_audio_section = gr.Column(visible=False)
    with joke_audio_section:
        gr.Markdown("### 🔊 **Listen to your joke!**")
        joke_audio_button = gr.Button("🔊 Read Joke Aloud", elem_classes=["audio-button"], variant="secondary")
        gr.Markdown("*Perfect for sharing with family and friends!*")
    
    # AI celebration section (initially hidden)
    ai_celebration = gr.Column(visible=False)
    with ai_celebration:
        gr.Markdown("### 🤖🎉 **You just created this joke with Artificial Intelligence!**")
        gr.Markdown("You picked the ingredients, and AI mixed them into something funny! 😄")
        
        # Make another joke section
        with gr.Row():
            with gr.Column():
                another_joke_btn = gr.Button("🎪 Make Another Joke!", variant="primary", size="lg")
        
        # Fun facts about AI and humor
        with gr.Accordion("🤔 How does AI make jokes?", open=False):
            gr.Markdown("""
            **AI Joke Creation:**
            - AI learns patterns from thousands of jokes to understand what's funny
            - It finds unexpected connections between different things
            - The surprise element is what makes jokes work!
            - AI can combine ideas in ways humans might not think of
            
            **Fun Fact:** The best jokes often mix two completely different things - just like what you did!
            
            **Joke Tips:**
            - The funnier jokes usually have the most unexpected combinations
            - Try mixing things that seem completely opposite
            - Sometimes the silliest combinations make the best jokes!
            """)
    
    # Error handling section (initially hidden)
    error_section = gr.Column(visible=False)
    with error_section:
        gr.Markdown("### 😅 **Oops! Our joke robot got tongue-tied!**")
        gr.Markdown("Even comedians have off days. Let's try making another joke!")
        retry_btn = gr.Button("🔄 Try Again", variant="primary")
    
    # Helper functions for guided experience
    def update_joke_progress(step):
        """Update progress indicator for joke creation"""
        steps_html = []
        icons = ["😄", "🎭", "🤣"]
        labels = ["First Thing", "Second Thing", "Joke Time!"]
        
        for i in range(1, 4):
            if i < step:
                class_name = "progress-step completed"
                icon = "✅"
            elif i == step:
                class_name = "progress-step active"
                icon = icons[i-1]
            else:
                class_name = "progress-step"
                icon = icons[i-1]
            
            steps_html.append(f'<div class="{class_name}">{i}. {icon} {labels[i-1]}</div>')
        
        return f'<div class="progress-container">{"".join(steps_html)}</div>'
    
    def select_subject1(subject_choice):
        """Handle first subject selection and move to next step"""
        return (
            subject_choice,  # selected_subject1
            2,  # current_step (move to second subject)
            update_joke_progress(2),  # progress_indicator
            gr.update(visible=False),  # subject1_section
            gr.update(visible=True),   # subject2_section
            gr.update(visible=False),  # summary_section
            gr.update(visible=False)   # error_section
        )
    
    def select_subject2(subject_choice, subject1):
        """Handle second subject selection and show summary"""
        subject1_icon = get_joke_icon(subject1, SUBJECT1_ICONS)
        subject2_icon = get_joke_icon(subject_choice, SUBJECT2_ICONS)
        
        summary_text = f"""
**{subject1_icon} First Thing:** {subject1}  
**{subject2_icon} Second Thing:** {subject_choice}  

**What happens when we mix them? Let's find out!** 🤔➡️😂
        """
        return (
            subject_choice,  # selected_subject2
            3,  # current_step (ready to create)
            update_joke_progress(3),  # progress_indicator
            gr.update(visible=False),  # subject1_section
            gr.update(visible=False),  # subject2_section
            gr.update(visible=True),   # summary_section
            summary_text,  # selection_summary
            gr.update(visible=False)   # error_section
        )
    
    def generate_joke(subject1, subject2):
        """Generate the joke and show loading/result with enhanced error handling"""
        try:
            # Hide summary section and show loading
            yield (
                gr.update(visible=False),    # summary_section
                gr.update(visible=True),     # loading
                gr.update(visible=False),    # joke
                gr.update(visible=False),    # joke_rating_section
                gr.update(visible=False),    # joke_audio_section
                gr.update(visible=False),    # ai_celebration
                gr.update(visible=False)     # error_section
            )
            
            # Generate joke
            joke_text = safe_generate_joke(subject1, subject2)
            
            # Show result with AI celebration
            yield (
                gr.update(visible=False),    # summary_section (keep hidden)
                gr.update(visible=False),    # loading
                gr.update(value=joke_text, visible=True),  # joke
                gr.update(visible=True),     # joke_rating_section
                gr.update(visible=True),     # joke_audio_section
                gr.update(visible=True),     # ai_celebration
                gr.update(visible=False)     # error_section
            )
        except Exception as e:
            # Child-friendly error message
            print(f"Error in generate_joke: {str(e)}")
            yield (
                gr.update(visible=False),    # summary_section
                gr.update(visible=False),    # loading
                gr.update(visible=False),    # joke
                gr.update(visible=False),    # joke_rating_section
                gr.update(visible=False),    # joke_audio_section
                gr.update(visible=False),    # ai_celebration
                gr.update(visible=True)      # error_section
            )
    
    def reset_joke():
        """Reset everything back to step 1"""
        return (
            "",  # selected_subject1
            "",  # selected_subject2
            1,   # current_step
            update_joke_progress(1),  # progress_indicator
            gr.update(visible=True),   # subject1_section
            gr.update(visible=False),  # subject2_section
            gr.update(visible=False),  # summary_section
            "",  # selection_summary
            gr.update(visible=False, value=""),  # joke_output
            gr.update(visible=False),  # joke_rating_section
            gr.update(visible=False),  # joke_audio_section
            gr.update(visible=False),  # ai_celebration
            gr.update(visible=False)   # error_section
        )
    
    def handle_joke_rating(rating):
        """Handle joke rating"""
        return gr.update(value=f"Thanks for rating our joke {rating}! We're glad you enjoyed it.")
    
    def handle_joke_audio():
        """Handle joke audio playback - placeholder for now"""
        return gr.update(value="🔊 Audio feature coming soon! For now, try reading the joke out loud with funny voices!")
    
    # Event Listeners
    
    # Connect first subject buttons
    for i, btn in enumerate(subject1_buttons):
        btn.click(
            fn=lambda i=i: select_subject1(JOKE_SUBJECTS_1[i]),
            outputs=[selected_subject1, current_step, progress_indicator,
                    subject1_section, subject2_section, summary_section, error_section]
        )
    
    # Connect second subject buttons
    for i, btn in enumerate(subject2_buttons):
        btn.click(
            fn=lambda subject1, i=i: select_subject2(JOKE_SUBJECTS_2[i], subject1),
            inputs=[selected_subject1],
            outputs=[selected_subject2, current_step, progress_indicator,
                    subject1_section, subject2_section, summary_section, 
                    selection_summary, error_section]
        )
    
    # Connect create joke button
    create_btn.click(
        fn=generate_joke,
        inputs=[selected_subject1, selected_subject2],
        outputs=[summary_section, loading_html, joke_output, joke_rating_section, 
                joke_audio_section, ai_celebration, error_section]
    )
    
    # Connect rating buttons
    for i, btn in enumerate(rating_buttons):
        btn.click(
            fn=lambda i=i: handle_joke_rating(emojis[i]),
            outputs=[joke_output]
        )
    
    # Connect audio button
    joke_audio_button.click(
        fn=handle_joke_audio,
        outputs=[joke_output]
    )
    
    # Connect another joke button
    another_joke_btn.click(
        fn=reset_joke,
        outputs=[selected_subject1, selected_subject2, current_step, progress_indicator,
                subject1_section, subject2_section, summary_section, 
                selection_summary, joke_output, joke_rating_section, 
                joke_audio_section, ai_celebration, error_section]
    )
    
    # Connect retry button
    retry_btn.click(
        fn=reset_joke,
        outputs=[selected_subject1, selected_subject2, current_step, progress_indicator,
                subject1_section, subject2_section, summary_section, 
                selection_summary, joke_output, joke_rating_section, 
                joke_audio_section, ai_celebration, error_section]
    )
    
    # Return empty for compatibility with existing interface
    return gr.Button(visible=False), [], []