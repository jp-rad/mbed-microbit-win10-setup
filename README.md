# mbed-microbit-win10-setup
The command of mbedubitwin10setup makes it easy to do Arm Mbed CLI programming of the BBC micro:bit on Windows10 and Ptyhon3 environment.

## pip install

```cmd
pip install mbed-cli git+https://github.com/jp-rad/mbed-microbit-win10-setup.git
```

# usage

>
> command: mbedubitwin10
>

Open the command prompt and run below commands.

```cmd
mbed new sample --create-only --scm=none
cd sample
```

Write `.\sample\main.cpp` file.

```cpp
#include "MicroBitDisplay.h"

MicroBitDisplay display;

int main()
{
    display.scroll("Hello world!");
}
```

Connect the BBC micro:bit to the PC. For example, it will be recognized as drive D.  
On the command prompt run below commands in the sample dir.  

```cmd
mbedubitwin10
mbed compile
copy .\BUILD\NRF51_MICROBIT\GCC_ARM\microbit-mbed.hex d:\
```
