# ui/story_tab.py
import gradio as gr
from logic.llm_interface import STORY_HEROES, STORY_ITEMS, STORY_SETTINGS, safe_generate_story

def create_story_tab():
    """Creates the UI for the Story Generator tab with guided step-by-step interface."""
    
    # Main header (hideable during generation)
    main_header = gr.Markdown("## 🎨 Let's build a story together!", visible=True)
    
    # State variables to track selections and current step
    selected_hero = gr.State("")
    selected_item = gr.State("")
    selected_setting = gr.State("")
    current_step = gr.State(1)  # 1=hero, 2=item, 3=setting, 4=ready
    
    # Step indicator
    step_indicator = gr.Markdown("### Step 1 of 3: Choose Your Hero! 🦸‍♀️🦸‍♂️")
    
    # Hero selection (initially visible)
    hero_section = gr.Column(visible=True)
    with hero_section:
        gr.Markdown("**Who will be the hero of your story?**")
        with gr.Row():
            hero_buttons = []
            for hero in STORY_HEROES:
                btn = gr.Button(hero, variant="secondary", size="lg")
                hero_buttons.append(btn)
    
    # Item selection (initially hidden)
    item_section = gr.Column(visible=False)
    with item_section:
        gr.Markdown("**What magical item will help your hero?**")
        with gr.Row():
            item_buttons = []
            for item in STORY_ITEMS:
                btn = gr.Button(item, variant="secondary", size="lg")
                item_buttons.append(btn)
    
    # Setting selection (initially hidden)
    setting_section = gr.Column(visible=False)
    with setting_section:
        gr.Markdown("**Where will your adventure take place?**")
        with gr.Row():
            setting_buttons = []
            for setting in STORY_SETTINGS:
                btn = gr.Button(setting, variant="secondary", size="lg")
                setting_buttons.append(btn)
    
    # Summary and create button (initially hidden)
    summary_section = gr.Column(visible=False)
    with summary_section:
        gr.Markdown("**🎉 Perfect! Here's your story setup:**")
        selection_summary = gr.Markdown("")
        create_btn = gr.Button("✨ Create My Amazing Story!", variant="primary", size="lg")
    
    # Loading animation (initially hidden)
    loading_html = gr.HTML(visible=False, value="""
        <div style="text-align: center; padding: 20px;">
            <div style="display: inline-block; animation: spin 2s linear infinite; font-size: 2em;">✨</div>
            <div style="margin-top: 10px; font-style: italic; color: #666;">Crafting your magical story...</div>
        </div>
        <style>
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    """)
    
    # Story output (initially hidden)
    story_output = gr.Textbox(label="📖 Your Story", interactive=False, lines=8, visible=False)
    
    # AI affirmation section (initially hidden)
    ai_affirmation = gr.Column(visible=False)
    with ai_affirmation:
        gr.Markdown("### 🤖✨ Amazing! You just created this story with Artificial Intelligence!")
        gr.Markdown("You chose the characters and setting, and AI helped bring your imagination to life! 🎨")
    
    story_image = gr.Image(label="🖼️ Your Story Illustration", visible=False)
    
    new_story_btn = gr.Button("🎭 Create Another Story!", variant="secondary", visible=False)
    
    # Helper functions for guided experience
    def select_hero(hero_choice):
        """Handle hero selection and move to next step"""
        return (
            hero_choice,  # selected_hero
            2,  # current_step (move to item selection)
            "### Step 2 of 3: Pick Your Magical Item! ✨",  # step_indicator
            gr.Column(visible=False),  # hero_section
            gr.Column(visible=True),   # item_section
            gr.Column(visible=False),  # setting_section
            gr.Column(visible=False)   # summary_section
        )
    
    def select_item(item_choice, hero, step):
        """Handle item selection and move to next step"""
        return (
            item_choice,  # selected_item
            3,  # current_step (move to setting selection)
            "### Step 3 of 3: Choose Your Adventure World! 🌍",  # step_indicator
            gr.Column(visible=False),  # hero_section
            gr.Column(visible=False),  # item_section
            gr.Column(visible=True),   # setting_section
            gr.Column(visible=False)   # summary_section
        )
    
    def select_setting(setting_choice, hero, item):
        """Handle setting selection and show summary"""
        summary_text = f"""
**🦸‍♀️ Hero:** {hero}  
**✨ Magical Item:** {item}  
**🌍 World:** {setting_choice}
        """
        return (
            setting_choice,  # selected_setting
            4,  # current_step (ready to create)
            "### 🎉 Ready to Create Your Story!",  # step_indicator
            gr.Column(visible=False),  # hero_section
            gr.Column(visible=False),  # item_section
            gr.Column(visible=False),  # setting_section
            gr.Column(visible=True),   # summary_section
            summary_text  # selection_summary
        )
    
    def generate_story(hero, item, setting):
        """Generate the story and show loading/result"""
        # Hide main header, step indicator, summary section and show loading
        yield (
            gr.Markdown(visible=False),  # main_header
            gr.Markdown(visible=False),  # step_indicator
            gr.Column(visible=False),    # summary_section
            gr.HTML(visible=True),       # loading
            gr.Textbox(visible=False),   # story
            gr.Column(visible=False),    # ai_affirmation
            gr.Image(visible=False),     # story_image
            gr.Button(visible=False)     # new story button
        )
        
        # Generate story
        story_text, image_path = safe_generate_story(hero, item, setting)
        
        # Show result with AI affirmation and optional image
        show_image = image_path is not None
        yield (
            gr.Markdown(visible=False),  # main_header (keep hidden)
            gr.Markdown(visible=False),  # step_indicator (keep hidden)
            gr.Column(visible=False),    # summary_section (keep hidden)
            gr.HTML(visible=False),      # loading
            gr.Textbox(value=story_text, visible=True),  # story
            gr.Column(visible=True),     # ai_affirmation
            gr.Image(value=image_path, visible=show_image),    # story_image
            gr.Button(visible=True)      # new story button
        )
    
    def reset_story():
        """Reset everything back to step 1"""
        return (
            "",  # selected_hero
            "",  # selected_item
            "",  # selected_setting
            1,   # current_step
            gr.Markdown("## 🎨 Let's build a story together!", visible=True),  # main_header (show again)
            "### Step 1 of 3: Choose Your Hero! 🦸‍♀️🦸‍♂️",  # step_indicator
            gr.Column(visible=True),   # hero_section
            gr.Column(visible=False),  # item_section
            gr.Column(visible=False),  # setting_section
            gr.Column(visible=False),  # summary_section
            "",  # selection_summary
            gr.Textbox(visible=False, value=""),  # story_output
            gr.Column(visible=False),  # ai_affirmation
            gr.Image(visible=False),   # story_image
            gr.Button(visible=False)   # new_story_btn
        )
    
    # Connect hero buttons
    for i, btn in enumerate(hero_buttons):
        btn.click(
            fn=lambda i=i: select_hero(STORY_HEROES[i]),
            outputs=[selected_hero, current_step, step_indicator, 
                    hero_section, item_section, setting_section, summary_section]
        )
    
    # Connect item buttons
    for i, btn in enumerate(item_buttons):
        btn.click(
            fn=lambda hero, step, i=i: select_item(STORY_ITEMS[i], hero, step),
            inputs=[selected_hero, current_step],
            outputs=[selected_item, current_step, step_indicator,
                    hero_section, item_section, setting_section, summary_section]
        )
    
    # Connect setting buttons
    for i, btn in enumerate(setting_buttons):
        btn.click(
            fn=lambda hero, item, i=i: select_setting(STORY_SETTINGS[i], hero, item),
            inputs=[selected_hero, selected_item],
            outputs=[selected_setting, current_step, step_indicator,
                    hero_section, item_section, setting_section, summary_section, selection_summary]
        )
    
    # Connect create story button
    create_btn.click(
        fn=generate_story,
        inputs=[selected_hero, selected_item, selected_setting],
        outputs=[main_header, step_indicator, summary_section, loading_html, story_output, ai_affirmation, story_image, new_story_btn]
    )
    
    # Connect new story button
    new_story_btn.click(
        fn=reset_story,
        outputs=[selected_hero, selected_item, selected_setting, current_step, main_header, step_indicator,
                hero_section, item_section, setting_section, summary_section, 
                selection_summary, story_output, ai_affirmation, story_image, new_story_btn]
    )