// Copyright 2024-2024, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

export const description = "Test getter/setter #2";

class C {
    static get foo() {
        throw new Error("This getter function should not be evaluated while closure serialization.")
    }

    static set foo(v: number) {
        throw new Error("This setter function should not be evaluated while closure serialization.")
    }
}

export const func = () => C;