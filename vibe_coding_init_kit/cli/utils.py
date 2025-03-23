"""
Utility functions for vibe-coding-init-kit CLI.
Provides common functionality used across different CLI modules.
"""

import os
import sys
from typing import Dict, List, Optional, Tuple


def get_user_input(prompt: str, default: str = "") -> str:
    """
    Get input from the user with a default value.
    
    Args:
        prompt: The prompt to display to the user
        default: The default value to use if the user doesn't provide input
        
    Returns:
        The user's input or the default value
    """
    if default:
        user_input = input(f"{prompt} [{default}]: ")
    else:
        user_input = input(f"{prompt}: ")
        
    return user_input if user_input else default


def get_editor_type() -> str:
    """
    Ask the user for the editor type (windsurf or cursor).
    
    Returns:
        Editor type ('windsurf' or 'cursor')
    """
    editor_type = get_user_input("Which editor are you using? (windsurf/cursor)", "windsurf")
    editor_type = editor_type.lower()
    
    if editor_type not in ["windsurf", "cursor"]:
        print(f"Invalid editor type: {editor_type}")
        print("Defaulting to 'windsurf'")
        editor_type = "windsurf"
        
    return editor_type
