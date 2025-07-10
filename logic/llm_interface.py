# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# logic/llm_interface.py
import time
import random

# --- Placeholder Data ---
# This data would come from a secure, curated database in a real application.
STORY_HEROES = ["a Brave Knight", "a Curious Astronaut", "a Clever Fox", "a Giggling Ghost"]
STORY_ITEMS = ["a Flying Carpet", "a Pair of Sparkling Boots", "a Magical Singing Shell"]
STORY_SETTINGS = ["an Enchanted Forest", "a Bouncy Castle on the Moon", "a Crystal Cave"]

JOKE_SUBJECTS_1 = ["a Dinosaur", "a Banana", "a Ghost", "a Robot"]
JOKE_SUBJECTS_2 = ["a Jellybean", "a Trampoline", "a Library Book", "a Soccer Ball"]

LEARN_SUBJECTS = ["How Planets Move", "Why Volcanoes Erupt", "How Bees Make Honey"]
LEARN_THEMES = ["Pirate Ships", "Magical Spells", "Superhero Training"]

# --- Simulated AI Logic ---

def safe_generate_story(hero, item, setting):
    """
    Simulates the "Creator" and "Safety Monitor" pipeline for stories.
    """
    print("[Logic] 1. Constructing prompt for Creator LLM...")
    # In a real app, you'd format a detailed prompt here.
    
    print(f"[Logic] 2. Calling Creator LLM with: ({hero}, {item}, {setting})")
    time.sleep(1.5) # Simulate API call latency
    
    # Simulated "Creator" output
    story = (
        f"Once upon a time, in {setting}, there was {hero}. "
        f"This hero had a very special treasure: {item}! One sunny morning, "
        f"they went on a grand adventure to find the legendary Giggling Grove. "
        "Everyone they met was kind and the journey was full of fun and laughter. The end!"
    )
    
    print("[Logic] 3. Passing story to Safety Monitor LLM for review...")
    time.sleep(0.5) # Simulate review latency
    
    # Simulated "Safety Monitor" check. In our stub, it always passes.
    safety_check_passed = True
    print(f"[Logic] 4. Safety Monitor result: {'PASS' if safety_check_passed else 'FAIL'}")
    
    if safety_check_passed:
        # Return the safe story and no image for now
        # In a real implementation, this would be a generated image
        return story, None
    else:
        # Return a generic, safe message if the check fails
        return "Oops! Let's try a different story. How about another one?", None

def safe_generate_joke(subject1, subject2):
    """
    Simulates a safe joke generation with variety for kids.
    """
    print(f"[Logic] Generating joke for: ({subject1}, {subject2})")
    time.sleep(1) # Simulate API call
    
    # Multiple joke templates for variety
    joke_templates = [
        f"What do you get when you cross {subject1} with {subject2}?\n\nSomething super silly that makes everyone giggle! 😄",
        f"Why did {subject1} meet {subject2}?\n\nBecause they wanted to have a funny adventure together! 🎉",
        f"What happens when {subject1} and {subject2} become best friends?\n\nThey create the most amazing giggles in the whole world! 🌟",
        f"What do you call {subject1} dancing with {subject2}?\n\nThe silliest, most wonderful dance party ever! 💃🕺",
        f"How do {subject1} and {subject2} tell jokes?\n\nThey tickle each other until everyone starts laughing! 🤣",
    ]
    
    # Pick a random template for variety
    joke = random.choice(joke_templates)
    
    # No safety monitor needed for these simple templates, but you could add one.
    return joke

def safe_generate_lesson(subject, theme, age):
    """
    Simulates a safe educational content generation.
    """
    print(f"[Logic] Generating lesson for age {age} on '{subject}' with theme '{theme}'")
    time.sleep(1.5)
    
    # Simulated "Creator" + "Safety Monitor"
    lesson = (
        f"Hello, future genius! You're {age} and that's a great age to learn! "
        f"Let's imagine you're on a big Pirate Ship and you want to know {subject.lower()}.\n\n"
        f"Think of it like this: The universe is a giant ocean, and the planets are like pirate ships following a secret treasure map around the big, bright sun! "
        f"They all follow their own path so they don't bump into each other. Isn't that neat? "
        f"Keep being curious!"
    )
    
    return lesson