cmake_minimum_required(VERSION 3.14)
project(cviko LANGUAGES CXX)

add_subdirectory(lib)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(my_main main.cpp)

target_link_libraries(my_main vector point)

add_subdirectory(test)