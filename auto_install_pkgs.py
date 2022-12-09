import subprocess
import colorama
from colorama import *
debpkgs='qalc fonts-powerline ninja-build gettext libtool libtool-bin autoconf automake cmake g++ pkg-config unzip curl doxygen python3-pip'

def debpkg_install():
    if userinput == 'y':
        for i in range(len(debpkgs)):
            subprocess.call(['sudo','apt','install',  f'{debpkgs[i]}'])
    if userinput!='y':
        print('exiting...')
        pass;

dist_pkgs='debpkgs'
colored_debpkg=(f'{colorama.Fore.LIGHTYELLOW_EX}{debpkgs}{colorama.Style.RESET_ALL}')
debpkgs=debpkgs.split(' ')
userinput=input(f'Enter pkgs you want to install here: {dist_pkgs}... ')
faa=userinput.split(' ')
userinput_list=[]
for a in range(len(faa)):
    print(f'looking for packages in set...{faa[a]}')
    userinput_list.append(faa[a])
# print(faa)
for b in range(len(userinput_list)):

    if userinput_list[b] not in dist_pkgs:
        print(f'{colorama.Fore.LIGHTRED_EX}{userinput_list[b]}{colorama.Style.RESET_ALL} not in dist_pkgs...')

    if userinput_list[b] in dist_pkgs:
        userinput=input(f'Do you wish to install deb pkgs y/n? ({colored_debpkg}): ')
        debpkg_install()

# print(userinput_list)
