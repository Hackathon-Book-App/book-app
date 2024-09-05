# ENVIRONMENT SETUP

Instructions and usefull links for setting up and working in this project

> **What you will need to set up**  
1. [VS Code](#vs-code)
1. [Git](#git)
    * [Git setup](#git-setup)
    * [GitHub setup](#github-setup)
    * [Cloning Repositories](#cloning-repositories)
1. [Python](#python)
    * [Python venv](#python-venv)

## VS Code

1. Install [VS Code](https://code.visualstudio.com/)
1. Go to Extensions install the `Python` extension
1. Short video to get the big picture about it: [Learn Visual Studio Code](https://youtu.be/B-s71n0dHUk?si=2oECTg6i5gEEQY8H)

## Git


1. Make a [GitHub](https://github.com/) acount
1. Download [Git](https://git-scm.com/)

---------------------------------


#### Git setup

* Run the installer
    * Choose `VS Code` as default editor  
    * Choose **`Override the default branch name for new repositories`** option  
    * Leave all other options **unchanged**  

* Open `Git Bash`
* Set your **username** and **email** with the following commands:  
    * `git config --global user.name "your username"`
    * `git config --global user.email "your_email@example.com"`
* Create `SSH key`
    * Generate the key: `ssh-keygen -t ed25519 -C "your_email@example.com"` (no passphrase needed, just press enter)
    * Start SSH Agent: ``` eval `ssh-agent` ```
    * Add key to SSH Agent: `ssh-add c:/Users/YOU/.ssh/id_ed25519` (**REPLACE "*YOU*" WITH YOUR USER FOLDER**)

---------------------------------

#### GitHub setup

* In Git Bash run the following: `clip < ~/.ssh/id_ed25519.pub` (this copies the key to the clipboard)
* Go to [GitHub](https://github.com/)
* In the upper-right corner of any page on GitHub, click your profile photo, then click `Settings`.
* In the `Access` section of the sidebar, click `SSH and GPG keys`.
* Click `New SSH key` or `Add SSH key`.
* In the `Title` field, add a descriptive label for the new key. For example, if you're using a personal laptop, you might call this key `Personal laptop`.
* In the `Key` field, paste your public key.
* Click `Add SSH key`.

---------------------------------


#### Cloning Repositories

* Go to the GitHub Repository you want to clone
* In the `<> Code` section, go to `<> Code`>`SSH` and copy the link
* In your user folder make a folder for the project (you can call it "Hackathon")
* Open it in a terminal and type: `git clone YOUR_URL` (paste the link replacing `YOUR_URL`)
* Now you can open it in VS Code

> This project has 2 Repos: book-app, indexing-app  

---------------------------------

> **RULES**

1. All tasks are done on the `development` branch
1. First thing `git pull`
1. Before `commit` and `push` another `git pull`

## Python

1. Follow [this](https://youtu.be/mNkH_NC8HME?si=VgDhwWPUDabKcDfi) tutorial
2. Open a .py file in VS Code and with `Ctrl + shift + P` open the Command Palette
3. Type `Python: Select Interpreter` and select the Python interpreter

#### Python venv