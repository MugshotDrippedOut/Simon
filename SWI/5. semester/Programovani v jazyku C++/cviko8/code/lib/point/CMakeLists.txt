add_library(point point.cpp)

target_include_directories(point PUBLIC
    header
    template
)

target_link_libraries(point vector)