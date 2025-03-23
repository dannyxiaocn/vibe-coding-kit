"""
Global command implementations for vibe-coding-init-kit CLI.
Handles global settings like language preferences.
"""

import os
import json
import re
import sys
from pathlib import Path
from typing import Dict

from .utils import get_user_input, get_editor_type


def get_templates_dir() -> str:
    """
    Get the path to the templates directory.
    
    Returns:
        Path to the templates directory
    """
    package_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.normpath(
        os.path.join(package_dir, '..', '..', 'templates')
    )
    return templates_dir


def global_start_command(
    communication_language: str = None,
    code_comment_language: str = None
) -> None:
    """
    Initialize global settings for vibe-coding-init-kit.
    Save language preferences and other global settings to a Markdown file.
    
    Args:
        communication_language: Communication language preference
        code_comment_language: Code comment language preference
    """
    print("\nInitializing vibe-coding-init-kit global settings...")
    
    # Get editor type
    editor_type = get_editor_type()
    
    # Get language preferences
    if communication_language is None:
        communication_language = get_user_input("What is your preferred communication language?", "English")
    
    if code_comment_language is None:
        code_comment_language = get_user_input("What is your preferred code comment language?", "English")
    
    # Create global rules content in Markdown format
    global_rules_content = "## Language Rules\n"
    global_rules_content += f'communication_language: {communication_language}\n'
    global_rules_content += f'code_comment_language: {code_comment_language}\n'
    
    # Save to global rules markdown file
    templates_dir = get_templates_dir()
    global_rules_path = os.path.join(templates_dir, 'global_rules_template.md')
    
    # Create templates directory if it doesn't exist
    os.makedirs(templates_dir, exist_ok=True)
    
    # Write global rules to file
    with open(global_rules_path, 'w', encoding='utf-8') as f:
        f.write(global_rules_content)
    
    print("\nGlobal settings initialized successfully.")
    print(f"Global rules file saved at: {global_rules_path}")
    print(f"Editor type: {editor_type.capitalize()}")
    print(f"Communication language set to: {communication_language}")
    print(f"Code comment language set to: {code_comment_language}")
    print("\nNow you can use 'vibe start' to initialize projects, and global settings will be automatically applied to each project.")
