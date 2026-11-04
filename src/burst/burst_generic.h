
#ifndef BURST_GENERIC_H
#define BURST_GENERIC_H
#include <stdint.h>
#include <stddef.h>

// Status codes returned by the encoder.
typedef enum
{
	BURST_DATA_CONSUMED,
	BURST_PACKET_READY,
	BURST_OVERFLOW_ERROR,
	BURST_ENCODE_ERROR,
	BURST_CRC_ERROR,
	BURST_DECODE_ERROR
} burst_status_t;

typedef struct
{
	uint8_t *data;
	size_t size;
} burst_packet_t;

#define COBS_DELIMITER 0x00
#define COBS_MAX_CODE 0xFF
#define CRC_SIZE sizeof(uint16_t)
// A packet of size bytes and its CRC, encoded, at worst: a code byte every 254 bytes, the first
// one, the delimiter
#define BURST_MAX_ENCODED(size) ((size) + ((size) + CRC_SIZE) / 254 + 2 + CRC_SIZE)

uint16_t burst_crc16(const uint8_t *data, size_t length);

#endif // BURST_GENERIC_H