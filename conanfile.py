from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class LuabindDeboostifiedConan(ConanFile):
    name = "luabind-deboostified"
    version = "1.0"
    license = "ZLIB"
    author = "Marius Elvert marius.elvert@googlemail.com"
    url = "https://github.com/ltjax/luabind-deboostified"
    description = "Create Lua bindings for your C++ code easily"
    topics = ("lua", "bindings")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "luabind/*", "src/*", "doc/*", "CMakeLists.txt",

    def requirements(self):
        self.requires("lua/5.1", transitive_headers=True)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        toolchain = CMakeToolchain(self)
        toolchain.variables['LUABIND_BUILD_SHARED'] = self.options.shared
        toolchain.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self)

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["luabind"]

