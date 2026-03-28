cmake_minimum_required(VERSION 3.16)
project(dupeguru LANGUAGES C)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

# Core PE extension (_block and _cache)
add_library(_block MODULE core/pe/modules/block.c core/pe/modules/common.c)
target_include_directories(_block PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(_block PRIVATE ${Python3_LIBRARIES})
set_target_properties(_block PROPERTIES PREFIX "" SUFFIX "${Python3_EXT_SUFFIX}")

add_library(_cache MODULE core/pe/modules/cache.c core/pe/modules/common.c)
target_include_directories(_cache PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(_cache PRIVATE ${Python3_LIBRARIES})
set_target_properties(_cache PROPERTIES PREFIX "" SUFFIX "${Python3_EXT_SUFFIX}")

# Qt PE extension (_block_qt)
add_library(_block_qt MODULE qt/pe/modules/block.c qt/pe/modules/common.c)
target_include_directories(_block_qt PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(_block_qt PRIVATE ${Python3_LIBRARIES})
set_target_properties(_block_qt PROPERTIES PREFIX "" SUFFIX "${Python3_EXT_SUFFIX}")

# Install Python packages + compiled extensions
install(DIRECTORY core/ DESTINATION ${Python3_SITELIB}/core
        FILES_MATCHING PATTERN "*.py" PATTERN "*.pyi" PATTERN "__pycache__" EXCLUDE)
install(TARGETS _block _cache LIBRARY DESTINATION ${Python3_SITELIB}/core/pe)

install(DIRECTORY qt/ DESTINATION ${Python3_SITELIB}/qt
        FILES_MATCHING PATTERN "*.py" PATTERN "*.pyi" PATTERN "__pycache__" EXCLUDE)
install(TARGETS _block_qt LIBRARY DESTINATION ${Python3_SITELIB}/qt/pe)

# Install binary, desktop file, resources, etc. (keep your existing install rules here)
install(PROGRAMS run.py DESTINATION bin RENAME dupeguru)
# ... rest of your original install rules for share/, locale/, images/, etc.
