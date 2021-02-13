# <img src="https://raw.githubusercontent.com/PfisterDaniel/PythonCCU/main/www/icon.png" width="48"> PythonCCU
Python Interpreter for Homematic CCU

This addon works only with RaspberryMatic on
(CCU3, Raspberry 2, Raspberry 3, Raspberry 4)

## Supported OS
* [RaspberryMatic](http://homematic-forum.de/forum/viewtopic.php?f=56&t=26917)

## Description
This addon adds a Python interpreter to [RaspberryMatic](http://homematic-forum.de/forum/viewtopic.php?f=56&t=26917).

You can install PIP with following command

    $ python -m ensurepip --default-pip

To update PIP using:

    $ pip install --upgrade pip

Install extensions e.g. Requests:

    $ pip install requests

The extension *requests* is necessary to communicate with the Homematic components!

Run example:

* Change Username and Passwort in line 5:

    $ cd /usr/local/addons/pythonccu/examples
    
    $ nano listRooms.py 
    
    $ python listRooms.py



## Note
Nano is not installed on the CCU, if you want to use nano please install [HM-Tools](https://github.com/fhetty/hm-tools) from a cool guy names fhetty :-)

You can only install extensions that do not require a C compiler. 

## Licenses:
All binaries are compiled from the buildroot system source code.<br>
The source code of the compiled binaries was not modified.<br>
<br>
The source code of the binaries is subject to the following licenses:<br>

| Package | License |
| ------------- | ------------- |
| Python 3.9.1 | [license](https://raw.githubusercontent.com/PfisterDaniel/PythonCCU/main/licenses/LICENSE) |

## Changelog
| Version | Description |
| ------ | ----------- |
| 1.0.0 | Initial Version |
| 1.0.1 | Add examples and bugfixes |

## Bugs and feature requests
Please create an issue in [GitHub](https://github.com/PfisterDaniel/PythonCCU/issues)

