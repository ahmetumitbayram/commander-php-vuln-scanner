import os
import re

# Banner
banner = """
  ____                                          _                   _   ___  
 / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| | ___ _ __  __   _/ | / _ \ 
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |/ _ \ '__| \ \ / / || | | |
| |__| (_) | | | | | | | | | | | (_| | | | | (_| |  __/ |     \ V /| || |_| |
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|\___|_|      \_/ |_(_)___/ 

          Coded by: Ahmet Ümit BAYRAM
"""

print(banner)
user_directory = input("Lütfen dizin yolunu girin: ")

dangerous_functions = [
    'shell_exec', 'eval', 'exec',
    'system', 'passthru', 'popen',
    'proc_open', 'pcntl_exec', 'assert',
    'preg_replace', 'create_function',
    'include', 'include_once', 'require',
    'require_once', 'file_put_contents',
    'fwrite', 'fputs', 'mkdir', 'rmdir',
    'unlink', 'rename', 'copy', 'move_uploaded_file'
]

user_input_sources = ['$_GET', '$_POST', '$_REQUEST', '$_COOKIE', '$_FILES', '$_SERVER']
user_inputs = {}

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.php'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.readlines()
                        for idx, line in enumerate(content):
                            # If the line has user input source, mark the variable as tainted
                            for source in user_input_sources:
                                if source in line:
                                    variable = re.findall('\$[a-zA-Z_][a-zA-Z0-9_]*', line)
                                    if variable:
                                        for var in variable:
                                            user_inputs[var] = True
                            # If the line has a dangerous function, check if the variable is tainted
                            for function in dangerous_functions:
                                pattern = r'\b{}\b\s*\('.format(function)
                                match = re.search(pattern, line)
                                if match:
                                    variable = re.findall('\$[a-zA-Z_][a-zA-Z0-9_]*', line)
                                    if variable:
                                        for var in variable:
                                            if var in user_inputs and user_inputs[var]:
                                                print(f"| {file_path} | {function} | {idx+1} | {var} | VULNERABLE |")
                                                # After using the variable in a dangerous function, mark it as untainted
                                                user_inputs[var] = False
                except UnicodeDecodeError:
                    pass

if os.path.isdir(user_directory):
    scan_directory(user_directory)
else:
    print("Geçersiz dizin yolunu girdiniz.")
