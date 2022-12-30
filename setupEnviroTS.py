import os
import time

path = input('Where would you like the project to be created?\n')
name = input('What would you like the project to be called?\n')

cdToPath = f'cd {path} &&'
os.system(f'{cdToPath} mkdir {name}')
dir = f'cd {path}/{name} &&'
os.system(f'{dir} npm init -y && {dir} npm i typescript --save-dev && {dir} npm i @types/node && {dir} npx tsc && {dir} npx tsc --init')

with open(f'defaultTSCONFIG.txt', 'r') as firstfile, open(f'{path}/{name}/tsconfig.json', 'a') as secondfile:
    for line in firstfile:
      secondfile.write(line)
  
os.system(f'{dir} touch test.ts')
with open(f'{path}/{name}/test.ts', 'w+') as g:
    g.write('console.log(\'<<<<ENVIRONMENT SETUP SUCCESSFUL>>>>\')')
os.system('clear')
os.system(f'{dir} npx tsc test.ts && node test.js')
os.system(f'{dir} rm -rf test.ts && rm -rf test.js')






