from colorama import Fore
import subprocess
import api
import google.generativeai as genai

# Functions

def runcmd(comm):
    subprocess.run(comm, shell=True, capture_output=False, text=True)

runcmd('clear')

def SearchGPT(query, orgId, projId):
    print("Under Development : Will be released in v2.0")

def SearchGem(query):
    genai.configure(api_key=api.API_GEMINI)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{query} and don't add single or double quotes to response")
    print(f"<RESPONSE > {response.text}")

    with open('db-local.txt', 'a+') as dbfile:
        dbfile.writelines("\n--------------------------------------")
        dbfile.writelines(f"\n\nQuery:- {query}")
        dbfile.writelines(f"\nResponse:- {response.text}")


def helpPrint():
    print(Fore.LIGHTGREEN_EX + '''
Usable Commands:

=> Regular Commands : Just type commands here and we'll run it for you if not a default PilotSearch v1.0 command!!
=> -h or -help : To open up this basic menu for any assistance

=> -sgem : Setup Gemini for your Device

=> -s : Search On ChatGPT (v2.0 only)
=> -t : Search On Gemini

=> -e : Exit
=> -git : Open GitHub Repository
''')
    
# Code

print(Fore.LIGHTCYAN_EX + '\nWelcome Users !!!\nThis is Pilot Search v1.0 by codec07\n\n')


while True:
    inp = input(Fore.LIGHTGREEN_EX + "\n? Search Pilot v1.0 ? ")

    if '-h' in inp or '-help' in inp:
        helpPrint()

    elif '-sgem' in inp:
        runcmd("pip3 install -q -U google-generativeai")

    elif '-t ' in inp:
        query = inp.replace('-t ', '')
        SearchGem(query)