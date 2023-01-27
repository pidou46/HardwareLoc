import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover(return_adv=True)
    for d in devices:
        print(devices[d])
    
    #for d in devices:
    #    print(f'{d.discovered_devices_and_advertisement_data.values()}')

asyncio.run(main())

#(BLEDevice(54:43:B2:A9:0D:A6, uBeacon 0DA6), AdvertisementData(local_name='uBeacon 0DA6', service_data={'0000feaa-0000-1000-8000-00805f9b34fb': b'\x00\xbaEddystone!\x00\x00\x00\x00\x00\x01\x00\x00'}, service_uuids=['0000feaa-0000-1000-8000-00805f9b34fb'], rssi=-24))