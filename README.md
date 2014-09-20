Python-Minecraft-API
====================

Minecraft Pi API in Python

The original API files listed below were all released under the LICENSE-mcpi.txt

All other files and alterations released under LICENSE.txt

Original Files:

1. `__init__.py`
2. `block.py`
3. `connection.py`
4. `event.py`
5. `minecraft.py`
6. `util.py`
7. `vec3.py`


To run tests in top level folder (where the README is located) run:

`python -m unittest discover`

Optionally you can add a -v to the end of the command for verbose output

`python -m unittest discover -v`

If the Minecraft Pi instance is not available or not running a rough stub for the Minecraft world is available

In another shell change directory to the tests folder and run the following command

`python MinecraftTCPServerStub.py`

To end the running server instance press ctrl+c

This will create a server running on 127.0.0.1:4711 and serve responses from a randomly generated terrain to run tests against.
There is minimal error checking on the server stub currently so it should only be used as an indication of correctness.
