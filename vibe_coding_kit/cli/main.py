"""
Main CLI module for vibe-coding-kit.
Provides command line interface for interacting with vibe-coding-kit.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List

from .commands import start_command, reset_command


def print_welcome_badge() -> None:
    """
    Print a colorful welcome badge when the vibe command is run without arguments.
    """
    # 标准颜色
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # 亮色版本
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    RESET = "\033[0m"
    
    badge = f"""{BRIGHT_CYAN}
██╗   ██╗██╗██████╗ ███████╗            {WHITE}██████╗    ██╗   
{BRIGHT_CYAN}██║   ██║██║██╔══██╗██╔════╝           {BRIGHT_MAGENTA}██╔═████╗  ███║   
{BRIGHT_BLUE}██║   ██║██║██████╔╝█████╗             {BRIGHT_MAGENTA}██║██╔██║  ╚██║   
{BRIGHT_BLUE}╚██╗ ██╔╝██║██╔══██╗██╔══╝             {BRIGHT_MAGENTA}████╔╝██║   ██║   
{BLUE} ╚████╔╝ ██║██████╔╝███████╗██╗{BRIGHT_RED}███████╗{MAGENTA}╚██████╔╝██╗██║   
{BLUE}  ╚═══╝  ╚═╝╚═════╝ ╚══════╝╚═╝{BRIGHT_RED}╚══════╝{MAGENTA} ╚═════╝ ╚═╝╚═╝   
{BRIGHT_GREEN} ██████╗ ██████╗ ██████╗ ███████╗    ██╗  ██╗██╗████████╗
{BRIGHT_GREEN}██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██║ ██╔╝██║╚══██╔══╝
{GREEN}██║     ██║   ██║██║  ██║█████╗█████╗█████╔╝ ██║   ██║   
{GREEN}██║     ██║   ██║██║  ██║██╔══╝╚════╝██╔═██╗ ██║   ██║   
{GREEN}╚██████╗╚██████╔╝██████╔╝███████╗    ██║  ██╗██║   ██║   
{GREEN} ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝   ╚═╝   
{RESET}"""
    print(badge)


def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI.
    
    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        prog='vibe',
        description='Vibe-coding-kit: Enhance code maintainability through Windsurf/Cursor rules'
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
    Check if this is the first run of vibe-coding-kit.
    
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
        print("Welcome to vibe-coding-kit!")
        print("This appears to be your first run. We'll set up global settings first.")
        start_command(is_global=True)
        print("\nGlobal setup complete. Now you can use 'vibe start' to initialize projects.")
        return

    # Normal command parsing
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command is None:
        # Show welcome badge before help info
        print_welcome_badge()
        parser.print_help()
        sys.exit(0)
    
    if args.command == 'start':
        print_welcome_badge()
        start_command(
            is_global=getattr(args, 'is_global', False)
        )
    elif args.command == 'reset':
        print_welcome_badge()
        reset_command(
            override_global=getattr(args, 'override_global', False),
            reset_global=getattr(args, 'reset_global', False)
        )
    
    
if __name__ == '__main__':
    main()
