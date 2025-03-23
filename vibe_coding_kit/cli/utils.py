"""
Utility functions for vibe-coding-kit CLI.
Provides common functionality used across different CLI modules.
"""

import os
import sys
from typing import Dict, List, Optional, Tuple


def get_user_input(prompt: str, default: str = "") -> str:
    """
    Get user input with a prompt and optional default value.
    
    Args:
        prompt: Prompt to display to user
        default: Default value if user enters nothing
        
    Returns:
        User input or default value
    """
    if default:
        user_input = input(f"{prompt} [{default}]: ")
        return user_input if user_input else default
    else:
        return input(f"{prompt}: ")


def get_editor_type() -> str:
    """
    Prompt user for editor type preference.
    
    Returns:
        'windsurf' or 'cursor'
    """
    print("\nSelect your preferred editor:")
    print("1. Windsurf")
    print("2. Cursor")
    
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Enter choice (1 or 2): ")
    
    return "windsurf" if choice == "1" else "cursor"
