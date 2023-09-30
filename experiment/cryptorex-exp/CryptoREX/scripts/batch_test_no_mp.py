import os
import pathlib

if __name__ == '__main__':
    input_dir = './input'
    log_dir = './tmp/log'
    os.system(f'rm -rf {log_dir} & mkdir {log_dir}')
    for dir_path, _, files in os.walk(input_dir):
        relative_path = dir_path.replace(input_dir, '')
        if relative_path.endswith('__'):
            continue
        for file in files:
            input = f'{relative_path}/{file}'
            pathlib.Path(os.path.dirname(f'{log_dir}/{input}.log')).mkdir(parents=True, exist_ok=True)
            os.system(f'python ./CryptoREX_rebuilt/rex/bin2vex.py "{input}" > "{log_dir}/{input}.log" 2>&1')