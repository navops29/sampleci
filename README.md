# Demo Mathlib
## Overview
* This is a very simple lib that performs basic math operations (`+`,`-`,`/`,`*`) on integers.
* It is used by https://github.com/navops29/demo-calculator app

## Building
* Build requires `conan` to be installed.
* Download/clone the `conanfile.py` from this repo.
* Run ` conan create .` command where `.` is the directory where `conanfile.py` is present.
* Full output of building `mathlib` dependency:
``` 
(venv) snc@desk01:~/demo/mathlib$ conan create .
WARN: Remotes registry file missing, creating default one in /home/snc/.conan/remotes.json
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'license'. It is recommended to add it as attribute
Exporting package recipe
mathlib/0.0.1: A new conanfile.py version was exported
mathlib/0.0.1: Folder: /home/snc/.conan/data/mathlib/0.0.1/_/_/export
mathlib/0.0.1: Exported revision: 2fbe22cd985a4872a37bba7c882b8407
Configuration:
[settings]
arch=x86_64
arch_build=x86_64
build_type=Release
compiler=gcc
compiler.libcxx=libstdc++11
compiler.version=9
os=Linux
os_build=Linux
[options]
[build_requires]
[env]

mathlib/0.0.1: Forced build from source
Installing package: mathlib/0.0.1
Requirements
    mathlib/0.0.1 from local cache - Cache
Packages
    mathlib/0.0.1:abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082 - Build

Installing (downloading, building) binaries...
mathlib/0.0.1: Configuring sources in /home/snc/.conan/data/mathlib/0.0.1/_/_/source
Cloning into 'mathlib'...
remote: Enumerating objects: 26, done.
remote: Counting objects: 100% (26/26), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 26 (delta 11), reused 22 (delta 7), pack-reused 0
Unpacking objects: 100% (26/26), 2.88 KiB | 268.00 KiB/s, done.
mathlib/0.0.1: Copying sources to build folder
mathlib/0.0.1: Building your package in /home/snc/.conan/data/mathlib/0.0.1/_/_/build/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082
mathlib/0.0.1: Generator cmake created conanbuildinfo.cmake
mathlib/0.0.1: Calling build()
-- The C compiler identification is GNU 9.3.0
-- The CXX compiler identification is GNU 9.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Conan: called by CMake conan helper
-- Conan: called inside local cache
-- Conan: Adjusting output directories
-- Conan: Using cmake global configuration
-- Conan: Adjusting default RPATHs Conan policies
-- Conan: Adjusting language standard
-- Conan: Compiler GCC>=5, checking major version 9
-- Conan: Checking correct version: 9
-- Conan: C++ stdlib: libstdc++11
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_EXPORT_NO_PACKAGE_REGISTRY
    CMAKE_INSTALL_BINDIR
    CMAKE_INSTALL_DATAROOTDIR
    CMAKE_INSTALL_INCLUDEDIR
    CMAKE_INSTALL_LIBDIR
    CMAKE_INSTALL_LIBEXECDIR
    CMAKE_INSTALL_OLDINCLUDEDIR
    CMAKE_INSTALL_SBINDIR


-- Build files have been written to: /home/snc/.conan/data/mathlib/0.0.1/_/_/build/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082
Scanning dependencies of target mathlib
[ 50%] Building CXX object CMakeFiles/mathlib.dir/src/mathlib.cpp.o
[100%] Linking CXX static library lib/libmathlib.a
[100%] Built target mathlib
[100%] Built target mathlib
Install the project...
-- Install configuration: "Release"
-- Installing: /home/snc/.conan/data/mathlib/0.0.1/_/_/package/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082/lib/libmathlib.a
-- Installing: /home/snc/.conan/data/mathlib/0.0.1/_/_/package/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082/./include
-- Installing: /home/snc/.conan/data/mathlib/0.0.1/_/_/package/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082/./include/mathlib
-- Installing: /home/snc/.conan/data/mathlib/0.0.1/_/_/package/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082/./include/mathlib/mathlib.hpp
mathlib/0.0.1: Package 'abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082' built
mathlib/0.0.1: Build folder /home/snc/.conan/data/mathlib/0.0.1/_/_/build/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082
mathlib/0.0.1: Generated conaninfo.txt
mathlib/0.0.1: Generated conanbuildinfo.txt
mathlib/0.0.1: Generating the package
mathlib/0.0.1: Package folder /home/snc/.conan/data/mathlib/0.0.1/_/_/package/abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082
mathlib/0.0.1: Calling package()
mathlib/0.0.1: WARN: This conanfile has no package step
mathlib/0.0.1 package(): Packaged 1 '.hpp' file: mathlib.hpp
mathlib/0.0.1 package(): Packaged 1 '.a' file: libmathlib.a
mathlib/0.0.1: Package 'abd3ca9581f5ec3d6672fa2ee8818b1f09dbb082' created
mathlib/0.0.1: Created package revision 5f581dcf3ed2dc5f4c41b6818faded1d
```


* Now, we can build the calculator app or any other app which uses above compiled mathlib.
* `conan` will ensure that the cached build is used, and we do not spend unnecessary time rebuilding the mathlib.
* For a more practical usage, we can package the `mathlib` lib using Conan and upload it to a repository (eg: JFrog) and reference that in projects that depend on it.


## References
* https://docs.conan.io/en/latest/introduction.html
