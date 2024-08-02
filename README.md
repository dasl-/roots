# TODO

## Development

### Midi input for the esp32

Once you flash the board, it's convenient to be be able to send the board midi signals and also read debug data that the board is sending back. To do that, use the serialmidi.py file which is a copy of the serialmidi project that just prints incoming messages rather than interpreting them as midi. Run it like this:

```
 python3 serialmidi.py --serial_name=/dev/cu.usbserial-0001 --midi_in_name="Circuit"  --midi_out_name="IAC Driver Bus 1"  --debug
```

You need to also "activate the serial bus" as a midi device in Audio Midi Setup to get this to work. Also you'll need to use the right midi_in_name, in my case I am using a novation circuit controller which appears as "Circuit".

## Initial setup

Install Arduino 1.8.13

Download https://github.com/jordanlewis/ml_synth_organ_example into ~/Documents/Arduino

Clone the following libraries:

Adafruit NeoPixel           1.8.3     1.12.3    user     Arduino library for controlling singl...
arduino-timer               3.0.1     -         user     -
ArduinoBLE                  1.3.7     -         user     -
audio-driver                0.0.1     -         user     -
audio-tools                 0.9.8     -         user     -
audio-tools midi            0.8       -         user     -
BLE-MIDI                    2.2       -         user     -
MIDI Library                5.0.2     -         user     -
ML SynthTools               1.3.1     -         user     -
NimBLE-Arduino              1.4.2     -         user     -
USB Host Shield Library 2.0 1.7.0     -         user     -

clone this into the libraries directory https://github.com/marcel-licence/ML_SynthTools?tab=readme-ov-file

Apply the following diff:

```
diff --git a/src/boards/board_audio_kit_es8388.h b/src/boards/board_audio_kit_es8388.h
index cf21f04..b8d0a36 100644
--- a/src/boards/board_audio_kit_es8388.h
+++ b/src/boards/board_audio_kit_es8388.h
@@ -53,8 +53,8 @@
 #define BOARDS_BOARD_AUDIO_KIT_ES8388_H_


-#define ES8388_CFG_I2C  1
-#define ES8388_CFG_I2S  4
+#define ES8388_CFG_I2C  2
+#define ES8388_CFG_I2S  5


 /* on board led */
diff --git a/src/ml_inline.h b/src/ml_inline.h
index 8398f96..b829f3a 100644
--- a/src/ml_inline.h
+++ b/src/ml_inline.h
@@ -41,11 +41,11 @@
 #include <es8388.h>
 #include <esp32_audio_kit_module.h>
 #if (defined ESP32) || (defined ESP8266) || (defined ARDUINO_RASPBERRY_PI_PICO) || (defined ARDUINO_GENERIC_RP2040)
-#include <fs\fs_access.h>
-#include <fs\fs_common.h>
-#include <fs\fs_esp32.h>
-#include <fs\fs_esp8266.h>
-#include <fs\fs_rp2040.h>
+#include <fs/fs_access.h>
+#include <fs/fs_common.h>
+#include <fs/fs_esp32.h>
+#include <fs/fs_esp8266.h>
+#include <fs/fs_rp2040.h>
 #endif
 #include <i2s_interface.h>
 #include <i2s_module.h>
```


Install esp32 boards in Arduino, version 2.0.2

Symlink python to python3

sudo ln -s $(which python3) /usr/local/bin/python

open /Applications/Arduino\ 2.app

sudo python3 -m pip install --upgrade --break-system-packages python-rtmidi pyserial

