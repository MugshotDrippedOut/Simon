cmake_minimum_required(VERSION 3.16)
project(templates LANGUAGES CXX)

add_executable(my_main main.cpp)

add_subdirectory(lib)

target_link_libraries(my_main point)