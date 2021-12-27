from ReadWriteMemory import ReadWriteMemory


rwm = ReadWriteMemory()
process = rwm.get_process_by_name('ac_client.exe')
process.open()

baseaddress = 0x400000 

print('\nPrint the Process information.')
print(process.__dict__)




ammo_pointer = process.get_pointer(baseaddress + 0x10F4F4, offsets=[0x150])






ammo = process.read(ammo_pointer)
print(ammo)

