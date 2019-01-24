"""
Copyright 2017 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# pylint: disable=invalid-name,relative-import
from example_bench_plugin import BenchPlugin
from example_multi_plugin import ExamplePlugin
from example_allocator import ExampleAllocatorPlugin

plugins_to_load = {"BenchPlugin": BenchPlugin, "ExamplePlugin": ExamplePlugin,
                   "ExampleAllocator": ExampleAllocatorPlugin}
