cmake_minimum_required(VERSION 3.10)
project(dupeGuru VERSION 0.1.0 LANGUAGES C) # LANGUAGES C because of the .c files in core/pe/modules

# Find Python and its components
set(Python3_FIND_VIRTUALENV NEVER)
set(Python3_FIND_STRATEGY LOCATION)
set(Python3_ROOT_DIR "/usr")
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
message(STATUS "Python3 interpreter: ${Python3_EXECUTABLE}")
message(STATUS "Python3 libraries: ${Python3_LIBRARIES}")
message(STATUS "Python3 includes: ${Python3_INCLUDE_DIRS}")
message(STATUS "Python3_SITELIB: ${Python3_SITELIB}")

# Find PyQt5 for pyrcc5
find_package(Qt5 COMPONENTS Core Widgets REQUIRED)
find_package(Qt5Core REQUIRED) # For pyrcc5
find_program(PYRCC5_EXECUTABLE pyrcc5)
if (NOT PYRCC5_EXECUTABLE)
    message(FATAL_ERROR "pyrcc5 not found. Please ensure PyQt5 development tools are installed and in PATH.")
endif()
message(STATUS "pyrcc5 executable: ${PYRCC5_EXECUTABLE}")

# Define a target for building Python C extensions using setup.py
add_custom_target(
    build_python_extensions
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/setup.py build_ext --inplace
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Building Python C extensions using setup.py"
)

# Define a target for building Qt resources using pyrcc5
add_custom_target(
    build_qt_resources
    COMMAND ${PYRCC5_EXECUTABLE} ${CMAKE_SOURCE_DIR}/qt/dg.qrc -o ${CMAKE_SOURCE_DIR}/qt/dg_rc.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Building Qt resources using pyrcc5"
)

# Optional: Add a 'run' target for convenience
add_custom_target(
    run_dupeguru
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/run.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Running dupeGuru"
)

# Install commands
install(PROGRAMS run.py DESTINATION bin RENAME dupeguru)
install(DIRECTORY core DESTINATION ${Python3_SITELIB})
install(DIRECTORY hscommon DESTINATION ${Python3_SITELIB})
install(DIRECTORY qt DESTINATION ${Python3_SITELIB})
install(DIRECTORY images locale help DESTINATION share/${PROJECT_NAME})
install(FILES pkg/dupeguru.desktop DESTINATION share/applications)
