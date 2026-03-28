cmake_minimum_required(VERSION 3.16)
project(dupeguru LANGUAGES C)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

# === C EXTENSIONS (this was the missing piece) ===

# Core PE: _block
add_library(_block MODULE core/pe/modules/block.c core/pe/modules/common.c)
target_include_directories(_block PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(_block PRIVATE ${Python3_LIBRARIES})
set_target_properties(_block PROPERTIES PREFIX "" SUFFIX "${Python3_EXT_SUFFIX}")

# Core PE: _cache
add_library(_cache MODULE core/pe/modules/cache.c core/pe/modules/common.c)
target_include_directories(_cache PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(_cache PRIVATE ${Python3_LIBRARIES})
set_target_properties(_cache PROPERTIES PREFIX "" SUFFIX "${Python3_EXT_SUFFIX}")

# Qt PE: _block_qt (only block.c exists in qt/pe/modules/)
add_library(_block_qt MODULE qt/pe/modules/block.c)
target_include_directories(_block_qt PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(_block_qt PRIVATE ${Python3_LIBRARIES})
set_target_properties(_block_qt PROPERTIES PREFIX "" SUFFIX "${Python3_EXT_SUFFIX}")

# === INSTALL PYTHON PACKAGES + COMPILED EXTENSIONS ===

install(DIRECTORY core/ DESTINATION ${Python3_SITELIB}/core
        FILES_MATCHING PATTERN "*.py" PATTERN "*.pyi" PATTERN "__pycache__" EXCLUDE)
install(TARGETS _block _cache LIBRARY DESTINATION ${Python3_SITELIB}/core/pe)

install(DIRECTORY qt/ DESTINATION ${Python3_SITELIB}/qt
        FILES_MATCHING PATTERN "*.py" PATTERN "*.pyi" PATTERN "__pycache__" EXCLUDE)
install(TARGETS _block_qt LIBRARY DESTINATION ${Python3_SITELIB}/qt/pe)

# === RESOURCE INSTALLS (matching your actual repo layout) ===

install(PROGRAMS run.py DESTINATION bin RENAME dupeguru)

install(DIRECTORY images/ DESTINATION share/dupeguru/images)

install(DIRECTORY locale/ DESTINATION share/dupeguru/locale
        FILES_MATCHING PATTERN "*.mo")

install(DIRECTORY help/ DESTINATION share/dupeguru/help)

# Desktop file — adjust path if your desktop file is in pkg/ instead of root
install(FILES pkg/dupeguru.desktop DESTINATION share/applications RENAME dupeguru.desktop)
