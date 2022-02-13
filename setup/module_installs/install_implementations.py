from .install_interface import InstallInterface
import subprocess
import pathlib
import os


class APMInstaller(InstallInterface):

    @property
    def packager_name(self):
        return 'apm'

    def _package_specific_install(self, package_name):
        completed = subprocess.run(f'sudo -S apm install {package_name}'.split())
        return completed.returncode != 0


class APTInstaller(InstallInterface):

    @property
    def packager_name(self):
        return 'apt'

    def _package_specific_install(self, package_name):
        completed = subprocess.run(f'sudo -S apt-get install {package_name}'.split())
        return completed.returncode != 0


class DebInstaller(InstallInterface):

    @property
    def packager_name(self):
        return 'deb'

    def _package_specific_install(self, package_name):
        completed_get = subprocess.run(f'wget {package_name}'.split())
        deb_file_name = pathlib.Path(package_name).name
        completed_install = subprocess.run(f'sudo -S dpkg -i {deb_file_name}'.split())
        # Remove the file if it passed
        if completed_get.returncode == 0 and completed_install.returncode == 0:
            os.remove(deb_file_name)
        return completed_get.returncode != 0 or completed_install.returncode != 0


class RunInstaller(InstallInterface):

    @property
    def packager_name(self):
        return 'run'

    def _package_specific_install(self, package_name):
        completed_get = subprocess.run(f'wget {package_name}'.split())
        run_file_name = pathlib.Path(package_name).name
        completed_install = subprocess.run(f'sudo -S ./{run_file_name}'.split())
        # Remove the file if it passed
        if completed_get.returncode == 0 and completed_install.returncode == 0:
            os.remove(run_file_name)
        return completed_get.returncode != 0 or completed_install.returncode != 0


class SnapInstaller(InstallInterface):

    @property
    def packager_name(self):
        return 'snap'

    def _package_specific_install(self, package_name):
        completed_install = subprocess.run(f'sudo -S snap install {package_name}'.split())
        return completed_install.returncode != 0
