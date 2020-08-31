# Build for LuaBind
# Ryan Pavlik <rpavlik@iastate.edu>
# http://academic.cleardefinition.com/
# Iowa State University HCI Graduate Program/VRAC

cmake_minimum_required(VERSION 3.8)
project(LuaBind)

set(CMAKE_CXX_STANDARD 17)

set(CPACK_PACKAGE_VERSION_MAJOR "0")
set(CPACK_PACKAGE_VERSION_MINOR "9")
set(CPACK_PACKAGE_VERSION_PATCH "1")
set(CPACK_PACKAGE_VERSION
  "${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH}")
  
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
  # We are the top-level project
  option(LUABIND_INSTALL "Install the LuaBind library and headers" ON)
  option(LUABIND_BUILD_SHARED "Build luabind as a shared library?" OFF)
  include(CTest)
endif()

if(CMAKE_COMPILER_IS_GNUCXX)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()


set(BUILD_SHARED_LIBS ${LUABIND_BUILD_SHARED})
if(BUILD_SHARED_LIBS)
  add_definitions(-DLUABIND_DYNAMIC_LINK)
endif()

include_directories(
  "${CMAKE_CURRENT_SOURCE_DIR}"
  ${LUA_INCLUDE_DIRS})

add_subdirectory(src)

if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
  if(LUABIND_BUILD_TESTING)
    add_subdirectory(test)
  endif()
  add_subdirectory(doc)
endif()
