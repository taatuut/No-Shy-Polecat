from string import Template

#from solace.messaging.errors.pubsubplus_client_error import PubSubPlusClientError
from solace.messaging.messaging_service import MessagingService

# source: https://www.solace.dev/
# Solace messaging APIs offer uniform client access to all Solace PubSub+ capabilities and qualities of service, and are available for C, .NET, iOS, Java, JavaScript, JMS, Python and Node.js. Solace also supports popular open protocols like AMQP, JMS, MQTT, REST and WebSocket, and open APIs such as Paho and Qpid.

# to broker

""""
MessagingService messagingService = MessagingService.builder(ConfigurationProfile.V1).fromProperties(properties).build().connect();
DirectMessagePublisher publisher = messagingService.createDirectMessagePublisherBuilder().onBackPressureWait(1).build().start();
OutboundMessage message = messagingService.messageBuilder().build("Hello World!");
Topic topic = Topic.of("solace/try/this/topic");
publisher.publish(message, topic);

# from broker

topic = Topic.of("solace/try/&gt;")
messaging_service = MessagingService.builder().from_properties(broker_props).build().connect()
direct_receiver = messaging_service.create_direct_message_receiver_builder().with_subscriptions(topic).build().start()
direct_receiver.receive_async(MessageHandlerImpl())
"""

# Connect with Python
# Solace Python API over SMF, Paho over MQTT
# Select Python SMF protocol and click [Get Started]

"""
python3 -m pip install solace-pubsubplus
Defaulting to user installation because normal site-packages is not writeable
Collecting solace-pubsubplus
  Downloading solace_pubsubplus-0.2.1-py36-none-any.whl (16.1 MB)
     |████████████████████████████████| 16.1 MB 1.6 MB/s 
Installing collected packages: solace-pubsubplus
Successfully installed solace-pubsubplus-0.2.1
WARNING: You are using pip version 21.2.4; however, version 23.1 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.
python3 -m pip install --upgrade pip
"""

"""
python3 -m pip install --upgrade pip
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pip in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Downloading pip-23.1-py3-none-any.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 3.8 MB/s 
Installing collected packages: pip
  WARNING: The scripts pip, pip3, pip3.10 and pip3.9 are installed in '/Users/emilzegers/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-23.1
"""


""""
default macos terminal is zsh
chnage path in ~/.zshrc and ~/.bash_profile

vim ~/.zshrc
export PATH="/Users/emilzegers/Library/Python/3.9/bin:$PATH"

source ~/.zshrc
"""

# determine
# echo $0
# source: https://www.moncefbelyamani.com/which-shell-am-i-using-how-can-i-switch/

# SMF, can also select Secured SMF and Compressed SMF

broker_props = {
    "solace.messaging.transport.host": "xxx",
    "solace.messaging.service.vpn-name": "yyy",
    "solace.messaging.authentication.scheme.basic.username": "zzz",
    "solace.messaging.authentication.scheme.basic.password": "***",
}

messaging_service = MessagingService.builder().from_properties(broker_props).with_reconnection_retry_strategy(RetryStrategy.parametrized_retry(20,3)).build()

messaging_service.connect()

""""
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

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/emilzegers/GitHub/No-Shy-Polecat/MessagingService.py", line 4, in <module>
    from solace.messaging.messaging_service import MessagingService
  File "/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/__init__.py", line 32, in <module>
    CORE_LIB = _SolaceApiLibrary().solclient_core_library
  File "/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/core/_solace_session.py", line 79, in __new__
    cls._core_lib = cls.__load_core_library()
  File "/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/core/_solace_session.py", line 163, in __load_core_library
    raise PubSubPlusClientError(message=f'{UNABLE_TO_LOAD_SOLCLIENT_LIBRARY} '
solace.messaging.errors.pubsubplus_client_error.PubSubPlusClientError: (PubSubPlusClientError(...), "Unable to load core library from [/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib]. Exception: dlopen(/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib, 0x0006): tried: '/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64')), '/System/Volumes/Preboot/Cryptexes/OS/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (no such file), '/Users/emilzegers/Library/Python/3.9/lib/python/site-packages/solace/messaging/lib/macosx-x86_64/libsolclient.dylib' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))")
"""