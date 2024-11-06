#!/bin/bash

# Define the alias
ALIAS="alias stail='python3 $(pwd)/search_tail/__main__.py \"\$@\"'"

# Function to add alias to the given file
add_alias() {
    local file=$1
    if [ -f "$file" ]; then
        if grep -q "alias stail=" "$file"; then
            echo "Updating existing alias in $file"
            sed -i "/alias stail=/c\\$ALIAS" "$file"
        else
            echo "Adding alias to $file"
            echo "$ALIAS" >> "$file"
        fi
    else
        return 1
    fi
}

# Add alias to .bashrc and .zshrc if they exist
added_to_any=false
if add_alias ~/.bashrc; then
    source ~/.bashrc
    echo "Alias added and sourced in ~/.bashrc"
    added_to_any=true
fi

if add_alias ~/.zshrc; then
    source ~/.zshrc
    echo "Alias added and sourced in ~/.zshrc"
    added_to_any=true
fi

# Provide feedback if neither .bashrc nor .zshrc were found
if [ "$added_to_any" = false ]; then
    echo "Neither ~/.bashrc nor ~/.zshrc were found. Please manually add the following alias to your terminal configuration file:"
    echo "$ALIAS"
else
    echo "Installation complete. You can now use the 'stail' command."
fi
