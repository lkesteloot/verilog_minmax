#!/usr/bin/python

#    Copyright 2017 Lawrence Kesteloot
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# Generates Verilog code to compute the min or max of a set of registers or
# constants. Specify the operator and all the operands on the command line.
#
# Example:
#
#     python minmax.py "<" "1'b0" vertex_0_x vertex_1_x vertex_2_x
#     python minmax.py ">" "WIDTH - 1" vertex_0_x vertex_1_x vertex_2_x
#

import sys

INDENT = "    "

# Generate the sub-tree with the given indent, operator, and operands.
def generate(indent, operator, operands):
    if len(operands) == 0:
        raise Exception("Should never have zero operands")

    if len(operands) == 1:
        return operands[0]

    return "%s %s %s\n%s? %s\n%s: %s" % (operands[0], operator, operands[1],
            indent,
            generate(indent + INDENT, operator, [operands[0]] + operands[2:]),
            indent,
            generate(indent + INDENT, operator, [operands[1]] + operands[2:]))

def main(args):
    if len(args) < 2:
        print "Usage: minmax.py operator a b c . . ."
        sys.exit(1)

    print "result <= " + generate(INDENT, args[0], args[1:]) + ";"

main(sys.argv[1:])
