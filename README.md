# Uncommon Python Bug: Infinite Recursion in Factorial Function

This repository demonstrates a common yet often overlooked bug in recursive functions: infinite recursion.  The `factorial` function, while correctly calculating factorials for non-negative integers, fails catastrophically when given a negative input. This leads to a `RecursionError` due to exceeding the maximum recursion depth.

The solution demonstrates how to handle this edge case gracefully by explicitly checking for negative inputs and raising a `ValueError`.