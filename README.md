# TODO

## Development

### Midi input for the esp32

Once you flash the board, it's convenient to be be able to send the board midi signals and also read debug data that the board is sending back. To do that, use the serialmidi.py file which is a copy of the serialmidi project that just prints incoming messages rather than interpreting them as midi. Run it like this:

```
 python3 serialmidi.py --serial_name=/dev/cu.usbserial-0001 --midi_in_name="Circuit"  --midi_out_name="IAC Driver Bus 1"  --debug
```

You need to also "activate the serial bus" as a midi device in Audio Midi Setup to get this to work. Also you'll need to use the right midi_in_name, in my case I am using a novation circuit controller which appears as "Circuit".
