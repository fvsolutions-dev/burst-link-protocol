from burst_link_protocol import BurstInterfaceC, BurstInterfacePy
import pytest


def test_python():
    interface = BurstInterfacePy()
    packets = [b"Hello, world!", b"Goodbye, world!"]

    data = interface.encode(packets)
    decoded = interface.decode(data)
    assert packets == decoded


def test_python_crc_validation():
    interface = BurstInterfacePy()
    packets = [b"Hello, world!", b"Goodbye, world!"]

    data = bytearray(interface.encode(packets))

    for i in range(len(data)):
        data_copy = data.copy()

        # modify byte x
        data_copy[i] = (data_copy[i] + 1) % 256
        with pytest.raises(Exception):
            decoded = interface.decode(bytes(data_copy))
            print(decoded)
            assert len(decoded) == len(packets), f"Expected {len(packets)} packets, got {len(decoded)}"


def test_large_packets_whole():
    interface = BurstInterfaceC()
    for size in [1, 253, 254, 255, 1023, 1024, 1025, 4000]:
        packet = bytes(i % 251 + 1 for i in range(size))
        assert interface.decode(interface.encode([packet])) == [packet]


def test_many_packets_whole():
    interface = BurstInterfaceC()
    packets = [bytes([i + 1]) * 300 for i in range(20)]
    assert interface.decode(interface.encode(packets)) == packets
