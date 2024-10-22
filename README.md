# PilotSearch v1.0 - by Codec07

About: PilotSearch is a very simple but very usefull tool that can be used by regular or cybersecurity personals allowing you to use Gemini AI inside your terminal that can be used as a normal terminal as well !!

## Note: This Project Uses Python3 and pip3, kindly install the same before use


## Steps to Use:

### 1. Installation
Go to your terminal and type: 
1. pip3 install colorama
2. pip3 install -q -U google-generativeai
3. git clone {repo_name}
And Done Your are all set

### 2. Setting Up API and Gemini
TO be able to use gemini, you must first add your api key inside the api.py file simply using nano (bash based) or any text editor.
Next, type -sgem to allow the program to settup gemini installation
And done...

### 3. Executing the file
Type python3 main.py or python main.py to run and you are into the terminal !!!

## Commands:

Usable Commands:

=> Regular Commands : Just type commands here and we'll run it for you if not a default PilotSearch v1.0 command!!

=> -h or -help : To open up this basic menu for any assistance

=> -sgem : Setup Gemini for your Device

=> -s : Search On ChatGPT (v2.0 only)

=> -t : Search On Gemini

=> -e : Exit

=> -git : Open github repository

## Example - For Linux/Bash Based

terminal>>> pip3 install colorama

terminal>>> pip3 install -q -U google-generativeai

terminal>>> git clone https://github.com/codec07/pilotsearch_v1

terminal>>> cd pilotsearch_v1

terminal>>> nano api.py

*NANO EDITOR WOULD OPEN, EDIT THE FOLLOWING*

API_GEMINI="YOUR API KEY HERE"

*press ctrl+s and ctrl+x To save and close*

terminal>>> python3 main.py

*APPLICATION WOULD START*

*TO USE GEMINI, TYPE*

? Pilot Search v1.0 ? -t "YOUR QUERY HERE"

## Accessing Data Generated

The data generated during the searches will be displayed and also would get stored in a file called db-local.txt in the root directory, to access it just open the root directory and open the file either by nano or any other text editor.

## Glimpse - Version 2.0

The version 2.0 is currently under development and Will introduce advanced capabilities and chatgpt integration with multiple storage and editing modes making it even more accessible. Features like chatgpt integration and wikipedia Module would be introduced. The UI and specific menu based Features would allow users to interact More easily with the tool.
