"""
Project command implementations for vibe-coding-init-kit CLI.
Handles project initialization and rules file creation.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .utils import get_user_input, get_editor_type


def create_project_structure() -> None:
    """
    Create project structure for documentation and code organization.
    """
    # Create dev directory for documentation
    dev_dir = os.path.join(os.getcwd(), "dev")
    os.makedirs(dev_dir, exist_ok=True)
    
    # Create documentation files
    for filename in ["todo.md", "progress.md", "project_description.md", "code_docs.md"]:
        file_path = os.path.join(dev_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                if filename == "todo.md":
                    f.write("# Todo\n")
                elif filename == "progress.md":
                    f.write("# Progress\n")
                elif filename == "project_description.md":
                    f.write("# Project Description\n")
                elif filename == "code_docs.md":
                    f.write("# Code Documentation\n")

def get_global_rules() -> Dict:
    """
    Get global rules from global_rules.md file.
    
    Returns:
        Dictionary of global rules
    """
    # Get package directory path
    package_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.normpath(os.path.join(package_dir, '..', '..'))
    global_rules_path = os.path.join(base_dir, 'templates', 'global_rules_template.md')
    
    if not os.path.exists(global_rules_path):
        return {
            "communication_language": "English",
            "code_comment_language": "English"
        }
    
    # Parse the global rules markdown file
    try:
        with open(global_rules_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract rules using regex patterns for Markdown format
        comm_lang_match = re.search(r'communication_language:\s*(.*?)$', content, re.MULTILINE)
        code_lang_match = re.search(r'code_comment_language:\s*(.*?)$', content, re.MULTILINE)
        
        return {
            "communication_language": comm_lang_match.group(1).strip() if comm_lang_match else "English",
            "code_comment_language": code_lang_match.group(1).strip() if code_lang_match else "English"
        }
    except Exception as e:
        print(f"Error reading global rules: {e}")
        return {
            "communication_language": "English",
            "code_comment_language": "English"
        }


def create_project_rules_file(editor_type: str = "windsurf") -> str:
    """
    Create project rules file for Windsurf or Cursor based on global settings.
    
    Args:
        editor_type: The editor type ("windsurf" or "cursor")
        
    Returns:
        Path to the created rules file
    """
    # Get global rules
    global_rules = get_global_rules()
    
    # Create project rules in Markdown format
    project_rules_content = "# Project Rules\n\n"
    project_rules_content += "## Language Rules\n\n"
    project_rules_content += f"communication_language: User prefers to use {global_rules.get('communication_language', 'English')} to communicate.\n"
    project_rules_content += f"code_comment_language: All code (including codes, comments, plotting information) should be in {global_rules.get('code_comment_language', 'English')} no matter what language is used to communicate.\n\n"
    
    # Add project rules template content if exists
    templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'templates')
    template_path = os.path.join(templates_dir, 'project_rules_template.md')
    if os.path.exists(template_path):
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # Skip header if it exists
            if template_content.startswith('# '):
                template_content = '\n'.join(template_content.split('\n')[1:])
            
            project_rules_content += template_content
        except Exception as e:
            print(f"Warning: Could not read template file: {e}")
    
    # Create rules file path
    file_name = ".windsurfrules" if editor_type == "windsurf" else ".cursorrules"
    rules_file_path = os.path.join(os.getcwd(), file_name)
    
    # Write rules to file
    with open(rules_file_path, 'w', encoding='utf-8') as f:
        f.write(project_rules_content)
    
    return rules_file_path


def create_project_rules_file_with_overrides(
    editor_type: str = "windsurf",
    communication_language: str = "English",
    code_comment_language: str = "English"
) -> str:
    """
    Create project rules file with custom overrides for global settings.
    
    Args:
        editor_type: The editor type ("windsurf" or "cursor")
        communication_language: User's preferred communication language for this project
        code_comment_language: User's preferred code comment language for this project
        
    Returns:
        Path to the created rules file
    """
    # Create project rules in Markdown format
    project_rules_content = "# Project Rules\n\n"
    project_rules_content += "## Language Rules\n\n"
    project_rules_content += f"communication_language: User prefers to use {communication_language} to communicate.\n"
    project_rules_content += f"code_comment_language: All code (including codes, comments, plotting information) should be in {code_comment_language} no matter what language is used to communicate.\n\n"
    
    # Add project rules template content if exists
    templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'templates')
    template_path = os.path.join(templates_dir, 'project_rules_template.md')
    if os.path.exists(template_path):
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # Skip header if it exists
            if template_content.startswith('# '):
                template_content = '\n'.join(template_content.split('\n')[1:])
            
            project_rules_content += template_content
        except Exception as e:
            print(f"Warning: Could not read template file: {e}")
    
    # Create rules file path
    file_name = ".windsurfrules" if editor_type == "windsurf" else ".cursorrules"
    rules_file_path = os.path.join(os.getcwd(), file_name)
    
    # Write rules to file
    with open(rules_file_path, 'w', encoding='utf-8') as f:
        f.write(project_rules_content)
    
    return rules_file_path


def project_start_command() -> None:
    """
    Initialize a project for vibe-coding-init-kit.
    Create project structure and rules file.
    """
    print("\nInitializing vibe-coding-init-kit for this project...")
    
    # Get editor type
    editor_type = get_editor_type()
    
    # Create project structure (documentation and source directories)
    create_project_structure()
    print("Project structure initialization successful.")
    print("Created 'dev' directory and documentation files.")
    
    # Create project rules file
    rules_file_path = create_project_rules_file(editor_type)
    print(f"Created project rules file: {rules_file_path}")
    print(f"Editor type: {editor_type.capitalize()}")
    
    # Check if global rules file exists
    base_dir = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
    global_rules_path = os.path.join(base_dir, 'templates', 'global_rules.md')
    if not os.path.exists(global_rules_path):
        print(f"\nHint: You have not set global preferences. Run 'vibe start --global' to set.")
