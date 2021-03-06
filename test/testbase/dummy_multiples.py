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

from icetea_lib.bench import Bench


class TestcaseBase(Bench):

    def __init__(self, test_name):
        Bench.__init__(self,
                       name=test_name,
                       title = "dummy",
                       status="unknown",
                       type="functional",
                       purpose = "dummy",
                       requirements={
                           "duts": {
                               '*': {
                                    "count": 0,
                                }
                           }}
        )

    def case(self):
        pass


class FirstTest(TestcaseBase):
    IS_TEST = True

    def __init__(self):
        TestcaseBase.__init__(self, "first_dummy_test")


class SecondTest(TestcaseBase):
    IS_TEST = True

    def __init__(self):
        TestcaseBase.__init__(self, "second_dummy_test")
