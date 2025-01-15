# Minimum CMake version required
cmake_minimum_required(VERSION 3.31)

# Define the project name
project(MyProject)

# Define the source files
add_executable(${PROJECT_NAME} libraries/list/classes/list/list.cpp)

# Set the C++ standard to C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
