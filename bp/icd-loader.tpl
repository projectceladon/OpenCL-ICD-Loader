# Copyright(c) 2019 Intel Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files(the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and / or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# The file-tree of OpenCL-ICD-Loader
# OpenCL-ICD-Loader (cmake -DCMAKE_BUILD_TYPE=Release OpenCL-ICD-Loader) 
# |
# +---- libOpenCL.so.1.2 -> Tools/Android/build/icd-loader/CMakeFiles/OpenCL.dir 
#       |
#       +---- test 
#             |
#             +---- log 
#             |     |
#             |     +---- libIcdLog.so -> Tools/Android/build/icd-loader/test/platform/CMakeFiles/IcdLog.dir 
#             |
#             +---- loader_test 
#             |     |
#             |     +---- icd_loader_test -> Tools/Android/build/icd-loader/test/loader_test/CMakeFiles/icd_loader_test.dir 
#             |           |
#             |           => libOpenCL.so.1.2, libIcdLog.so
#             |
#             +---- driver_stub
#                   |
#                   +---- libOpenCLDriverStub.so -> Tools/Android/build/icd-loader/test/driver_stub/CMakeFiles/OpenCLDriverStub.dir 
#                         |
#                         => libIcdLog.so
# 
# About the detailed of soong-build-tools(cc package), please refer to: 
#     https://ci.android.com/builds/submitted/5357401/linux/latest/view/soong_build.html 
# 
# 
# library_static, library_shared, binary 
cc_@module {
    name: "@name",

    vendor_available: true,

    defaults: [
@defaults
    ],

    srcs: [
@srcs
    ],

    cflags: [
@cflags
    ],

    cppflags: [
@cppflags
    ],

    local_include_dirs: [
@local_include_dirs
    ],

    shared_libs: [
@shared_libs
    ],

    static_libs: [
@static_libs
    ],

}