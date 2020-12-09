from conans import ConanFile, CMake, tools


class MathlibConan(ConanFile):
    name = "mathlib"
    version = "0.0.1"
    description = "Simple math lib for calc options"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/navops29/demo-mathlib.git mathlib")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="mathlib")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["mathlib"]

