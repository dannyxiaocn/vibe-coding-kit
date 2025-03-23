"""
Command implementations for vibe-coding-init-kit CLI.
Provides a unified entry point for global and project commands.
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Import global and project command modules
from .utils import get_user_input, get_editor_type
from .global_commands import global_start_command
from .project_commands import project_start_command, create_project_rules_file, create_project_rules_file_with_overrides


def start_command(
    communication_language: str = None,
    code_comment_language: str = None,
    is_global: bool = False
) -> None:
    """
    Unified entry point, decides whether to execute global or project commands based on parameters.
    
    Args:
        communication_language: Communication language preference
        code_comment_language: Code comment language preference
        is_global: Whether to apply global settings
    """
    if is_global:
        # Call global initialization command
        global_start_command(
            communication_language=communication_language,
            code_comment_language=code_comment_language
        )
    else:
        # Call project initialization command
        project_start_command()


def reset_command(
    override_global: bool = False,
    reset_global: bool = False
) -> None:
    """
    Reset or override project/global rules.
    
    Args:
        override_global: Whether to override global settings for this project only
        reset_global: Whether to reset global settings
    """
    # If reset_global is True, update global settings
    if reset_global:
        print("\nReset global settings...")
        from .global_commands import global_start_command
        global_start_command()
        
        # After updating global settings, also update current project rules if in a project
        cwd = os.getcwd()
        windsurf_rules = os.path.join(cwd, '.windsurfrules')
        cursor_rules = os.path.join(cwd, '.cursorrules')
        
        if os.path.exists(windsurf_rules) or os.path.exists(cursor_rules):
            editor_type = "windsurf" if os.path.exists(windsurf_rules) else "cursor"
            print("\nUpdating current project rules to reflect new global settings...")
            from .project_commands import create_project_rules_file
            rules_file_path = create_project_rules_file(editor_type)
            print(f"Project rules updated: {rules_file_path}")
        
        return
    
    # Check if in a project directory
    cwd = os.getcwd()
    windsurf_rules = os.path.join(cwd, '.windsurfrules')
    cursor_rules = os.path.join(cwd, '.cursorrules')
    
    if not os.path.exists(windsurf_rules) and not os.path.exists(cursor_rules):
        print("Error: No .windsurfrules or .cursorrules file found in the current directory.")
        print("Please run 'vibe start' to initialize the project.")
        sys.exit(1)
    
    # Determine which editor type is being used
    editor_type = "windsurf" if os.path.exists(windsurf_rules) else "cursor"
    
    # If override_global is True, create custom global settings for this project
    if override_global:
        print("\nCreating custom global settings for this project...")
        from .utils import get_user_input
        
        # Get user preferences
        print("Please enter project-specific preferences:")
        communication_language = get_user_input("What language would you like to use for communication in this project?", "English")
        code_comment_language = get_user_input("What language would you like to use for code comments in this project?", "English")
        
        # Create or update project rules file with overridden globals
        from .project_commands import create_project_rules_file_with_overrides
        rules_file_path = create_project_rules_file_with_overrides(
            editor_type, 
            communication_language, 
            code_comment_language
        )
        
        print(f"Custom global settings for this project have been created.")
        print(f"Rules file: {rules_file_path}")
        return
    
    # Default case: reset project rules to defaults
    print("\nResetting project rules...")
    from .project_commands import create_project_rules_file
    rules_file_path = create_project_rules_file(editor_type)
    print(f"Project rules have been reset.")
    print(f"Rules file: {rules_file_path}")
    return