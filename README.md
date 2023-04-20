# No-Shy-Polecat
First exercises with Pyhton and Solace.

There you have the anagram input (thanks https://new.wordsmith.org/anagram/), leading to No Shy Polecat! Nice match with the otter, the overall Soalce mascotte.

The European Polecat https://en.wikipedia.org/wiki/European_polecat

# Links
https://docs.solace.com/API/Messaging-APIs/Python-API/python-home.htm
https://tutorials.solace.dev/python
https://github.com/SolaceSamples/solace-samples-python
https://pypi.org/project/solace-pubsubplus/

# Test

Intalled the solace-pubsubplus Python module with `python3 -m pip install solace-pubsubplus`.

Running script `MessagingService.py` errors (see below) because of arm architecture of my MacBook Pro M2.

````
At https://docs.solace.com/API/API-Developer-Guide/Supported-Environments.htm I see that Python API is supported on macOS 10.15 and later (x86_64 versions) only. Are there any plans to provide support for ARM too?
python3 MessagingService.py
  File "/Users/emilzegers/GitHub/No-Shy-Polecat/MessagingService.py", line 81
emilzegers@emilzegers No-Shy-Polecat % python3 MessagingService.py
Unable to load core library from [/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib]. Exception: dlopen(/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib, 0x0006): tried: '/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64')), '/System/Volumes/Preboot/Cryptexes/OS/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (no such file), '/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))
Traceback (most recent call last):
  File "/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/core/_solace_session.py", line 159, in __load_core_library
    return cdll.LoadLibrary(shared_lib_path_default)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 444, in LoadLibrary
    return self._dlltype(name)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 366, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: dlopen(/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib, 0x0006): tried: '/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64')), '/System/Volumes/Preboot/Cryptexes/OS/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (no such file), '/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))
````

# arm
https://stackoverflow.com/questions/58346120/how-to-cross-compile-a-single-python-library-for-arm
https://stackoverflow.com/questions/70925516/compile-python-modules-for-arm64-architecture