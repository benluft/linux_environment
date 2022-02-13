import os.path
from abc import ABC, abstractmethod
import pathlib


class InstallInterface(ABC):

    def __init__(self):
        self._file_dir = pathlib.Path(__file__).parent.absolute()

    @property
    @abstractmethod
    def packager_name(self):
        pass

    @property
    def package_storage_filenames(self):
        path = self._file_dir / f'{self.packager_name}_packages.txt'
        fun_path = self._file_dir / f'{self.packager_name}_packages_fun.txt'
        return path, fun_path

    def add_new_package(self, package_name, fun=False):
        filename = self.package_storage_filenames[1] if fun else self.package_storage_filenames[0]
        in_file = False
        # Make empty file if it doesn't exist
        if not os.path.exists(filename):
            open(filename, 'w').close()
        with open(filename) as f:
            for line in f:
                if line == package_name:
                    in_file = True
                    break
        failure = self._package_specific_install(package_name.strip())
        if not failure and not in_file:
            with open(filename, 'a') as f:
                f.write(package_name + '\n')
        elif failure:
            print(f"Package {package_name} failed install using {self.packager_name}")

    @abstractmethod
    def _package_specific_install(self, package_name):
        pass

    def install_all_packages(self, fun=False):
        filenames = self.package_storage_filenames if fun else [self.package_storage_filenames[0]]
        report_dict = {}
        for filename in filenames:
            if not filename.exists():
                continue
            with open(filename) as f:
                for line in f:
                    line = line.strip()
                    if line == '':
                        continue
                    failure = self._package_specific_install(line.strip())
                    report_dict[line.strip()] = "Failed" if failure else "Passed"
            results_string = self.results_string(report_dict)
            print(results_string)

    def results_string(self, results_dict):
        string_list = []
        print(f"\n\nInstall results for {self.packager_name}")
        max_package_length = max([len(key) for key in results_dict.keys()])
        format_string = "{:<" + str(max_package_length+3) + "} {:<6}"
        for package, result in results_dict.items():
            string_list.append(format_string.format(package, result))
        return '\n'.join(string_list)
