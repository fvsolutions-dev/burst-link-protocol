# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.6] - 2026-11-04

### Added

- `BURST_MAX_ENCODED`, the encoded size of a packet
- A Zephyr module

### Changed

- The package is built as Release, without coverage counters. Importing it no longer prints
  `profiling:` lines on exit
- The Python decoder's buffer is 4 KiB
- `numpy` is no longer a dependency: only the tests use it. Nor are `pytest`, its plugins,
  `scikit-build-core` and `nanobind`
- Wheels are built with cibuildwheel 4, and each is tested as it is built. Linux wheels now need
  glibc 2.28 or later, and there are no more 32-bit Linux or PyPy wheels

### Fixed

- The Python encoder cut off packets of about 1024 bytes and more. It now sizes its buffer per call,
  and raises when a packet cannot be encoded
- The decoder counted an overflow on a packet that exactly fills its buffer
- An ESP-IDF build is detected with `ESP_PLATFORM`, so other builds in an environment with ESP-IDF
  installed no longer take the wrong branch
- `pydantic` is declared as a dependency, so importing the package works on a clean install
- `SerialBurstInterface.close()` waits for its transmit thread, with a timeout

## [1.1.5] - 2025-06-15

### Added

- More statistics in `SerialBurstInterface`, and `BurstSerialStatistics` exported from the package

## [1.1.4] - 2025-06-15

Released from the tag `v1.1.0`.

### Added

- `SerialBurstInterface`, a serial port with BURST framing
- Managed encoder and decoder in C, which keep their own state between calls
- Statistics from the decoder, also in the Python bindings
- ESP-IDF build support

### Changed

- The source files are restructured

### Fixed

- The CRC function has a name of its own (`blp_crc16_ccitt`), so it no longer conflicts with others
  in the same build
- Compiler errors and warnings, and the Zephyr build
- `pyserial` and `janus` are declared as dependencies

## [1.0.5] - 2025-03-25

### Fixed

- nanobind's reference leak warnings are off

## [1.0.4] - 2025-03-25

### Fixed

- The decoder is rewritten to fix its decoding

## [1.0.3] - 2025-03-25

### Added

- A Zephyr `CMakeLists.txt`

### Fixed

- The decoder lost a packet's last byte, which came in with 1.0.2

## [1.0.2] - 2025-03-06

### Changed

- The decoder drops the last byte from a packet's size

## [1.0.1] - 2025-02-25

The first version on PyPI; uploading 1.0.0 failed.

## [1.0.0] - 2025-02-23

The first release: encoding and decoding packets with COBS and a CRC-16, in C with Python bindings,
and a Python implementation.
