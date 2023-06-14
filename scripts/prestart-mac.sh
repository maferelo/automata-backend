#!/bin/bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install --cask docker visual-studio-code

code --install-extension ms-vscode-remote.remote-containers

brew install pyenv

curl -sSL https://install.python-poetry.org | python3 -
echo "export PATH='$HOME/.local/bin:$PATH'" >> ~/.zshrc

code .
