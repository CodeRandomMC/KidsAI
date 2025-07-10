# ui/learn_tab.py
import gradio as gr
from logic.llm_interface import LEARN_SUBJECTS, LEARN_THEMES, safe_generate_lesson

def create_learn_tab():
    """Creates the UI for the Fun Learning tab with guided step-by-step interface."""
    
    # Main header (hideable during generation)
    main_header = gr.Markdown("## 🧠 Let's make learning an adventure!", visible=True)
    sub_header = gr.Markdown("### We'll turn any topic into a fun story! 🎯", visible=True)
    
    # State variables to track selections and current step
    selected_subject = gr.State("")
    selected_theme = gr.State("")
    selected_age = gr.State(6)
    current_step = gr.State(1)  # 1=subject, 2=theme, 3=age, 4=ready
    
    # Step indicator
    step_indicator = gr.Markdown("### Step 1 of 3: What do you want to explore? 🔍")
    
    # Subject selection (initially visible)
    subject_section = gr.Column(visible=True)
    with subject_section:
        gr.Markdown("**Pick something cool to learn about!**")
        with gr.Row():
            subject_buttons = []
            for subject in LEARN_SUBJECTS:
                btn = gr.Button(subject, variant="secondary", size="lg")
                subject_buttons.append(btn)
    
    # Theme selection (initially hidden)
    theme_section = gr.Column(visible=False)
    with theme_section:
        gr.Markdown("**How should we make it fun? Pick your favorite theme!**")
        with gr.Row():
            theme_buttons = []
            for theme in LEARN_THEMES:
                btn = gr.Button(theme, variant="secondary", size="lg")
                theme_buttons.append(btn)
    
    # Age selection (initially hidden)
    age_section = gr.Column(visible=False)
    with age_section:
        gr.Markdown("**How old are you? This helps us tell the story just right!**")
        with gr.Row():
            age_buttons = []
            ages = [4, 5, 6, 7, 8, 9, 10]
            for age in ages:
                btn = gr.Button(f"{age} years old", variant="secondary", size="lg")
                age_buttons.append(btn)
    
    # Summary and create button (initially hidden)
    summary_section = gr.Column(visible=False)
    with summary_section:
        gr.Markdown("**🎉 Perfect! Here's your learning adventure:**")
        selection_summary = gr.Markdown("")
        create_btn = gr.Button("🚀 Start My Learning Adventure!", variant="primary", size="lg")
    
    # Loading animation (initially hidden)
    loading_html = gr.HTML(visible=False, value="""
        <div style="text-align: center; padding: 20px;">
            <div style="display: inline-block; animation: pulse 1.5s infinite; font-size: 3em;">🧠</div>
            <div style="margin-top: 10px; font-style: italic; color: #666;">Creating your personalized lesson...</div>
        </div>
        <style>
            @keyframes pulse {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.1); opacity: 0.7; }
                100% { transform: scale(1); opacity: 1; }
            }
        </style>
    """)
    
    # Lesson output (initially hidden)
    lesson_output = gr.Textbox(label="📚 Your Personal Learning Adventure", interactive=False, lines=8, visible=False)
    
    # AI learning celebration section (initially hidden)
    ai_learning = gr.Column(visible=False)
    with ai_learning:
        gr.Markdown("### 🤖✨ You just learned something new with Artificial Intelligence!")
        gr.Markdown("You picked what to learn and how to learn it, and AI turned it into a fun story just for you! 🎨")
        gr.Markdown("**Amazing fact:** AI can help make any topic fun by connecting it to things you already love!")
    
    new_lesson_btn = gr.Button("🎓 Learn Something Else!", variant="secondary", visible=False)
    
    # Helper functions for guided experience
    def select_subject(subject_choice):
        """Handle subject selection and move to next step"""
        return (
            subject_choice,  # selected_subject
            2,  # current_step (move to theme selection)
            "### Step 2 of 3: Pick Your Adventure Theme! 🎭",  # step_indicator
            gr.Column(visible=False),  # subject_section
            gr.Column(visible=True),   # theme_section
            gr.Column(visible=False),  # age_section
            gr.Column(visible=False)   # summary_section
        )
    
    def select_theme(theme_choice, subject):
        """Handle theme selection and move to next step"""
        return (
            theme_choice,  # selected_theme
            3,  # current_step (move to age selection)
            "### Step 3 of 3: Tell us your age! 🎂",  # step_indicator
            gr.Column(visible=False),  # subject_section
            gr.Column(visible=False),  # theme_section
            gr.Column(visible=True),   # age_section
            gr.Column(visible=False)   # summary_section
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
            "### 🎉 Ready for Your Learning Adventure!",  # step_indicator
            gr.Column(visible=False),  # subject_section
            gr.Column(visible=False),  # theme_section
            gr.Column(visible=False),  # age_section
            gr.Column(visible=True),   # summary_section
            summary_text  # selection_summary
        )
    
    def generate_lesson(subject, theme, age):
        """Generate the lesson and show loading/result"""
        # Hide headers, step indicator, summary section and show loading
        yield (
            gr.Markdown(visible=False),  # main_header
            gr.Markdown(visible=False),  # sub_header
            gr.Markdown(visible=False),  # step_indicator
            gr.Column(visible=False),    # summary_section
            gr.HTML(visible=True),       # loading
            gr.Textbox(visible=False),   # lesson
            gr.Column(visible=False),    # ai_learning
            gr.Button(visible=False)     # new lesson button
        )
        
        # Generate lesson
        lesson_text = safe_generate_lesson(subject, theme, age)
        
        # Show result with AI learning celebration
        yield (
            gr.Markdown(visible=False),  # main_header (keep hidden)
            gr.Markdown(visible=False),  # sub_header (keep hidden)
            gr.Markdown(visible=False),  # step_indicator (keep hidden)
            gr.Column(visible=False),    # summary_section (keep hidden)
            gr.HTML(visible=False),      # loading
            gr.Textbox(value=lesson_text, visible=True),  # lesson
            gr.Column(visible=True),     # ai_learning
            gr.Button(visible=True)      # new lesson button
        )
    
    def reset_lesson():
        """Reset everything back to step 1"""
        return (
            "",  # selected_subject
            "",  # selected_theme
            6,   # selected_age (reset to default)
            1,   # current_step
            gr.Markdown("## 🧠 Let's make learning an adventure!", visible=True),  # main_header (show again)
            gr.Markdown("### We'll turn any topic into a fun story! 🎯", visible=True),  # sub_header (show again)
            "### Step 1 of 3: What do you want to explore? 🔍",  # step_indicator
            gr.Column(visible=True),   # subject_section
            gr.Column(visible=False),  # theme_section
            gr.Column(visible=False),  # age_section
            gr.Column(visible=False),  # summary_section
            "",  # selection_summary
            gr.Textbox(visible=False, value=""),  # lesson_output
            gr.Column(visible=False),  # ai_learning
            gr.Button(visible=False)   # new_lesson_btn
        )
    
    # Connect subject buttons
    for i, btn in enumerate(subject_buttons):
        btn.click(
            fn=lambda i=i: select_subject(LEARN_SUBJECTS[i]),
            outputs=[selected_subject, current_step, step_indicator, 
                    subject_section, theme_section, age_section, summary_section]
        )
    
    # Connect theme buttons
    for i, btn in enumerate(theme_buttons):
        btn.click(
            fn=lambda subject, i=i: select_theme(LEARN_THEMES[i], subject),
            inputs=[selected_subject],
            outputs=[selected_theme, current_step, step_indicator,
                    subject_section, theme_section, age_section, summary_section]
        )
    
    # Connect age buttons
    ages = [4, 5, 6, 7, 8, 9, 10]
    for i, btn in enumerate(age_buttons):
        btn.click(
            fn=lambda subject, theme, i=i: select_age(ages[i], subject, theme),
            inputs=[selected_subject, selected_theme],
            outputs=[selected_age, current_step, step_indicator,
                    subject_section, theme_section, age_section, summary_section, selection_summary]
        )
    
    # Connect create lesson button
    create_btn.click(
        fn=generate_lesson,
        inputs=[selected_subject, selected_theme, selected_age],
        outputs=[main_header, sub_header, step_indicator, summary_section, loading_html, lesson_output, ai_learning, new_lesson_btn]
    )
    
    # Connect new lesson button
    new_lesson_btn.click(
        fn=reset_lesson,
        outputs=[selected_subject, selected_theme, selected_age, current_step, main_header, sub_header, step_indicator,
                subject_section, theme_section, age_section, summary_section, 
                selection_summary, lesson_output, ai_learning, new_lesson_btn]
    )
    
    # Return empty for compatibility with existing interface
    # The old interface expected btn, inputs, outputs but the new guided interface handles everything internally
    return gr.Button(visible=False), [], []