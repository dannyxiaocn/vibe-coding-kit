"""
Main CLI module for vibe-coding-init-kit.
Provides command line interface for interacting with vibe-coding-init-kit.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List

from .commands import start_command, reset_command


def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI.
    
    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        prog='vibe',
        description='Vibe-coding-init-kit: Enhance code maintainability through Windsurf/Cursor rules'
    )
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Start command - initialize project or global settings
    start_parser = subparsers.add_parser(
        'start',
        help='Initialize project structure or set global language preferences'
    )
    start_parser.add_argument(
        '--global',
        dest='is_global',
        action='store_true',
        help='Apply global settings (set language preferences)'
    )
    
    # Reset command - reset existing project rules to defaults
    reset_parser = subparsers.add_parser(
        'reset',
        help='Reset project rules to defaults (keeping global settings)'
    )
    reset_parser.add_argument(
        '--override',
        dest='override_global',
        action='store_true',
        help='Override global settings for this project only'
    )
    reset_parser.add_argument(
        '--global',
        dest='reset_global',
        action='store_true',
        help='Reset global settings'
    )
    
    return parser


def is_first_run() -> bool:
    """
    Check if this is the first run of vibe-coding-init-kit.
    
    Returns:
        True if this is the first run (global rules don't exist yet), False otherwise
    """
    # Determine the location of global rules file
    package_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.normpath(os.path.join(package_dir, '..', '..'))
    global_rules_path = os.path.join(base_dir, 'templates', 'global_rules_template.md')
    
    # Check if global rules file exists
    return not os.path.exists(global_rules_path)


def main() -> None:
    """
    Main entry point for the CLI.
    """
    # Check if this is the first run and no command is specified
    if is_first_run():
        print("Welcome to vibe-coding-init-kit!")
        print("This appears to be your first run. We'll set up global settings first.")
        start_command(is_global=True)
        print("\nGlobal setup complete. Now you can use 'vibe start' to initialize projects.")
        return

    # Normal command parsing
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(0)
    
    if args.command == 'start':
        start_command(
            is_global=getattr(args, 'is_global', False)
        )
    elif args.command == 'reset':
        reset_command(
            override_global=getattr(args, 'override_global', False),
            reset_global=getattr(args, 'reset_global', False)
        )
    
    
if __name__ == '__main__':
    main()
