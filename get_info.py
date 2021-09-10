# this programm is for collecting data about the device to be added to the door
import os


# The screen clear function
def screen_clear():
    _ = os.system('clear')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def chk():
    global width_of_device
    abb_list = ('RHGX20', 'RHGX12', 'RHGX8', 'RHGX4', 'HALF', 'PQ8CHU', 'MIDOS', 'SPA-140C', 'SPA-310C', 'ONE')
    # abb_list = ['RHGX20', 'RHGX12', 'RHGX8', 'RHGX4', 'HALF', 'PQ8CHU', 'MIDOS', 'SPA-140C', 'SPA-310C', 'ONE']
    my_size = (
        (470, 210), (300, 210), (216, 210), (132, 210), (102, 158), (150, 110), (103, 177), (142, 162), (226, 162),
        (100, 270))
    my_list = abb_list
    ee_list = ('1DV', '1.5DV', '2DV', '3DH', '3DV', 'QTRN', 'HALFNH', 'HALFNV')
    my_size = my_size + ((170, 233), (170, 362), (170, 422), (454, 233), (170, 524), (105, 118), (153, 124), (124, 153))
    my_list = my_list + ee_list
    er_list = ('1V', '3H', '1N', '3N')
    my_size = my_size + ((168, 243), (455, 243), (73, 128), (156, 128))
    my_list = my_list + er_list
    mtr_list = ('KWH-ALPHA', 'KWH-SIMCO', 'KWH-IMP', '144SQ', '110SQ', '96SQ')
    my_size = my_size + ((200, 275), (170, 267), (181, 277), (144, 144), (110, 110), (96, 96))
    my_list = my_list + mtr_list
    ann_list = (
        'YASH-6P', 'YASH-8P', 'YASH-10P', '240-SQ', 'ALAN-6P', 'ALAN-8P', 'ALAN-11P', 'ALAN-15P', 'ALAN-19P',
        'ALAN-23P')
    my_size = my_size + (
        (240, 125), (310, 125), (380, 125), (240, 240), (265, 166), (265, 166), (265, 205), (315, 183), (315, 223),
        (315, 263))
    my_list = my_list + ann_list
    sw_list = ('75SQ', '48SQ', 'LR95', 'LR75', 'AM', 'BC70X83', 'BC95')
    my_size = my_size + ((75, 75), (48, 48), (95, 95), (75, 75), (95, 95), (70, 83), (95, 95))
    my_list = my_list + sw_list
    ttb = 'CD-TTB'
    n = 0;
    add_more = True

    while add_more:
        screen_clear()
        use_std_size = False
        width_of_device = 0
        height_of_device = 0
        sr_no =1

        variable = input("Item Designation <end if finished> : ").upper()
        while variable == '':
            variable = input("Item Designation <end if finished> : ").upper()
        item_desn = variable

        if item_desn == 'END':
            add_more = False
        else:
            print("\nABB make relays: \n", end='')
            for n in range(0, len(abb_list)):
                print(sr_no, '.', abb_list[n], " ", end='')
                sr_no+=1

            print("\n\nEE make relays : \n", end='')
            for n in range(0, len(ee_list)):
                print(sr_no, '.', ee_list[n], " ", end='')
                sr_no+=1

            print("\n\nER make relays : \n", end='')
            for n in range(0, len(er_list)):
                print(sr_no, '.', er_list[n], " ", end='')
                sr_no+=1

            print("\n\nMeters         : \n", end='')
            for n in range(0, len(mtr_list)):
                print(sr_no, '.', mtr_list[n], " ", end='')
                sr_no+=1

            print("\n\nAnnunciation   : \n", end='')
            for n in range(0, len(ann_list)):
                print(sr_no, '.', ann_list[n], " ", end='')
                sr_no+=1

            print("\n\nSwitches       : \n", end='')
            for n in range(0, len(sw_list)):
                print(sr_no, '.', sw_list[n], " ", end='')
                sr_no+=1
                
            print("\n\nTest terminal block:\n", sr_no, '.', ttb)

            variable = input("Size of Apparatus: ").upper()
            while variable == '':
                variable = input("Size of Apparatus: ").upper()
            for n in range (0, len(my_list)):
                if my_list[n] == variable:
                    use_std_size = True
                    (width_of_device, height_of_device) = my_size[n]

            if not use_std_size:
                width_of_device = 0
                height_of_device = 0
                while width_of_device == 0 or width_of_device == '':
                    width_of_device = input("\nEnter width of device")

                while height_of_device == 0 or height_of_device == '':
                    height_of_device = input("\nEnter height of device")

            case_size = variable

            print("Size = ",  case_size, 'width = ', width_of_device, 'height = ', height_of_device)

            variable = input("Name of Relay: ").upper()
            while variable == '':
                variable = input("Name of Relay: ").upper()
            type = variable

            variable = input("Lable required <Y/N>: ").upper()
            while variable == '':
                variable = input("Lable required <Y/N>: ").upper()
            labelyn = variable


print("running...")

print("\n\n Panel Type	Height		 Door Type\n",
      "\nVHA12S   	 589 mm		VHA-12S1",
      "\nVHA12S   	 871 mm 	VHA-12S2",
      "\nVHA12S   	 951 mm		VHA-12S3",
      "\nVHA12    	 669 mm 	11KVSF1",
      "\nVHA12    	 951 mm 	11KVSF2",
      "\nVHE-800  	 744 mm 	11KVMO1",
      "\nVHE-800 	1000 mm 	11KVMO2",
      "\nVHE-950  	 744 mm 	11KVMO3",
      "\nVHE-950 	1000 mm 	11KVMO4",
      "\n22KVSF6  	 756 mm 	22KVSF",
      "\nVHA 36  	 724 mm 	VHA362",
      "\nVHA 36  	 524 mm 	VHA361",
      "\nUniSafe600   750 mm 	U600-1",
      "\nUniSafe600 	1030 mm 	U600-2",
      "\nUniSafe750   750 mm 	U750-1",
      "\nUniSafe750  1030 mm 	U750-2",
      "\nVHA12D   	 661 mm 	VHA-12D1",
      "\nVHA12D   	 906 mm 	VHA-12D2")
add_yn = "Y"

valid_types = ("VHA-12D1", "VHA-12D2", "VHA-12S1", "VHA-12S2", "VHA-12S3", "11KVMO1",
               "11KVMO2", "11KVMO3", "11KVMO4", "22KVSF", "VHA361", "VHA362", "U600-1", "U600-2", "U750-2", "U750-1")
qty = len(valid_types)
num = 0
door_type = input("Select Door Type : :").upper()
# door_type = door_type.upper()
items = 0;

while items in range(0, qty):
    if door_type == valid_types[items]:
        print("Correct Entry")
        items = items + 1
        break
    else:
        items = items + 1
        if items == qty:
            items = 0;
            door_type = input("Select correct Door Type : :").upper()
chk()