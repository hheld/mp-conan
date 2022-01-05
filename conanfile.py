from conans import ConanFile, CMake, tools


class MpConan(ConanFile):
    name = "mp"
    version = "f7033500faa24432de38694361132de6770f50ad"
    license = "https://github.com/ampl/mp/blob/master/LICENSE.rst"
    author = "Harald Held <harald.held@gmail.com>"
    url = "https://github.com/hheld/mp-conan"
    description = "An open-source library for mathematical programming."
    topics = ("AMPL", "mathematical programming")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def _configure_cmake(self):
        cmake = CMake(self, generator="Ninja")
        cmake.definitions["BUILD"] = "asl"
        cmake.configure()
        return cmake

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/ampl/mp.git", f"{self.version}", shallow=True)
        git.run("submodule init thirdparty/asl")
        git.run("submodule update")

    def build(self):
        cmake = self._configure_cmake()
        tools.replace_path_in_file("src/asl/CMakeLists.txt", "${CMAKE_CURRENT_BINARY_DIR}/arith.h",
                                   "${CMAKE_CURRENT_BINARY_DIR}/asl/include/arith.h")
        tools.replace_path_in_file("src/asl/CMakeLists.txt", "solvers/opcode.hd", "")
        tools.replace_path_in_file("src/asl/CMakeLists.txt", "solvers/r_opn.hd", "")
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["aslmp", "mp"]
