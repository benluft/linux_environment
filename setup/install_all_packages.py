import getpass
from module_installs.install_implementations import *
import time

if __name__ == '__main__':

    invalid_input = True
    fun_packages = False
    while invalid_input:
        print("Do you want to install 'fun' packages? [y/n]")
        user_response = input().lower().strip()
        invalid_input = False
        if user_response == 'y':
            fun_packages = True
        elif user_response == 'n':
            fun_packages = False
        else:
            print("Please enter a valid response")
            invalid_input = True

    installer_classes_dict = {'apt': APTInstaller(),
                              'apm': APMInstaller(),
                              'deb': DebInstaller(),
                              'snap': SnapInstaller(),
                              'run': RunInstaller()}

    for installer_type, installer_class in installer_classes_dict.items():
        installer_class.install_all_packages(fun=fun_packages)
        time.sleep(3)
