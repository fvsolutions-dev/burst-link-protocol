import pytest

from burst_link_protocol import BurstInterfaceC, BurstInterfacePy

payloads = [
    # Malformed packet
    (
        "04 01 ff 0e 06 d3 23 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 03 85 1f 00 0b 02 04 02 07 02 0b 02 04 02 08 02 0b 02 04 02 0c 02 0b 02 02 02 0d 02 0b 02 02 03 aa 94 00 04 02 ff 0e 03 d3 23 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 03 85 1f 00"
    ),
    # Good packet
    (
        "04 02 ff 0e 03 e1 23 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 03 99 fe 00"
    ),
    (
        "04 01 ff 0e 06 ef be ad de c1 02 0b 02 01 02 01 02 0b 02 04 02 02 02 0b 02 04 02 03 02 0b 02 04 02 04 02 0b 02 04 02 05 02 0b 02 04 02 06 02 0b 02 04 02 a6 02 0b 02 04 02 07 02 0b 02 04 02 08 02 0b 02 04 02 0c 02 0b 02 02 02 0d 02 0b 02 02 03 aa 94 00"
    )
]


def as_bytes(payload):
    return bytes.fromhex(payload.replace(" ", ""))


def test_malformed_packet():
    malformed = as_bytes(payloads[0])

    # The C decoder drops it and keeps the good packet behind it, the Python one raises
    c_interface = BurstInterfaceC()
    assert [len(packet) for packet in c_interface.decode(malformed)] == [49]
    assert c_interface.crc_errors + c_interface.decode_errors > 0

    with pytest.raises(ValueError):
        BurstInterfacePy().decode(malformed)


@pytest.mark.parametrize("payload", payloads[1:])
def test_good_packets_decode_the_same(payload):
    payload = as_bytes(payload)

    c_decoded = [bytes(packet) for packet in BurstInterfaceC().decode(payload)]

    assert len(c_decoded) == 1
    assert c_decoded == BurstInterfacePy().decode(payload)
