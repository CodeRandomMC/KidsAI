# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# ui/learn_tab.py
import gradio as gr
from logic.llm_interface import LEARN_SUBJECTS, LEARN_THEMES, safe_generate_lesson

# Subject icons for visual recognition
SUBJECT_ICONS = {
    "Planets": "🪐",
    "Volcanoes": "🌋", 
    "Bees": "🐝",
    "Dinosaurs": "🦕",
    "Ocean": "🌊",
    "Space": "🚀",
    "Animals": "🦁",
    "Plants": "🌱"
}

def get_subject_icon(subject):
    """Get appropriate icon for subject"""
    for key, icon in SUBJECT_ICONS.items():
        if key in subject:
            return icon
    return "📚"

def create_learn_tab():
    """Create the UI for the Fun Learning tab with guided step-by-step interface."""
    
    # State variables to track selections and current step
    selected_subject = gr.State("")
    selected_theme = gr.State("")
    selected_age = gr.State(6)
    current_step = gr.State(1)  # 1=subject, 2=theme, 3=age, 4=ready
    parent_mode = gr.State(False)
    
    # Progress indicator
    progress_indicator = gr.HTML(value="""
        <div class="progress-container">
            <div class="progress-step active" id="step1">1. 📚 Topic</div>
            <div class="progress-step" id="step2">2. 🎭 Theme</div>
            <div class="progress-step" id="step3">3. 🎂 Age</div>
            <div class="progress-step" id="step4">4. 🚀 Create!</div>
        </div>
    """)
    
    # Subject selection (initially visible)
    subject_section = gr.Column(visible=True)
    with subject_section:
        gr.Markdown("### **Pick something cool to learn about!**")
        gr.Markdown("*Choose any topic that interests you - we'll make it fun and exciting!*")
        with gr.Row():
            subject_buttons = []
            for subject in LEARN_SUBJECTS:
                icon = get_subject_icon(subject)
                btn = gr.Button(
                    f"{icon} {subject}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["subject-button"]
                )
                subject_buttons.append(btn)
    
    # Theme selection (initially hidden)
    theme_section = gr.Column(visible=False)
    with theme_section:
        gr.Markdown("### **How should we make it fun? Pick your favorite theme!**")
        gr.Markdown("*This will decide the style of your learning adventure!*")
        with gr.Row():
            theme_buttons = []
            theme_icons = ["🏴‍☠️", "🏰", "🚀", "🦸", "🧙‍♂️", "🔬"]
            for i, theme in enumerate(LEARN_THEMES):
                icon = theme_icons[i % len(theme_icons)]
                btn = gr.Button(
                    f"{icon} {theme}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["theme-button"]
                )
                theme_buttons.append(btn)
    
    # Age selection (initially hidden)
    age_section = gr.Column(visible=False)
    with age_section:
        gr.Markdown("### **How old are you? This helps us tell the story just right!**")
        gr.Markdown("*We'll use words and ideas that are perfect for your age!*")
        with gr.Row():
            age_buttons = []
            ages = [4, 5, 6, 7, 8, 9, 10]
            for age in ages:
                btn = gr.Button(
                    f"""
                    <div class="age-number">{age}</div>
                    <div class="age-label">years old</div>
                    """, 
                    elem_classes=["custom-age-btn"], 
                    variant="secondary"
                )
                age_buttons.append(btn)
    
    # Summary and create button (initially hidden)
    summary_section = gr.Column(visible=False)
    with summary_section:
        gr.Markdown("### **🎉 Perfect! Here's your learning adventure:**")
        selection_summary = gr.Markdown("")
        create_btn = gr.Button("🚀 Start My Learning Adventure!", variant="primary", size="lg")
    
    # Loading animation (initially hidden)
    loading_html = gr.HTML(visible=False, value="""
        <div style="text-align: center; padding: 30px;">
            <div style="display: inline-block; font-size: 4em;" class="pulse-animation">🧠</div>
            <div style="margin-top: 15px; font-size: 1.3em; color: #0ea5e9; font-weight: bold;">Creating your personalized lesson...</div>
            <div style="margin-top: 10px; font-style: italic; color: #666;">Our AI is crafting something special just for you!</div>
        </div>
    """)
    
    # Lesson output (initially hidden) 
    lesson_output = gr.Textbox(
        label="📚 Your Personal Learning Adventure", 
        interactive=False, 
        lines=12, 
        visible=False
    )
    
    # Audio controls (initially hidden)
    audio_section = gr.Column(visible=False)
    with audio_section:
        gr.Markdown("### 🔊 **Listen to your lesson!**")
        audio_button = gr.Button("🔊 Read Aloud", elem_classes=["audio-button"], variant="secondary")
        gr.Markdown("*Click the button above to hear your lesson read out loud!*")
    
    # AI learning celebration section (initially hidden)
    ai_learning = gr.Column(visible=False)
    with ai_learning:
        gr.Markdown("### 🤖✨ **You just learned something new with Artificial Intelligence!**")
        gr.Markdown("You picked what to learn and how to learn it, and AI turned it into a fun story just for you! 🎨")
        gr.Markdown("**Amazing fact:** AI can help make any topic fun by connecting it to things you already love!")
        
        # Fun facts about AI for kids
        with gr.Accordion("🤔 Want to know more about AI?", open=False):
            gr.Markdown("""
            **What is AI?** 
            - AI stands for "Artificial Intelligence" 
            - It's like having a very smart computer friend that can help create stories, answer questions, and learn new things!
            - The AI reads lots and lots of books to learn how to help you learn better
            - AI is used in many things you might know: voice assistants, games, and even some toys!
            """)
    
    new_lesson_btn = gr.Button("🎓 Learn Something Else!", variant="secondary", visible=False)
    
    # Error handling section (initially hidden)
    error_section = gr.Column(visible=False)
    with error_section:
        gr.Markdown("### 😅 **Oops! Our friendly robot got confused!**")
        gr.Markdown("Don't worry - this happens sometimes. Let's try again!")
        retry_btn = gr.Button("🔄 Try Again", variant="primary")
    
    # Helper functions for guided experience
    def update_progress(step):
        """Update progress indicator"""
        steps_html = []
        for i in range(1, 5):
            if i < step:
                class_name = "progress-step completed"
                icon = "✅"
            elif i == step:
                class_name = "progress-step active"
                icon = ["📚", "🎭", "🎂", "🚀"][i-1]
            else:
                class_name = "progress-step"
                icon = ["📚", "🎭", "🎂", "🚀"][i-1]
            
            labels = ["Topic", "Theme", "Age", "Create!"]
            steps_html.append(f'<div class="{class_name}">{i}. {icon} {labels[i-1]}</div>')
        
        return f'<div class="progress-container">{"".join(steps_html)}</div>'
    
    def select_subject(subject_choice):
        """Handle subject selection and move to next step"""
        return (
            subject_choice,  # selected_subject
            2,  # current_step (move to theme selection)
            update_progress(2),  # progress_indicator
            gr.update(visible=False),  # subject_section
            gr.update(visible=True),   # theme_section
            gr.update(visible=False),  # age_section
            gr.update(visible=False),  # summary_section
            gr.update(visible=False)   # error_section
        )
    
    def select_theme(theme_choice, subject):
        """Handle theme selection and move to next step"""
        return (
            theme_choice,  # selected_theme
            3,  # current_step (move to age selection)
            update_progress(3),  # progress_indicator
            gr.update(visible=False),  # subject_section
            gr.update(visible=False),  # theme_section
            gr.update(visible=True),   # age_section
            gr.update(visible=False),  # summary_section
            gr.update(visible=False)   # error_section
        )
    

    
    def select_age(age_choice, subject, theme):
        """Handle age selection and show summary"""
        summary_text = f"""
**🔍 Learning Topic:** {subject}  
**🎭 Fun Theme:** {theme}  
**🎂 Your Age:** {age_choice} years old

**Get ready for a learning adventure tailored just for you!** 🌟
        """
        return (
            age_choice,  # selected_age
            4,  # current_step (ready to create)
            update_progress(4),  # progress_indicator
            gr.update(visible=False),  # subject_section
            gr.update(visible=False),  # theme_section
            gr.update(visible=False),  # age_section
            gr.update(visible=True),   # summary_section
            summary_text,  # selection_summary
            gr.update(visible=False)   # error_section
        )
    
    def generate_lesson(subject, theme, age):
        """Generate the lesson and show loading/result with enhanced error handling"""
        try:
            # Hide summary section and show loading
            yield (
                gr.update(visible=False),    # summary_section
                gr.update(visible=True),     # loading
                gr.update(visible=False),    # lesson
                gr.update(visible=False),    # audio_section
                gr.update(visible=False),    # ai_learning
                gr.update(visible=False),    # new lesson button
                gr.update(visible=False)     # error_section
            )
            
            # Generate lesson
            lesson_text = safe_generate_lesson(subject, theme, age)
            
            # Show result with AI learning celebration
            yield (
                gr.update(visible=False),    # summary_section (keep hidden)
                gr.update(visible=False),    # loading
                gr.update(value=lesson_text, visible=True),  # lesson
                gr.update(visible=True),     # audio_section
                gr.update(visible=True),     # ai_learning
                gr.update(visible=True),     # new lesson button
                gr.update(visible=False)     # error_section
            )
        except Exception as e:
            # Child-friendly error message
            print(f"Error in generate_lesson: {str(e)}")
            yield (
                gr.update(visible=False),    # summary_section
                gr.update(visible=False),    # loading
                gr.update(visible=False),    # lesson
                gr.update(visible=False),    # audio_section
                gr.update(visible=False),    # ai_learning
                gr.update(visible=False),    # new lesson button
                gr.update(visible=True)      # error_section
            )
    
    def reset_lesson():
        """Reset everything back to step 1"""
        return (
            "",  # selected_subject
            "",  # selected_theme
            6,   # selected_age (reset to default)
            1,   # current_step
            update_progress(1),  # progress_indicator
            gr.update(visible=True),   # subject_section
            gr.update(visible=False),  # theme_section
            gr.update(visible=False),  # age_section
            gr.update(visible=False),  # summary_section
            "",  # selection_summary
            gr.update(visible=False, value=""),  # lesson_output
            gr.update(visible=False),  # audio_section
            gr.update(visible=False),  # ai_learning
            gr.update(visible=False),  # new_lesson_btn
            gr.update(visible=False)   # error_section
        )
    
    def handle_audio_playback():
        """Handle audio playback - placeholder for now"""
        return gr.update(value="🔊 Audio feature coming soon! For now, you can read the lesson out loud together.")
    
    # Connect subject buttons
    for i, btn in enumerate(subject_buttons):
        btn.click(
            fn=lambda i=i: select_subject(LEARN_SUBJECTS[i]),
            outputs=[selected_subject, current_step, progress_indicator,
                    subject_section, theme_section, age_section, summary_section, error_section]
        )
    
    # Connect theme buttons
    for i, btn in enumerate(theme_buttons):
        btn.click(
            fn=lambda subject, i=i: select_theme(LEARN_THEMES[i], subject),
            inputs=[selected_subject],
            outputs=[selected_theme, current_step, progress_indicator,
                    subject_section, theme_section, age_section, summary_section, error_section]
        )
    
    # Connect age buttons
    ages = [4, 5, 6, 7, 8, 9, 10]
    for i, btn in enumerate(age_buttons):
        btn.click(
            fn=lambda subject, theme, i=i: select_age(ages[i], subject, theme),
            inputs=[selected_subject, selected_theme],
            outputs=[selected_age, current_step, progress_indicator,
                    subject_section, theme_section, age_section, summary_section, 
                    selection_summary, error_section]
        )
    
    # Connect create lesson button
    create_btn.click(
        fn=generate_lesson,
        inputs=[selected_subject, selected_theme, selected_age],
        outputs=[summary_section, loading_html, lesson_output, audio_section, ai_learning, new_lesson_btn, error_section]
    )
    
    # Connect new lesson button
    new_lesson_btn.click(
        fn=reset_lesson,
        outputs=[selected_subject, selected_theme, selected_age, current_step, progress_indicator,
                subject_section, theme_section, age_section, summary_section, 
                selection_summary, lesson_output, audio_section, ai_learning, new_lesson_btn, error_section]
    )
    
    # Connect retry button
    retry_btn.click(
        fn=reset_lesson,
        outputs=[selected_subject, selected_theme, selected_age, current_step, progress_indicator,
                subject_section, theme_section, age_section, summary_section, 
                selection_summary, lesson_output, audio_section, ai_learning, new_lesson_btn, error_section]
    )
    
    # Connect audio button (placeholder functionality)
    audio_button.click(
        fn=handle_audio_playback,
        outputs=[lesson_output]
    )
    
    # Return empty for compatibility with existing interface
    return gr.Button(visible=False), [], []