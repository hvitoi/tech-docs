# Minimum CMake version required
cmake_minimum_required(VERSION 3.31)

# Define the project name
project(MyProject)

# Set the C++ standard to C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Define the source files
add_executable(${PROJECT_NAME} libraries/list/classes/list/list.cpp)

# Define libraries
# add_library(mylib lib.cpp)
# add_library(mylib STATIC lib.cpp) # default option when not specified
# add_library(mylib SHARED lib.cpp)

# Link librarie to the main project
target_link_libraries(${PROJECT_NAME} mylib)
