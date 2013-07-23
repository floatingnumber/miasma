miasma techical design document
-------------------------------
Description: Miasma is a binary manipulation program designed to provide on-the-fly patching and function hooking (shared lib injection/breakpoint injection) attacks on Linux and Windows binaries.

Components:
patch_reader - the module that loads a patch file at runtime and generates a set of mods for otfpatching
wrapper - module that runs the program, applies otfpatches, and listens for breaks
injection_handler - the module that receives signals from breakpoints, processes logic, and sends it back to the program

wrapper input: binary target
wrapper output: direct modifications to binary
patch_reader input: binary patch file (generated if not available)
patch_reader output: set of binary mods for otf patching (including breakpoints)
injection_handler input: breakpoint signals from program
injection_handler output: return values/logic -> wrapper


