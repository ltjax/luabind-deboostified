#include <iostream>
#include <lua.hpp>
#include <luabind/luabind.hpp>

void HelloWorld()
{
  std::cout << "Hello world!" << std::endl;
}

int main(int argc, char** argv)
{
  auto L = lua_open();
  
  luabind::module(L)
  [
    luabind::def("HelloWorld", &HelloWorld)
  ];
  
  lua_close(L);
  return 0;
}

