import os
import base64
from sys import argv

# configuration
OFFSET = 10
VARIABLE_NAME = '_TEST' * 100 #Add custom text to make it harder for auto decode programmes

def obfuscate(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))' #Actualy Encode bytes
    return code

def main():
    print('#############################')
    print('#        RobinHood          #')
    print('#                           #')
    print('#       gg/RbdAh4ap         #')
    print('#    Made by !" 𝖜𝖔𝖇𝖟𝖆#0001  #')
    print('#############################')

    try:
        path = argv[1]
        if not os.path.exists(path):
            print('[-] File not found')
            exit()

        if not os.path.isfile(path) or not path.endswith('.py'): #If it's not a python file it will throw an error
            print('[-] Invalid file extension')
            exit()
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        obfuscated_content = obfuscate(file_content)

        with open(f'{path.split(".")[0]} robinhood.py', 'w') as file: #Make output file 
            file.write(obfuscated_content)

        print('[+] Script has been obfuscated') #Success
    except:
        print(f'To run do: py {argv[0]} <file>')

if __name__ == '__main__':
    main()