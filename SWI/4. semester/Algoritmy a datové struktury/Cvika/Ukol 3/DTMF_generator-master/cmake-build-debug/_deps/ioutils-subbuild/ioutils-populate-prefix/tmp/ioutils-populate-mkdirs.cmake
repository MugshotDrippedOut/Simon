# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-src"
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-build"
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix"
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix/tmp"
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix/src/ioutils-populate-stamp"
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix/src"
  "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix/src/ioutils-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix/src/ioutils-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/bucka/Documents/GitHub/Simon/SWI/4. semester/Algoritmy a datové struktury/Cvika/Ukol 3/DTMF_generator-master/cmake-build-debug/_deps/ioutils-subbuild/ioutils-populate-prefix/src/ioutils-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
