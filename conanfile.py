from conans import ConanFile, CMake, tools


class MpConan(ConanFile):
    name = "mp"
    version = "bb7d616605dd23e4a453a834b0fc8c0a2a71b5aa"
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
        pass
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
