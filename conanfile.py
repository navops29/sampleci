from conans import ConanFile, CMake, tools


class MathlibConan(ConanFile):
    name = "mathlib"
    version = "0.0.1"
    description = "Simple math lib for calc options"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/navops29/demo-mathlib.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="mathlib")
        cmake.build()
        cmake.install()
        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    """def package(self):
        self.copy("*.h", dst="include", src="mathlib")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)"""

    def package_info(self):
        self.cpp_info.libs = ["mathlib"]

