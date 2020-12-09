cmake_minimum_required(VERSION 3.0) 
project(Mathlib)

 add_definitions("-std=c++11")

 include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
 conan_basic_setup()

 add_library(mathlib src/mathlib.cpp)
 
 target_include_directories(mathlib
  PUBLIC
  $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
 
 target_link_libraries(mathlib ${CONAN_LIBS})
 
 install(TARGETS mathlib
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY include DESTINATION .)
