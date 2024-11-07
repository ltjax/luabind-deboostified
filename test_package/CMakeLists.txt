cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 11)

find_package(luabind-deboostified CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example luabind-deboostified::luabind-deboostified)

