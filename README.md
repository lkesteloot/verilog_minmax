# Verilog min/max generator

This tool generates Verilog code to compute the min or max of a set of
registers or constants. Specify the operator and all the operands on the
command line.

# Examples

    % python minmax.py "<" "1'b0" vertex_0_x vertex_1_x vertex_2_x
    result <= 1'b0 < vertex_0_x
        ? 1'b0 < vertex_1_x
            ? 1'b0 < vertex_2_x
                ? 1'b0
                : vertex_2_x
            : vertex_1_x < vertex_2_x
                ? vertex_1_x
                : vertex_2_x
        : vertex_0_x < vertex_1_x
            ? vertex_0_x < vertex_2_x
                ? vertex_0_x
                : vertex_2_x
            : vertex_1_x < vertex_2_x
                ? vertex_1_x
                : vertex_2_x;

    % python minmax.py ">" "WIDTH - 1" vertex_0_x vertex_1_x vertex_2_x
    result <= WIDTH - 1 > vertex_0_x
        ? WIDTH - 1 > vertex_1_x
            ? WIDTH - 1 > vertex_2_x
                ? WIDTH - 1
                : vertex_2_x
            : vertex_1_x > vertex_2_x
                ? vertex_1_x
                : vertex_2_x
        : vertex_0_x > vertex_1_x
            ? vertex_0_x > vertex_2_x
                ? vertex_0_x
                : vertex_2_x
            : vertex_1_x > vertex_2_x
                ? vertex_1_x
                : vertex_2_x;

# License 

Copyright 2017 Lawrence Kesteloot

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

