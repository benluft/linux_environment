import getpass
from module_installs.install_implementations import *
import time
from argparse import ArgumentParser

if __name__ == '__main__':

    installer_classes_dict = {'apt': APTInstaller(),
                              'apm': APMInstaller(),
                              'deb': DebInstaller(),
                              'snap': SnapInstaller(),
                              'run': RunInstaller()}

    parser = ArgumentParser()
    parser.add_argument("installer_type", type=str, help="What installer type would you like to use",
                        choices=installer_classes_dict.keys())
    parser.add_argument("package_name", type=str, help='Package name to add')

    args = parser.parse_args()

    installer_classes_dict[args.installer_type].add_new_package(args.package_name)

