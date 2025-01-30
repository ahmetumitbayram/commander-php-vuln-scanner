import os
import re
import json
import logging
from concurrent.futures import ThreadPoolExecutor
import argparse

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


# Log ayarları
logging.basicConfig(filename="scanner.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

dangerous_functions = [
    'shell_exec', 'eval', 'exec', 'system', 'passthru', 'popen', 'proc_open',
    'pcntl_exec', 'assert', 'preg_replace', 'create_function',
    'include', 'include_once', 'require', 'require_once',
    'file_put_contents', 'fwrite', 'mkdir', 'unlink', 'copy'
]

user_input_sources = ['$_GET', '$_POST', '$_REQUEST', '$_COOKIE', '$_FILES', '$_SERVER']
results = []

def analyze_file(file_path):
    user_inputs = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
            for idx, line in enumerate(content):
                for source in user_input_sources:
                    if source in line:
                        variables = re.findall(r'\$\w+', line)
                        for var in variables:
                            user_inputs[var] = True
                
                for function in dangerous_functions:
                    if re.search(r'\b{}\b\s*\('.format(function), line):
                        variables = re.findall(r'\$\w+', line)
                        for var in variables:
                            if var in user_inputs and user_inputs[var]:
                                results.append({
                                    "file": file_path,
                                    "function": function,
                                    "line": idx+1,
                                    "variable": var,
                                    "status": "VULNERABLE"
                                })
    except Exception as e:
        logging.error(f"Hata oluştu: {file_path} - {str(e)}")

def scan_directory(directory):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.php'):
                    file_path = os.path.join(root, file)
                    executor.submit(analyze_file, file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PHP Güvenlik Tarayıcısı")
    parser.add_argument("directory", help="Taranacak dizinin yolu")
    parser.add_argument("--output", "-o", help="Sonucu JSON olarak kaydet")
    args = parser.parse_args()

    scan_directory(args.directory)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
