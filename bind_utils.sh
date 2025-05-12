#!/bin/bash

# set the path file and repo url
SUBMODULE_PATH="utils"
REPO_URL="https://github.com/leopengningchuan/personal_utils.git"

echo "Checking if submodule already exists..."

if [ -d "$SUBMODULE_PATH" ]; then
    echo "Submodule directory '$SUBMODULE_PATH/' already exists. Skipping addition."
else
    echo "Adding personal_utils as submodule to '$SUBMODULE_PATH/'..."
    git submodule add $REPO_URL $SUBMODULE_PATH
    git submodule update --init --recursive
    echo "Submodule added and initialized successfully."
fi
