import os
from conans import ConanFile

class ScdocConan(ConanFile):
    name = "scdoc"
    version = "1.11.1"
    settings = "os", "arch"
    exports_sources = "source/*"

    def build(self):
        self.run(f"make PREFIX={self.package_folder}", cwd="source")

    def package(self):
        self.run(f"make PREFIX={self.package_folder} install" , cwd="source")

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))