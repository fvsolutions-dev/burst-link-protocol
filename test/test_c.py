from burst_link_protocol import BurstInterfaceC, BurstInterfacePy


def test_c_encoding_decoding():
    c_interface = BurstInterfaceC()

    packets = [b"Hello, world!", b"Goodbye, world!"]

    decoded = c_interface.decode(c_interface.encode(packets))
    print(decoded)
    assert packets == decoded, f"Expected {packets}, got {decoded}"


def test_c_encoding_decoding_fail():
    c_interface = BurstInterfaceC()

    packets = [b"\0Hello, world!"]

    decoded = c_interface.decode(c_interface.encode(packets))
    print(decoded)
    assert packets == decoded, f"Expected {packets}, got {decoded}"



def test_c_packet_filling_the_buffer():
    # The binding's decoder buffer is 4096 bytes: a packet of 4094 and its CRC fill it exactly,
    # and its delimiter still has to come
    c_interface = BurstInterfaceC()

    packets = [bytes((i % 255) + 1 for i in range(4094))]

    decoded = c_interface.decode(BurstInterfacePy().encode(packets), fail_on_crc_error=True)
    assert packets == decoded, f"Expected 4094 bytes, got {[len(p) for p in decoded]}"


if __name__ == "__main__":
    test_c_encoding_decoding()
