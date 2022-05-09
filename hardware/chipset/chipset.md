# Chipset

- It's a `silicone backbone` single integrated circuit soldered into the motherboard
- Also referred to as the `Platform Controller Hub` (PCH)
- It relays communications between the CPU and the other components
- The name of the chipset is included in the motherboard name (E.g., B450M GAMING)

## North and South bridges

- On older motherboards, the chipset was split into two circuits

- **Northbridge** (Memory Controller Hub)

  - Handles high speed communication with the CPU
  - CPU <-> RAM
  - CPU <-> Display
  - CPU <-> PCIe slots

- **Southbridge** (I/O Hub)

  - Handles slow speed communication with the northbridge
  - Ethernet
  - Audio
  - PCI slots
  - Sata ports
  - USB ports

## Direct Media Interface (DMI)

- `Direct Media Interface` (DMI) is the `communication lane` between the CPU and the Chipset
- Today the high speed communication is built-in in the processor (formerly done via northbridge)
  - Therefore the CPU communicates directly with RAM, display and PCIe slots
  - For communication with slow speed I/O, `DMI` is used in order to talk to the chipset
