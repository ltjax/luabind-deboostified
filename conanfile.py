from conans import ConanFile, CMake, tools


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
    generators = "cmake"
    exports_sources = "luabind/*", "src/*", "doc/*", "CMakeLists.txt",
    requires = "lua/5.1@ltjax/testing"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".",defs={
            'LUA_INCLUDE_DIR': ";".join(self.deps_cpp_info["lua"].include_paths),
            'LUA_LIBRARIES': ";".join(self.deps_cpp_info["lua"].libs),
            'LUABIND_BUILD_SHARED': self.options.shared,
        })
        cmake.build()

    def package(self):
        CMake(self).install()

    def package_info(self):
        self.cpp_info.libs = ["luabind"]

