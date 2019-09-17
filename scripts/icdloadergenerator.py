#! /usr/bin/env python3
"""
* Copyright (c) 2019, Intel Corporation
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included
* in all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
* THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
* OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
* ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
* OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import os.path as path
import re
from androidbpgenerator import INDENT, CCDefaults, ModuleInfo, Generator, NOVERBOSE

RUN_CALLABLE = True


class ICDLoaderGenerator(Generator):
    def __init__(self, root): 
        # It is necessary that patching on LLVM before generating Android.bp
        self.proj = path.join(root, "OpenCL-ICD-Loader/")
        super(ICDLoaderGenerator, self).__init__(self.proj, root)

        self.allmoduleinfo[0] = ModuleInfo("libOpenCL", "libOpenCL.bp", "CMakeFiles/OpenCL.dir/",
            "library_shared", "OpenCL-ICD-Loader-defaults")
        self.allmoduleinfo[1] = ModuleInfo("libIcdLog", "libIcdLog.bp", "test/log/CMakeFiles/IcdLog.dir/",
            "library_shared", "OpenCL-ICD-Loader-defaults")
        self.allmoduleinfo[2] = ModuleInfo("libOpenCLDriverStub", "libOpenCLDriverStub.bp",
            "test/driver_stub/CMakeFiles/OpenCLDriverStub.dir/", "library_shared", "OpenCL-ICD-Loader-defaults")
        self.allmoduleinfo[3] = ModuleInfo("icd_loader_test", "icd_loader_test.bp",
            "test/loader_test/CMakeFiles/icd_loader_test.dir/", "binary", "OpenCL-ICD-Loader-defaults")

        self.allmoduledefaults = CCDefaults(self.proj, "OpenCL-ICD-Loader-defaults",
            cflags = ["-Wno-error", "-Wno-error=implicit-function-declaration", "-DAMD64"],
            cppflags = ["-D__ANDROID__"],
            clang_cflags = ["-Wno-error=non-virtual-dtor"],
            include_dirs = ["hardware/intel/external/opencl/compute-runtime/third_party/opencl_headers"],
            bpfiles = ["libOpenCL.bp", "libIcdLog.bp", "libOpenCLDriverStub.bp", "icd_loader_test.bp"], )

    def getTemplate(self):
        return "icd-loader.tpl"

    def adjustSources(self, mode, all_sources):
        for i, l in enumerate(all_sources): 
            all_sources[i] = INDENT * 2 + "\"" + re.sub(r".*?: " + self.allmoduleinfo[mode].Mid_Dir, "",
                re.sub("CMakeFiles/.*?\\.dir/", "", l.replace("__/", "../")))


class Main:

    def run(self):
        script = path.dirname(__file__)
        root = path.abspath(path.join(script, "../.."))

        print("script = " + script)
        print("root = " + root)

        ICDLoaderGenerator(root).generate()


if RUN_CALLABLE:
    m = Main()
    m.run()