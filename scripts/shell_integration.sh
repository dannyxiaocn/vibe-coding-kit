#!/bin/bash
# Shell integration for vibe-coding-init-kit

# Determine shell type
shell_type=$(basename "$SHELL")

# Path to the initialization script
init_script=""

if [ "$shell_type" = "zsh" ]; then
    # For ZSH
    init_script="$HOME/.zshrc"
elif [ "$shell_type" = "bash" ]; then
    # For Bash
    init_script="$HOME/.bashrc"
else
    echo "Unsupported shell: $shell_type"
    echo "Please manually add the vibe command to your shell initialization script."
    exit 1
fi

# Add vibe command to shell initialization script if not already present
if ! grep -q "# vibe-coding-init-kit integration" "$init_script"; then
    echo "" >> "$init_script"
    echo "# vibe-coding-init-kit integration" >> "$init_script"
    echo 'export PATH="$PATH:$HOME/.local/bin"  # Ensure local bin is in PATH' >> "$init_script"
    echo "alias vibe-init='vibe start'" >> "$init_script"
    echo "alias vibe-global='vibe start --global'" >> "$init_script"
    echo "" >> "$init_script"
    
    echo "Shell integration added to $init_script"
    echo "Please restart your shell or run 'source $init_script' to apply changes."
else
    echo "Shell integration already exists in $init_script"
fi
