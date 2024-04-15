add_executable(app main.c)
target_include_directories(app PRIVATE include)

include(FetchContent)
FetchContent_Declare(
  ioutils
  GIT_REPOSITORY https://ioutils:aFiG6LqzyabnzhxzbhNC@git.vyuka.fai.utb.cz/ads/common/ioutils.git
)

FetchContent_MakeAvailable(ioutils)

target_link_libraries(app dijkstra ioutils)
