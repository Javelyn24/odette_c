cmake_minimum_required(VERSION 3.12)
project(ODETTE_satellite_core)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find Python and pybind11
find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(Eigen3 REQUIRED)

# Add pybind11 - support both system pybind11 or submodule
if(NOT TARGET pybind11::module)
    # Add as a subdirectory if available in the project
    if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/pybind11/CMakeLists.txt")
        add_subdirectory(pybind11)
    else()
        # Try to find a system pybind11
        find_package(pybind11 REQUIRED)
    endif()
endif()

# Set include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/cpp_core/include
    ${EIGEN3_INCLUDE_DIR}
)

# Collect all source files
set(CORE_SOURCES
    cpp_core/src/interpret.cpp
    cpp_core/src/orbmath.cpp
    cpp_core/src/propagator.cpp
    cpp_core/src/RADec.cpp
    cpp_core/src/SGP4.cpp
    cpp_core/src/TLE.cpp
    cpp_core/src/TDMParser.cpp
)

# Optional: Add any additional libraries your project needs
# find_package(LIBRARY_NAME REQUIRED)
# include_directories(${LIBRARY_NAME_INCLUDE_DIRS})

# Python module - combine core sources with the bindings
pybind11_add_module(satellite_core
    /Users/evelynschuller/Desktop/Facultate/Master/An\ 1,\ sem\ 2/OOP/Project/ODETTE/Python_interface/Bindings/satellite_core_bindings.cpp
    ${CORE_SOURCES}
)

# Optional: Link against additional libraries if needed
# target_link_libraries(satellite_core PRIVATE ${LIBRARY_NAME_LIBRARIES})

# Set proper install location
install(TARGETS satellite_core
        LIBRARY DESTINATION ${Python_SITEARCH}/odette)