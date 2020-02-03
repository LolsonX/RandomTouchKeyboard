# Random Touch Keyboard

## Installation

### Install **Python3** and **pip**
   ```bash
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.7
    sudo apt-get install python3-pip
   ```

### Create Virtual Env
Install VirtualEnv:
   ```bash
    sudo pip3 install virtualenv 
   ```
Change working directory to project directory:
   ```bash
    cd /path/to/project
   ```

Create virualenv
   ```bash
    python3 -m venv myenv
   ```

Activate venv:
   ```bash
    source venv/bin/activate
   ```
### Install libraries

   ```bash
   (venv) pip install -r requirements.txt
   ```

## Run app

   ```bash
    python main.py
   ```

To change max time and keyboard reshuffle time change values of vars in main.py (MAX_TIME and CHANGE_TIME)
