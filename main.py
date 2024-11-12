import sys
import formated
from searcher import search
from os import chdir
import subprocess

def error():
    print('Error!')
    print('-a - ChadAI api\n-h - help\n-s - search\n' )
    print('wiki -s <Lorem>')
    print('wiki -a <API>')
    sys.exit(1)

try:
    command = subprocess.run(['whoami'], capture_output=True, text=True)
    name = command.stdout.strip()
    chdir(f'/home/{name}/wiki')

    if len(sys.argv) > 1 and sys.argv[1] == '-a':
        with open('api.txt', 'r+') as api_file:
            api_file.write(sys.argv[2])
            API = api_file.read()
    elif len(sys.argv) > 1 and sys.argv[1] == '-h':
        print('Using:')
        print('-a - ChadAI api\n-h - help\n-s - search\n' )
        print('wiki -s <Lorem>')
        print('wiki -a <API>')
    elif len(sys.argv) > 1 and sys.argv[1] == '-s':
        with open('api.txt', 'r') as api_file:
            API = api_file.read()
        input_value = sys.argv[1]
        output = search(input_value)
        print(formated.formater(output, API))
        sys.exit(0)
except:
    error()