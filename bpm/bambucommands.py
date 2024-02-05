ANNOUNCE_PUSH =             {
                                "pushing":{
                                    "command":"pushall",
                                    "push_target":1,
                                    "sequence_id":"0",
                                    "version":1
                                }
                            }

ANNOUNCE_VERSION =          {
                                "info":{
                                    "command":"get_version",
                                    "sequence_id":"0"
                                }
                            }

CHAMBER_LIGHT_TOGGLE =      {
                                "system": {
                                    "sequence_id": "0", 
                                    "command": "ledctrl", 
                                    "led_node": "chamber_light", 
                                    "led_mode": "on",
                                    "led_on_time": 500, 
                                    "led_off_time": 500, 
                                    "loop_times": 0, 
                                    "interval_time": 0
                                }
                            }

SPEED_PROFILE_TEMPLATE =    {
                                "print": {
                                    "sequence_id": "0",
                                    "command": "print_speed", 
                                    "param": "2"
                                }
                            }

PAUSE_PRINT =               {
                                "print": {
                                    "sequence_id": "0", 
                                    "command": "pause"
                                }
                            }

RESUME_PRINT =              {
                                "print": {
                                    "sequence_id": "0", 
                                    "command": "resume"
                                }
                            }

STOP_PRINT =                {
                                    "print": {
                                        "sequence_id": "0", 
                                        "command": "stop"
                                    }
                            }

SEND_GCODE_TEMPLATE =       {
                                "print": {
                                    "sequence_id": "0", 
                                    "command": "gcode_line", 
                                    "param": ""
                                }
                            }

MOVE_RIGHT =                {
                                "print": {
                                    "sequence_id": "0", 
                                    "command": "gcode_line", 
                                    "param": "G91\nG1 X100 F3600\n"
                                }
                            }

MOVE_LEFT =                 {
                                "print": {
                                    "sequence_id": "0", 
                                    "command": "gcode_line", 
                                    "param": "G91\nG1 X-100 F3600\n"
                                }
                            }

UNLOAD_FILAMENT =           {
                                "print": {
                                    "sequence_id": "0",
                                    "command": "unload_filament"
                                }
                            }

AMS_FILAMENT_CHANGE =       {
                                "print": {
                                    "sequence_id": "0",
                                    "command": "ams_change_filament",
                                    "target": 0, 
                                    "curr_temp": 250, 
                                    "tar_temp": 250
                                }
                            }

PRINT_3MF_FILE =            {
                                "print": {
                                    "ams_mapping": [],
                                    "bed_leveling": True,
                                    "bed_type": "hot_plate",
                                    "command": "project_file",
                                    "file": "Oreo.gcode.3mf",
                                    "flow_cali": True,
                                    "layer_inspect": True,
                                    "md5": "",
                                    "param": "Metadata/plate_1.gcode",
                                    "profile_id": "0",
                                    "project_id": "0",
                                    "sequence_id": "0",
                                    "subtask_id": "0",
                                    "subtask_name": "Oreo",
                                    "task_id": "0",
                                    "timelapse": False,
                                    "url": "file:///sdcard/Oreo.gcode.3mf",
                                    "use_ams": False,
                                    "vibration_cali": False
                                }
                            }

# X1 only currently
GET_ACCESSORIES = {"system": {"sequence_id": "0", "command": "get_accessories", "accessory_type": "none"}}

HMS_STATUS = {
  "result": 0,
  "t": 1699198652,
  "ver": 202311050300,
  "data": {
    "device_hms": {
      "ver": 202311050300,
      "en": [
        {
          "ecode": "0300010000010001",
          "intro": "The heatbed temperature is abnormal; the heater may have a short circuit."
        },
        {
          "ecode": "0300010000010002",
          "intro": "The heatbed temperature is abnormal; the heater may have an open circuit, or the thermal switch may be open."
        },
        {
          "ecode": "0300010000010003",
          "intro": "The heatbed temperature is abnormal; the heater is over temperature."
        },
        {
          "ecode": "0300020000010001",
          "intro": "The nozzle temperature is abnormal; the heater may have a short circuit."
        },
        {
          "ecode": "0300020000010002",
          "intro": "The nozzle temperature is abnormal; the heater may have an open circuit."
        },
        {
          "ecode": "0300020000010003",
          "intro": "The nozzle temperature is abnormal; the heater is over temperature."
        },
        {
          "ecode": "0300030000010001",
          "intro": "The speed of the nozzle fan is too slow or stopped. It may be stuck or the connector is not plugged in properly."
        },
        {
          "ecode": "0300030000020002",
          "intro": ""
        },
        {
          "ecode": "0300040000020001",
          "intro": "The speed of the part cooling fan is too slow or stopped. It may be stuck or the connector is not plugged in properly."
        },
        {
          "ecode": "0300050000010001",
          "intro": "The motor driver is overheating. Its radiator may be loose, or its cooling fan may be damaged."
        },
        {
          "ecode": "0300060000010001",
          "intro": "Motor-A has an open-circuit. There may be a loose connection, or the motor may have failed."
        },
        {
          "ecode": "0300060000010002",
          "intro": "Motor-A has a short-circuit. It may have failed."
        },
        {
          "ecode": "0300070000010001",
          "intro": "Motor-B has an open-circuit. The connection may be loose, or the motor may have failed."
        },
        {
          "ecode": "0300070000010002",
          "intro": "Motor-B has a short-circuit. It may have failed."
        },
        {
          "ecode": "0300080000010001",
          "intro": "Motor-Z has an open-circuit. The connection may be loose, or the motor may have failed."
        },
        {
          "ecode": "0300080000010002",
          "intro": "Motor-Z has a short-circuit. It may have failed."
        },
        {
          "ecode": "0300090000010001",
          "intro": "Motor-E has an open-circuit. The connection may be loose, or the motor may have failed."
        },
        {
          "ecode": "0300090000010002",
          "intro": "Motor-E has a short-circuit. It may have failed."
        },
        {
          "ecode": "03000A0000010001",
          "intro": "Heatbed force sensor 1 is too sensitive. It may be stuck between the strain arm and heatbed support, or the adjusting screw may be too tight."
        },
        {
          "ecode": "03000A0000010002",
          "intro": "The signal of heatbed force sensor 1 is weak. The force sensor may be broken or have poor electric connection."
        },
        {
          "ecode": "03000A0000010003",
          "intro": "The signal of heatbed force sensor 1 is too weak. The electronic connection to the sensor may be broken."
        },
        {
          "ecode": "03000A0000010004",
          "intro": "An external disturbance was detected on force sensor 1. The heatbed plate may have touched something outside the heatbed."
        },
        {
          "ecode": "03000A0000010005",
          "intro": "Force sensor 1 detected unexpected continuous force. The heatbed may be stuck, or the analog front end may be broken."
        },
        {
          "ecode": "03000B0000010001",
          "intro": "Heatbed force sensor 2 is too sensitive. It may be stuck between the strain arm and heatbed support, or the adjusting screw may be too tight."
        },
        {
          "ecode": "03000B0000010003",
          "intro": "The signal of heatbed force sensor 2 is too weak. The electronic connection to the sensor may be broken."
        },
        {
          "ecode": "03000B0000010004",
          "intro": "An external disturbance was detected on force sensor 2. The heatbed plate may have touched something outside the heatbed."
        },
        {
          "ecode": "03000B0000010005",
          "intro": "Force sensor 2 detected unexpected continuous force. The heatbed may be stuck, or the analog front end may be broken."
        },
        {
          "ecode": "03000B0000010002",
          "intro": "The signal of heatbed force sensor 2 is weak. The force sensor may be broken or have poor electric connection."
        },
        {
          "ecode": "03000C0000010001",
          "intro": "Heatbed force sensor 3 is too sensitive. It may be stuck between the strain arm and heatbed support, or the adjusting screw may be too tight."
        },
        {
          "ecode": "03000C0000010002",
          "intro": "The signal of heatbed force sensor 3 is weak. The force sensor may be broken or have poor electric connection."
        },
        {
          "ecode": "03000C0000010003",
          "intro": "The signal of heatbed force sensor 3 is too weak. The electronic connection to the sensor may be broken."
        },
        {
          "ecode": "03000C0000010004",
          "intro": "An external disturbance was detected on force sensor 3. The heatbed plate may have touched something outside the heatbed."
        },
        {
          "ecode": "03000C0000010005",
          "intro": "Force sensor 3 detected unexpected continuous force. The heatbed may be stuck, or the analog front end may be broken."
        },
        {
          "ecode": "03000D0000010002",
          "intro": "Heatbed homing failed. The environmental vibration is too great."
        },
        {
          "ecode": "03000D0000010003",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000010004",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000010005",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000010006",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000010007",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000010008",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000010009",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D000001000A",
          "intro": "The build plate is not placed properly. Please adjust it."
        },
        {
          "ecode": "03000D0000020001",
          "intro": "Heatbed homing abnormal: there may be a bulge on the heatbed or the nozzle tip may not be clean."
        },
        {
          "ecode": "03000F0000010001",
          "intro": "The accelerometer data is unavailable. The communication connection to the tool head may be broken, or the accelerometer may be damaged."
        },
        {
          "ecode": "0300100000020001",
          "intro": "The resonance frequency of the X axis is low. The timing belt may be loose."
        },
        {
          "ecode": "0300110000020001",
          "intro": "The resonance frequency of the Y axis is low. The timing belt may be loose."
        },
        {
          "ecode": "0300120000020001",
          "intro": "The front cover of the toolhead fell off."
        },
        {
          "ecode": "0500010000020001",
          "intro": "The media pipeline is malfunctioning."
        },
        {
          "ecode": "0500010000020002",
          "intro": "USB camera is not connected. Please check video camera cable connection."
        },
        {
          "ecode": "0500010000020003",
          "intro": "USB camera is malfunctioning."
        },
        {
          "ecode": "0500010000030004",
          "intro": "Not enough space in MicroSD Card, please clear some space."
        },
        {
          "ecode": "0500010000030005",
          "intro": "MicroSD Card error: please reinsert, format or replace it."
        },
        {
          "ecode": "0500010000030006",
          "intro": "Unformatted MicroSD Card: please format it."
        },
        {
          "ecode": "0500020000020001",
          "intro": "Failed to connect internet. Please check the network connection."
        },
        {
          "ecode": "0500020000020002",
          "intro": "Device login failed; please check your account information."
        },
        {
          "ecode": "0500020000020003",
          "intro": "Failed to connect internet; please check the network connection."
        },
        {
          "ecode": "0500020000020004",
          "intro": "Unauthorized user: please check your account information."
        },
        {
          "ecode": "0500020000020005",
          "intro": "Failed to connect internet; please check the network connection."
        },
        {
          "ecode": "0500020000020006",
          "intro": "Liveview service is malfunctioning; please check your network connection."
        },
        {
          "ecode": "0500020000020007",
          "intro": "Liveview service login failed; please check your network connection."
        },
        {
          "ecode": "0500030000010001",
          "intro": "The MC module is malfunctioning; please restart the device or check device cable connection."
        },
        {
          "ecode": "0500030000010002",
          "intro": "The toolhead is malfunctioning. Please restart the device."
        },
        {
          "ecode": "0500030000010003",
          "intro": "The AMS module is malfunctioning. Please restart the device."
        },
        {
          "ecode": "0500030000010004",
          "intro": "The AHB module is malfunctioning. Please restart the device."
        },
        {
          "ecode": "0500030000010005",
          "intro": "Internal service is malfunctioning. Please restart the device."
        },
        {
          "ecode": "0500030000010006",
          "intro": "A system panic occurred. Please restart the device."
        },
        {
          "ecode": "0500030000010008",
          "intro": "A system hang occurred. Please restart the device."
        },
        {
          "ecode": "0500030000010009",
          "intro": "A system hang occurred. It has been recovered by automatic restart."
        },
        {
          "ecode": "050003000001000a",
          "intro": "System state is abnormal; please restore factory settings."
        },
        {
          "ecode": "050003000001000b",
          "intro": "The screen is malfunctioning; please restart the device."
        },
        {
          "ecode": "050003000002000c",
          "intro": "Wireless hardware error: please turn off/on WiFi or restart the device."
        },
        {
          "ecode": "050003000002000d",
          "intro": "The SD Card controller is malfunctioning."
        },
        {
          "ecode": "0500030000030007",
          "intro": "A system panic occurred. It has been recovered by automatic restart."
        },
        {
          "ecode": "0500040000010001",
          "intro": "Failed to download print job. Please check your network connection."
        },
        {
          "ecode": "0500040000010002",
          "intro": "Failed to report print state. Please check your network connection."
        },
        {
          "ecode": "0500040000010003",
          "intro": "The content of print file is unreadable. Please resend the print job."
        },
        {
          "ecode": "0500040000010004",
          "intro": "The print file is unauthorized."
        },
        {
          "ecode": "0500040000010006",
          "intro": "Failed to resume previous print."
        },
        {
          "ecode": "0700010000010001",
          "intro": "The AMS1 assist motor has slipped. The extrusion wheel may be worn down, or the filament may be too thin."
        },
        {
          "ecode": "0700010000010003",
          "intro": "The AMS1 assist motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0700010000010004",
          "intro": "The AMS1 assist motor speed control is malfunctioning. The speed sensor may be faulty."
        },
        {
          "ecode": "0700010000020002",
          "intro": "The AMS1 assist motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0700020000010001",
          "intro": "AMS1 Filament speed and length error: The filament odometry may be faulty."
        },
        {
          "ecode": "0700100000010001",
          "intro": "The AMS1 slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0700100000010003",
          "intro": "The AMS1 slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0700100000020002",
          "intro": "The AMS1 slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0700110000010001",
          "intro": "The AMS1 slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0700110000010003",
          "intro": "The AMS1 slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0700110000020002",
          "intro": "The AMS1 slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0700120000010001",
          "intro": "The AMS1 slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0700120000010003",
          "intro": "The AMS1 slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0700120000020002",
          "intro": "The AMS1 slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0700130000010001",
          "intro": "The AMS1 slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0700130000010003",
          "intro": "The AMS1 slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0700130000020002",
          "intro": "The AMS1 slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0700200000020001",
          "intro": "AMS1 Slot1 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0700200000020002",
          "intro": "AMS1 Slot1 is empty; please load a new filament."
        },
        {
          "ecode": "0700200000020003",
          "intro": "AMS1 Slot1's filament may be broken in AMS."
        },
        {
          "ecode": "0700210000020001",
          "intro": "AMS1 Slot2 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0700210000020002",
          "intro": "AMS1 Slot2 is empty; please load a new filament."
        },
        {
          "ecode": "0700210000020003",
          "intro": "AMS1 Slot2's filament may be broken in AMS."
        },
        {
          "ecode": "0700220000020001",
          "intro": "AMS1 Slot3 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0700220000020002",
          "intro": "AMS1 Slot3 is empty; please load a new filament."
        },
        {
          "ecode": "0700220000020003",
          "intro": "AMS1 Slot3's filament may be broken in AMS."
        },
        {
          "ecode": "0700230000020001",
          "intro": "AMS1 Slot4 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0700230000020002",
          "intro": "AMS1 Slot4 is empty; please load a new filament."
        },
        {
          "ecode": "0700230000020003",
          "intro": "AMS1 Slot4's filament may be broken in AMS."
        },
        {
          "ecode": "0700300000010001",
          "intro": "The RFID board between AMS1 Slot1 & Slot2 has an error."
        },
        {
          "ecode": "0700300000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0700300000020002",
          "intro": "The RFID-tag on AMS1 Slot1 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0700300000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0700310000010001",
          "intro": "The RFID board between AMS1 Slot3 & Slot4 has an error."
        },
        {
          "ecode": "0700310000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0700310000020002",
          "intro": "The RFID-tag on AMS1 Slot2 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0700310000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0700320000020002",
          "intro": "The RFID-tag on AMS1 Slot3 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0700330000020002",
          "intro": "The RFID-tag on AMS1 Slot4 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0700350000010001",
          "intro": "The temperature and humidity sensor has an error. The chip may be faulty."
        },
        {
          "ecode": "0700400000020001",
          "intro": "The filament buffer position signal lost: the cable or position sensor may be malfunctioning."
        },
        {
          "ecode": "0700400000020002",
          "intro": "The filament buffer position signal error: the position sensor may be malfunctioning."
        },
        {
          "ecode": "0700400000020003",
          "intro": "The AMS Hub communication is abnormal, the cable may be not well connected."
        },
        {
          "ecode": "0700450000020001",
          "intro": "The filament cutter sensor is malfunctioning; please check whether the connector is properly plugged in."
        },
        {
          "ecode": "0700450000020002",
          "intro": "The filament cutter's cutting distance is too large. The XY motor may lose steps."
        },
        {
          "ecode": "0700450000020003",
          "intro": "The filament cutter handle has not released. The handle or blade may be stuck."
        },
        {
          "ecode": "0701010000010001",
          "intro": "The AMS2 assist motor has slipped. The extrusion wheel may be worn down, or the filament may be too thin."
        },
        {
          "ecode": "0701010000010003",
          "intro": "The AMS2 assist motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0701010000010004",
          "intro": "The AMS2 assist motor speed control is malfunctioning. The speed sensor may be faulty."
        },
        {
          "ecode": "0701010000020002",
          "intro": "The AMS2 assist motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0701020000010001",
          "intro": "AMS2 Filament speed and length error: The filament odometry may be faulty."
        },
        {
          "ecode": "0701100000010001",
          "intro": "The AMS2 slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0701100000010003",
          "intro": "The AMS2 slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0701100000020002",
          "intro": "The AMS2 slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0701110000010001",
          "intro": "The AMS2 slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0701110000010003",
          "intro": "The AMS2 slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0701110000020002",
          "intro": "The AMS2 slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0701120000010001",
          "intro": "The AMS2 slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0701120000010003",
          "intro": "The AMS2 slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0701120000020002",
          "intro": "The AMS2 slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0701130000010001",
          "intro": "The AMS2 slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0701130000010003",
          "intro": "The AMS2 slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0701130000020002",
          "intro": "The AMS2 slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0701200000020001",
          "intro": "AMS2 Slot1 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0701200000020002",
          "intro": "AMS2 Slot1 is empty; please load a new filament."
        },
        {
          "ecode": "0701200000020003",
          "intro": "AMS2 Slot1's filament may be broken in AMS."
        },
        {
          "ecode": "0701210000020001",
          "intro": "AMS2 Slot2 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0701210000020002",
          "intro": "AMS2 Slot2 is empty; please load a new filament."
        },
        {
          "ecode": "0701210000020003",
          "intro": "AMS2 Slot2's filament may be broken in AMS."
        },
        {
          "ecode": "0701220000020001",
          "intro": "AMS2 Slot3 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0701220000020002",
          "intro": "AMS2 Slot3 is empty; please load a new filament."
        },
        {
          "ecode": "0701220000020003",
          "intro": "AMS2 Slot3's filament may be broken in AMS."
        },
        {
          "ecode": "0701230000020001",
          "intro": "AMS2 Slot4 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0701230000020002",
          "intro": "AMS2 Slot4 is empty; please load a new filament."
        },
        {
          "ecode": "0701230000020003",
          "intro": "AMS2 Slot4's filament may be broken in AMS."
        },
        {
          "ecode": "0701300000010001",
          "intro": "The RFID board between AMS2 Slot1 & Slot2 has an error."
        },
        {
          "ecode": "0701300000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0701300000020002",
          "intro": "The RFID-tag on AMS2 Slot1 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0701300000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0701310000010001",
          "intro": "The RFID board between AMS2 Slot3 & Slot4 has an error."
        },
        {
          "ecode": "0701310000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0701310000020002",
          "intro": "The RFID-tag on AMS2 Slot2 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0701310000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0701320000020002",
          "intro": "The RFID-tag on AMS2 Slot3 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0701330000020002",
          "intro": "The RFID-tag on AMS2 Slot4 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0701350000010001",
          "intro": "The temperature and humidity sensor has an error. The chip may be faulty."
        },
        {
          "ecode": "0702010000010001",
          "intro": "The AMS3 assist motor has slipped. The extrusion wheel may be worn down, or the filament may be too thin."
        },
        {
          "ecode": "0702010000010003",
          "intro": "The AMS3 assist motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0702010000010004",
          "intro": "The AMS3 assist motor speed control is malfunctioning. The speed sensor may be faulty."
        },
        {
          "ecode": "0702010000020002",
          "intro": "The AMS3 assist motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0702020000010001",
          "intro": "AMS3 Filament speed and length error: The filament odometry may be faulty."
        },
        {
          "ecode": "0702100000010001",
          "intro": "The AMS3 slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0702100000010003",
          "intro": "The AMS3 slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0702100000020002",
          "intro": "The AMS3 slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0702110000010001",
          "intro": "The AMS3 slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0702110000010003",
          "intro": "The AMS3 slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0702110000020002",
          "intro": "The AMS3 slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0702120000010001",
          "intro": "The AMS3 slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0702120000010003",
          "intro": "The AMS3 slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0702120000020002",
          "intro": "The AMS3 slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0702130000010001",
          "intro": "The AMS3 slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0702130000010003",
          "intro": "The AMS3 slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0702130000020002",
          "intro": "The AMS3 slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0702200000020001",
          "intro": "AMS3 Slot1 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0702200000020002",
          "intro": "AMS3 Slot1 is empty; please load a new filament."
        },
        {
          "ecode": "0702200000020003",
          "intro": "AMS3 Slot1's filament may be broken in AMS."
        },
        {
          "ecode": "0702210000020001",
          "intro": "AMS3 Slot2 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0702210000020002",
          "intro": "AMS3 Slot2 is empty; please load a new filament."
        },
        {
          "ecode": "0702210000020003",
          "intro": "AMS3 Slot2's filament may be broken in AMS."
        },
        {
          "ecode": "0702220000020001",
          "intro": "AMS3 Slot3 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0702220000020002",
          "intro": "AMS3 Slot3 is empty; please load a new filament."
        },
        {
          "ecode": "0702220000020003",
          "intro": "AMS3 Slot3's filament may be broken in AMS."
        },
        {
          "ecode": "0702230000020001",
          "intro": "AMS3 Slot4 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0702230000020002",
          "intro": "AMS3 Slot4 is empty; please load a new filament."
        },
        {
          "ecode": "0702230000020003",
          "intro": "AMS3 Slot4's filament may be broken in AMS."
        },
        {
          "ecode": "0702300000010001",
          "intro": "The RFID board between AMS3 Slot1 & Slot2 has an error."
        },
        {
          "ecode": "0702300000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0702300000020002",
          "intro": "The RFID-tag on AMS3 Slot1 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0702300000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0702310000010001",
          "intro": "The RFID board between AMS3 Slot3 & Slot4 has an error."
        },
        {
          "ecode": "0702310000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0702310000020002",
          "intro": "The RFID-tag on AMS3 Slot2 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0702310000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0702320000020002",
          "intro": "The RFID-tag on AMS3 Slot3 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0702330000020002",
          "intro": "The RFID-tag on AMS3 Slot4 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0702350000010001",
          "intro": "The temperature and humidity sensor has an error. The chip may be faulty."
        },
        {
          "ecode": "0703010000010001",
          "intro": "The AMS4 assist motor has slipped. The extrusion wheel may be worn down, or the filament may be too thin."
        },
        {
          "ecode": "0703010000010003",
          "intro": "The AMS4 assist motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0703010000010004",
          "intro": "The AMS4 assist motor speed control is malfunctioning. The speed sensor may be faulty."
        },
        {
          "ecode": "0703010000020002",
          "intro": "The AMS4 assist motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0703020000010001",
          "intro": "AMS4 Filament speed and length error: The filament odometry may be faulty."
        },
        {
          "ecode": "0703100000010001",
          "intro": "The AMS4 slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0703100000010003",
          "intro": "The AMS4 slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0703100000020002",
          "intro": "The AMS4 slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0703110000010001",
          "intro": "The AMS4 slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0703110000010003",
          "intro": "The AMS4 slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0703110000020002",
          "intro": "The AMS4 slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0703120000010001",
          "intro": "The AMS4 slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0703120000010003",
          "intro": "The AMS4 slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0703120000020002",
          "intro": "The AMS4 slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0703130000010001",
          "intro": "The AMS4 slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "0703130000010003",
          "intro": "The AMS4 slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "0703130000020002",
          "intro": "The AMS4 slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "0703200000020001",
          "intro": "AMS4 Slot1 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0703200000020002",
          "intro": "AMS4 Slot1 is empty; please load a new filament."
        },
        {
          "ecode": "0703200000020003",
          "intro": "AMS4 Slot1's filament may be broken in AMS."
        },
        {
          "ecode": "0703210000020001",
          "intro": "AMS4 Slot2 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0703210000020002",
          "intro": "AMS4 Slot2 is empty; please load a new filament."
        },
        {
          "ecode": "0703210000020003",
          "intro": "AMS4 Slot2's filament may be broken in AMS."
        },
        {
          "ecode": "0703220000020001",
          "intro": "AMS4 Slot3 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0703220000020002",
          "intro": "AMS4 Slot3 is empty; please load a new filament."
        },
        {
          "ecode": "0703220000020003",
          "intro": "AMS4 Slot3's filament may be broken in AMS."
        },
        {
          "ecode": "0703230000020001",
          "intro": "AMS4 Slot4 filament has run out. Please insert a new filament."
        },
        {
          "ecode": "0703230000020002",
          "intro": "AMS4 Slot4 is empty; please load a new filament."
        },
        {
          "ecode": "0703230000020003",
          "intro": "AMS4 Slot4's filament may be broken in AMS."
        },
        {
          "ecode": "0703300000010001",
          "intro": "The RFID board between AMS4 Slot1 & Slot2 has an error."
        },
        {
          "ecode": "0703300000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0703300000020002",
          "intro": "The RFID-tag on AMS4 Slot1 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0703300000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0703310000010001",
          "intro": "The RFID board between AMS4 Slot3 & Slot4 has an error."
        },
        {
          "ecode": "0703310000010004",
          "intro": "Encryption chip failure."
        },
        {
          "ecode": "0703310000020002",
          "intro": "The RFID-tag on AMS4 Slot2 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0703310000030003",
          "intro": "RFID cannot be read because of a hardware or structural error."
        },
        {
          "ecode": "0703320000020002",
          "intro": "The RFID-tag on AMS4 Slot3 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0703330000020002",
          "intro": "The RFID-tag on AMS4 Slot4 is damaged or the it's content cannot be identified."
        },
        {
          "ecode": "0703350000010001",
          "intro": "The temperature and humidity sensor has an error. The chip may be faulty."
        },
        {
          "ecode": "0C00010000010001",
          "intro": "The Micro Lidar camera is offline. Please check the hardware connection."
        },
        {
          "ecode": "0C00010000010003",
          "intro": "Synchronization between the Micro Lidar camera and MCU is abnormal. Please restart your printer."
        },
        {
          "ecode": "0C00010000010004",
          "intro": "The Micro Lidar camera lens seems to be dirty. Please clean the lens."
        },
        {
          "ecode": "0C00010000010005",
          "intro": "Micro Lidar camera OTP parameter is abnormal. Please contact after-sales."
        },
        {
          "ecode": "0C00010000010009",
          "intro": "The chamber camera lens seems to be dirty. Please clean the lens."
        },
        {
          "ecode": "0C00010000020002",
          "intro": "The Micro Lidar camera is malfunctioning and related functions may fail. Please contact after-sales if this message keeps appearing in multiple prints."
        },
        {
          "ecode": "0C00010000020006",
          "intro": "Micro Lidar camera extrinsic parameters are abnormal. Please enable flowrate calibration in your next print."
        },
        {
          "ecode": "0C00010000020007",
          "intro": "Micro Lidar laser parameters are drifted. Please re-calibrate your printer."
        },
        {
          "ecode": "0C00010000020008",
          "intro": "Failed to get image from chamber camera. Spaghetti and excess chute pileup detection is not available for now."
        },
        {
          "ecode": "0C00020000010001",
          "intro": "The horizontal laser is not lit. Please check if it's covered or hardware connection is normal."
        },
        {
          "ecode": "0C00020000010005",
          "intro": "A new Micro Lidar was detected. Please calibrate it on Calibration page before use."
        },
        {
          "ecode": "0C00020000020002",
          "intro": "The horizontal laser line is too wide. Please check if the heatbed is dirty."
        },
        {
          "ecode": "0C00020000020003",
          "intro": "The horizontal laser is not bright enough at homing position. Please clean or replace heatbed if this message appears repeatedly."
        },
        {
          "ecode": "0C00020000020004",
          "intro": "Nozzle height seems too low. Please check if the nozzle is worn or tilted. Re-calibrate Lidar if the nozzle has been replaced."
        },
        {
          "ecode": "0C00020000020006",
          "intro": "Nozzle height seems too high. Please check if there is filament residual attached to the nozzle."
        },
        {
          "ecode": "0C00030000010009",
          "intro": "The first layer inspection module rebooted abnormally. The inspection result may be inaccurate."
        },
        {
          "ecode": "0C0003000001000a",
          "intro": "Your printer is in factory mode. Please contact Technical Support."
        },
        {
          "ecode": "0C00030000020001",
          "intro": "Filament exposure metering failed because laser reflection is too weak on this material. First layer inspection may be inaccurate."
        },
        {
          "ecode": "0C00030000020002",
          "intro": "First layer inspection terminated due to abnormal Lidar data."
        },
        {
          "ecode": "0C00030000020004",
          "intro": "First layer inspection is not supported for the current print job."
        },
        {
          "ecode": "0C00030000020005",
          "intro": "First layer inspection timed out abnormally, and the current results may be inaccurate."
        },
        {
          "ecode": "0C00030000030006",
          "intro": "Purged filament may have piled up in the excess chute. Please check and clean the excess chute."
        },
        {
          "ecode": "0C00030000030007",
          "intro": "Possible first layer defects have been detected. Please check the first layer quality and decide if the job should be stopped."
        },
        {
          "ecode": "0C00030000030008",
          "intro": "Possible spaghetti defects were detected. Please check the print quality and decide if the job should be stopped."
        },
        {
          "ecode": "0C0003000003000b",
          "intro": "Inspecting the first layer: please wait a moment."
        },
        {
          "ecode": "0300010000010006",
          "intro": "The heatbed temperature is abnormal; the sensor may have a short circuit."
        },
        {
          "ecode": "0300010000010007",
          "intro": "The heatbed temperature is abnormal; the sensor may have an open circuit."
        },
        {
          "ecode": "0300020000010006",
          "intro": "The nozzle temperature is abnormal; the sensor may have a short circuit, please check whether the connector is properly plugged."
        },
        {
          "ecode": "0300020000010007",
          "intro": "The nozzle temperature is abnormal; the sensor may have an open circuit."
        },
        {
          "ecode": "03000D000001000B",
          "intro": "The Z axis motor seems to be stuck when moving. Please check if there is any foreign matter on the Z sliders or Z timing belt wheels ."
        },
        {
          "ecode": "0300100000020002",
          "intro": "The resonance frequency of the X axis differs greatly from last calibration. Please clean the carbon rod and rerun the machine calibration afterward."
        },
        {
          "ecode": "0300110000020002",
          "intro": "The resonance frequency of the Y axis differs greatly from the last calibration. Please clean the carbon rod and rerun the machine calibration afterward."
        },
        {
          "ecode": "0C0003000002000c",
          "intro": "The build plate localization marker is not detected. Please check if the build plate is aligned correctly."
        },
        {
          "ecode": "0C0001000001000A",
          "intro": "The Micro Lidar LED may be broken."
        },
        {
          "ecode": "0C00020000020007",
          "intro": "The vertical laser is not lit. Please check if it's covered or hardware connection is normal."
        },
        {
          "ecode": "0C00020000020008",
          "intro": "The vertical laser line is too wide. Please check if the heatbed is dirty."
        },
        {
          "ecode": "0C0003000003000d",
          "intro": "Some objects may have fallen down, or the extruder is not extruding normally. Please check and decide if the printing should be stopped."
        },
        {
          "ecode": "0C0003000003000e",
          "intro": "Your printer seems to be printing without extruding."
        },
        {
          "ecode": "0C0003000003000f",
          "intro": "Your nozzle seems to be covered with jammed or clogged material."
        },
        {
          "ecode": "0300060000010003",
          "intro": "The resistance of Motor-A is abnormal, the motor may have failed."
        },
        {
          "ecode": "0300070000010003",
          "intro": "The resistance of Motor-B is abnormal, the motor may have failed."
        },
        {
          "ecode": "0300080000010003",
          "intro": "The resistance of Motor-Z is abnormal, the motor may have failed."
        },
        {
          "ecode": "0300090000010003",
          "intro": "The resistance of Motor-E is abnormal, the motor may have failed."
        },
        {
          "ecode": "0300130000010001",
          "intro": "The current sensor of Motor-A is abnormal. This may be caused by a failure of the hardware sampling circuit."
        },
        {
          "ecode": "0300140000010001",
          "intro": "The current sensor of Motor-B is abnormal. This may be caused by a failure of the hardware sampling circuit."
        },
        {
          "ecode": "0300150000010001",
          "intro": "The current sensor of Motor-Z is abnormal. This may be caused by a failure of the hardware sampling circuit."
        },
        {
          "ecode": "0300160000010001",
          "intro": "The current sensor of Motor-E is abnormal. This may be caused by a failure of the hardware sampling circuit."
        },
        {
          "ecode": "0701200000030001",
          "intro": "AMS2 Slot1 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0702200000030001",
          "intro": "AMS3 Slot1 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0703200000030001",
          "intro": "AMS4 Slot1 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0701210000030001",
          "intro": "AMS2 Slot2 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0702210000030001",
          "intro": "AMS3 Slot2 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0703210000030001",
          "intro": "AMS4 Slot2 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0701220000030001",
          "intro": "AMS2 Slot3 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0702220000030001",
          "intro": "AMS3 Slot3 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0703220000030001",
          "intro": "AMS4 Slot3 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0700230000030001",
          "intro": "AMS1 Slot4 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0701230000030001",
          "intro": "AMS2 Slot4 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0702230000030001",
          "intro": "AMS3 Slot4 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0703230000030001",
          "intro": "AMS4 Slot4 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0700500000020001",
          "intro": "AMS1 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "0701500000020001",
          "intro": "AMS2 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "0702500000020001",
          "intro": "AMS3 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "0703500000020001",
          "intro": "AMS4 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "0700510000030001",
          "intro": "The AMS is disabled; please load filament from spool holder."
        },
        {
          "ecode": "0500040000020007",
          "intro": "The bed temperature exceeds the filament's vitrification temperature, which may cause a nozzle clog. Please keep the front door of the printer open or lower the bed temperature."
        },
        {
          "ecode": "0C00020000020009",
          "intro": "The vertical laser is not bright enough at homing position. Please clean or replace heatbed if this message appears repeatedly."
        },
        {
          "ecode": "0C0001000001000B",
          "intro": "Failed to calibrate Micro Lidar. Please make sure the calibration chart is clean and not occluded, and run machine calibration again."
        },
        {
          "ecode": "0500030000020010",
          "intro": "forward coredump, it is recovering."
        },
        {
          "ecode": "0500030000020011",
          "intro": "upgrade coredump, it is recovering."
        },
        {
          "ecode": "0500030000020012",
          "intro": "ipcam coredump, it is recovering."
        },
        {
          "ecode": "0500030000020013",
          "intro": "xcam coredump, it is recovering."
        },
        {
          "ecode": "0500030000020014",
          "intro": "bbl_screen coredump, it is recovering."
        },
        {
          "ecode": "0500030000020015",
          "intro": "device_gate coredump, it is recovering."
        },
        {
          "ecode": "0500030000020016",
          "intro": "device_manager coredump, it is recovering."
        },
        {
          "ecode": "0500030000020017",
          "intro": "recorder coredump, it is recovering."
        },
        {
          "ecode": "0500030000020018",
          "intro": "security coredump, it is recovering."
        },
        {
          "ecode": "0300200000010001",
          "intro": "X axis homing abnormal: please check if the tool head is stuck or the carbon rod has too much resistance."
        },
        {
          "ecode": "0300200000010002",
          "intro": "Y axis homing abnormal: please check if the tool head is stuck or the Y carriage has too much resistance."
        },
        {
          "ecode": "0300200000010003",
          "intro": "X axis homing abnormal: the timing belt may be loose."
        },
        {
          "ecode": "0300200000010004",
          "intro": "Y axis homing abnormal: the timing belt may be loose."
        },
        {
          "ecode": "0300400000020001",
          "intro": "Data transmission over the serial port is abnormal; the software system may be faulty."
        },
        {
          "ecode": "0300410000010001",
          "intro": "The system voltage is unstable; triggering the power failure protection function."
        },
        {
          "ecode": "0700400000020004",
          "intro": "The filament buffer signal is abnormal; the spring may be stuck or the filament may be tangle."
        },
        {
          "ecode": "0700600000020001",
          "intro": "The AMS1 slot1 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0701600000020001",
          "intro": "The AMS2 slot1 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0702600000020001",
          "intro": "The AMS3 slot1 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0703600000020001",
          "intro": "The AMS4 slot1 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0700610000020001",
          "intro": "The AMS1 slot2 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0701610000020001",
          "intro": "The AMS2 slot2 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0702610000020001",
          "intro": "The AMS3 slot2 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0703610000020001",
          "intro": "The AMS4 slot2 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0700620000020001",
          "intro": "The AMS1 slot3 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0701620000020001",
          "intro": "The AMS2 slot3 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0702620000020001",
          "intro": "The AMS3 slot3 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0703620000020001",
          "intro": "The AMS4 slot3 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0700630000020001",
          "intro": "The AMS1 slot4 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0701630000020001",
          "intro": "The AMS2 slot4 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0702630000020001",
          "intro": "The AMS3 slot4 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0703630000020001",
          "intro": "The AMS4 slot4 is overloaded. The filament may be tangled or the spool may be stuck."
        },
        {
          "ecode": "0300010000030008",
          "intro": "The temperature of the heated bed exceeds the limit and automatically adjusts to the limit temperature."
        },
        {
          "ecode": "0700200000020004",
          "intro": "AMS1 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "0701200000020004",
          "intro": "AMS2 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "0702200000020004",
          "intro": "AMS3 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "0703200000020004",
          "intro": "AMS4 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "0700210000020004",
          "intro": "AMS1 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "0701210000020004",
          "intro": "AMS2 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "0702210000020004",
          "intro": "AMS3 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "0703210000020004",
          "intro": "AMS4 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "0700220000020004",
          "intro": "AMS1 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "0701220000020004",
          "intro": "AMS2 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "0702220000020004",
          "intro": "AMS3 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "0703220000020004",
          "intro": "AMS4 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "0700230000020004",
          "intro": "AMS1 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "0701230000020004",
          "intro": "AMS2 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "0702230000020004",
          "intro": "AMS3 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "0703230000020004",
          "intro": "AMS4 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "0700200000020005",
          "intro": "AMS1 Slot1 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0701200000020005",
          "intro": "AMS2 Slot1 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0702200000020005",
          "intro": "AMS3 Slot1 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0703200000020005",
          "intro": "AMS4 Slot1 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0700210000020005",
          "intro": "AMS1 Slot2 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0701210000020005",
          "intro": "AMS2 Slot2 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0702210000020005",
          "intro": "AMS3 Slot2 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0703210000020005",
          "intro": "AMS4 Slot2 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0700220000020005",
          "intro": "AMS1 Slot3 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0701220000020005",
          "intro": "AMS2 Slot3 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0702220000020005",
          "intro": "AMS3 Slot3 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0703220000020005",
          "intro": "AMS4 Slot3 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0700230000020005",
          "intro": "AMS1 Slot4 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0701230000020005",
          "intro": "AMS2 Slot4 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0702230000020005",
          "intro": "AMS3 Slot4 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0703230000020005",
          "intro": "AMS4 Slot4 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head."
        },
        {
          "ecode": "0701200000030002",
          "intro": "AMS2 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0702200000030002",
          "intro": "AMS3 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0703200000030002",
          "intro": "AMS4 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0701210000030002",
          "intro": "AMS2 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0702210000030002",
          "intro": "AMS3 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0703210000030002",
          "intro": "AMS4 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0701220000030002",
          "intro": "AMS2 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0702220000030002",
          "intro": "AMS3 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0703220000030002",
          "intro": "AMS4 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0700230000030002",
          "intro": "AMS1 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0701230000030002",
          "intro": "AMS2 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0702230000030002",
          "intro": "AMS3 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0703230000030002",
          "intro": "AMS4 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0700200000030001",
          "intro": "AMS1 Slot1 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0700210000030001",
          "intro": "AMS1 Slot2 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0700220000030001",
          "intro": "AMS1 Slot3 filament has run out. Please wait while old filament is purged."
        },
        {
          "ecode": "0700200000030002",
          "intro": "AMS1 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0700210000030002",
          "intro": "AMS1 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0700220000030002",
          "intro": "AMS1 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "0500030000020020",
          "intro": "Micro SD Card capacity is insufficient to cache print files."
        },
        {
          "ecode": "0500030000010021",
          "intro": "Hardware incompatible, please check the laser."
        },
        {
          "ecode": "0500030000030022",
          "intro": "MicroSD Card performance degradation has been detected. It may affect print jobs, logs, and video records. Please try to format or change the MicroSD card."
        },
        {
          "ecode": "07FF200000020001",
          "intro": "External filament has run out; please load a new filament."
        },
        {
          "ecode": "07FF200000020002",
          "intro": "External filament is missing; please load a new filament."
        },
        {
          "ecode": "07FF200000020004",
          "intro": "Please pull the external filament from the extruder."
        },
        {
          "ecode": "0500040000030008",
          "intro": "The door is detected to be open."
        },
        {
          "ecode": "0500010000030007",
          "intro": "Unable to record time-lapse photography without MicroSD card inserted."
        },
        {
          "ecode": "1200100000010001",
          "intro": "The AMS1 Slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1201100000010001",
          "intro": "The AMS2 Slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1202100000010001",
          "intro": "The AMS3 Slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1203100000010001",
          "intro": "The AMS4 Slot1 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1200110000010001",
          "intro": "The AMS1 Slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1201110000010001",
          "intro": "The AMS2 Slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1202110000010001",
          "intro": "The AMS3 Slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1203110000010001",
          "intro": "The AMS4 Slot2 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1200120000010001",
          "intro": "The AMS1 Slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1201120000010001",
          "intro": "The AMS2 Slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1202120000010001",
          "intro": "The AMS3 Slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1203120000010001",
          "intro": "The AMS4 Slot3 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1200130000010001",
          "intro": "The AMS1 Slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1201130000010001",
          "intro": "The AMS2 Slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1202130000010001",
          "intro": "The AMS3 Slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1203130000010001",
          "intro": "The AMS4 Slot4 motor has slipped. The extrusion wheel may be malfunctioning, or the filament may be too thin."
        },
        {
          "ecode": "1200100000020002",
          "intro": "The AMS1 Slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1201100000020002",
          "intro": "The AMS2 Slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1202100000020002",
          "intro": "The AMS3 Slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1203100000020002",
          "intro": "The AMS4 Slot1 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1200110000020002",
          "intro": "The AMS1 Slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1201110000020002",
          "intro": "The AMS2 Slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1202110000020002",
          "intro": "The AMS3 Slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1203110000020002",
          "intro": "The AMS4 Slot2 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1200120000020002",
          "intro": "The AMS1 Slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1201120000020002",
          "intro": "The AMS2 Slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1202120000020002",
          "intro": "The AMS3 Slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1203120000020002",
          "intro": "The AMS4 Slot3 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1200130000020002",
          "intro": "The AMS1 Slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1201130000020002",
          "intro": "The AMS2 Slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1202130000020002",
          "intro": "The AMS3 Slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1203130000020002",
          "intro": "The AMS4 Slot4 motor is overloaded. The filament may be tangled or stuck."
        },
        {
          "ecode": "1200100000010003",
          "intro": "The AMS1 Slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1201100000010003",
          "intro": "The AMS2 Slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1202100000010003",
          "intro": "The AMS3 Slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1203100000010003",
          "intro": "The AMS4 Slot1 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1200110000010003",
          "intro": "The AMS1 Slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1201110000010003",
          "intro": "The AMS2 Slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1202110000010003",
          "intro": "The AMS3 Slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1203110000010003",
          "intro": "The AMS4 Slot2 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1200120000010003",
          "intro": "The AMS1 Slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1201120000010003",
          "intro": "The AMS2 Slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1202120000010003",
          "intro": "The AMS3 Slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1203120000010003",
          "intro": "The AMS4 Slot3 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1200130000010003",
          "intro": "The AMS1 Slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1201130000010003",
          "intro": "The AMS2 Slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1202130000010003",
          "intro": "The AMS3 Slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1203130000010003",
          "intro": "The AMS4 Slot4 motor torque control is malfunctioning. The current sensor may be faulty."
        },
        {
          "ecode": "1200200000020001",
          "intro": "AMS1 Slot1 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1201200000020001",
          "intro": "AMS2 Slot1 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1202200000020001",
          "intro": "AMS3 Slot1 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1203200000020001",
          "intro": "AMS4 Slot1 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1200210000020001",
          "intro": "AMS1 Slot2 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1201210000020001",
          "intro": "AMS2 Slot2 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1202210000020001",
          "intro": "AMS3 Slot2 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1203210000020001",
          "intro": "AMS4 Slot2 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1200220000020001",
          "intro": "AMS1 Slot3 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1201220000020001",
          "intro": "AMS2 Slot3 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1202220000020001",
          "intro": "AMS3 Slot3 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1203220000020001",
          "intro": "AMS4 Slot3 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1200230000020001",
          "intro": "AMS1 Slot4 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1201230000020001",
          "intro": "AMS2 Slot4 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1202230000020001",
          "intro": "AMS3 Slot4 filament has run out; please insert a new filament."
        },
        {
          "ecode": "1203230000020001",
          "intro": "AMS4 Slot4 filament has run out; please insert a new filament."
        },
        {
          "ecode": "12FF200000020001",
          "intro": "Filament at the spool holder has run out; please insert a new filament."
        },
        {
          "ecode": "1200200000020002",
          "intro": "AMS1 Slot1 is empty; please insert a new filament."
        },
        {
          "ecode": "1201200000020002",
          "intro": "AMS2 Slot1 is empty; please insert a new filament."
        },
        {
          "ecode": "1202200000020002",
          "intro": "AMS3 Slot1 is empty; please insert a new filament."
        },
        {
          "ecode": "1203200000020002",
          "intro": "AMS4 Slot1 is empty; please insert a new filament."
        },
        {
          "ecode": "1200210000020002",
          "intro": "AMS1 Slot2 is empty; please insert a new filament."
        },
        {
          "ecode": "1201210000020002",
          "intro": "AMS2 Slot2 is empty; please insert a new filament."
        },
        {
          "ecode": "1202210000020002",
          "intro": "AMS3 Slot2 is empty; please insert a new filament."
        },
        {
          "ecode": "1203210000020002",
          "intro": "AMS4 Slot2 is empty; please insert a new filament."
        },
        {
          "ecode": "1200220000020002",
          "intro": "AMS1 Slot3 is empty; please insert a new filament."
        },
        {
          "ecode": "1201220000020002",
          "intro": "AMS2 Slot3 is empty; please insert a new filament."
        },
        {
          "ecode": "1202220000020002",
          "intro": "AMS3 Slot3 is empty; please insert a new filament."
        },
        {
          "ecode": "1203220000020002",
          "intro": "AMS4 Slot3 is empty; please insert a new filament."
        },
        {
          "ecode": "1200230000020002",
          "intro": "AMS1 Slot4 is empty; please insert a new filament."
        },
        {
          "ecode": "1201230000020002",
          "intro": "AMS2 Slot4 is empty; please insert a new filament."
        },
        {
          "ecode": "1202230000020002",
          "intro": "AMS3 Slot4 is empty; please insert a new filament."
        },
        {
          "ecode": "1203230000020002",
          "intro": "AMS4 Slot4 is empty; please insert a new filament."
        },
        {
          "ecode": "12FF200000020002",
          "intro": "Filament on the spool holder is empty; please insert a new filament."
        },
        {
          "ecode": "1200200000020003",
          "intro": "AMS1 Slot1 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1201200000020003",
          "intro": "AMS2 Slot1 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1202200000020003",
          "intro": "AMS3 Slot1 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1203200000020003",
          "intro": "AMS4 Slot1 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1200210000020003",
          "intro": "AMS1 Slot2 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1201210000020003",
          "intro": "AMS2 Slot2 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1202210000020003",
          "intro": "AMS3 Slot2 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1203210000020003",
          "intro": "AMS4 Slot2 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1200220000020003",
          "intro": "AMS1 Slot3 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1201220000020003",
          "intro": "AMS2 Slot3 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1202220000020003",
          "intro": "AMS3 Slot3 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1203220000020003",
          "intro": "AMS4 Slot3 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1200230000020003",
          "intro": "AMS1 Slot4 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1201230000020003",
          "intro": "AMS2 Slot4 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1202230000020003",
          "intro": "AMS3 Slot4 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1203230000020003",
          "intro": "AMS4 Slot4 filament may be broken in the PTFE tube."
        },
        {
          "ecode": "1200200000020004",
          "intro": "AMS1 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "1201200000020004",
          "intro": "AMS2 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "1202200000020004",
          "intro": "AMS3 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "1203200000020004",
          "intro": "AMS4 Slot1 filament may be broken in the tool head."
        },
        {
          "ecode": "1200210000020004",
          "intro": "AMS1 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "1201210000020004",
          "intro": "AMS2 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "1202210000020004",
          "intro": "AMS3 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "1203210000020004",
          "intro": "AMS4 Slot2 filament may be broken in the tool head."
        },
        {
          "ecode": "1200220000020004",
          "intro": "AMS1 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "1201220000020004",
          "intro": "AMS2 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "1202220000020004",
          "intro": "AMS3 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "1203220000020004",
          "intro": "AMS4 Slot3 filament may be broken in the tool head."
        },
        {
          "ecode": "1200230000020004",
          "intro": "AMS1 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "1201230000020004",
          "intro": "AMS2 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "1202230000020004",
          "intro": "AMS3 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "1203230000020004",
          "intro": "AMS4 Slot4 filament may be broken in the tool head."
        },
        {
          "ecode": "12FF200000020004",
          "intro": "Please pull out the filament on the spool holder from the extruder."
        },
        {
          "ecode": "1200200000020005",
          "intro": "AMS1 Slot1 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1201200000020005",
          "intro": "AMS2 Slot1 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1202200000020005",
          "intro": "AMS3 Slot1 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1203200000020005",
          "intro": "AMS4 Slot1 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1200210000020005",
          "intro": "AMS1 Slot2 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1201210000020005",
          "intro": "AMS2 Slot2 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1202210000020005",
          "intro": "AMS3 Slot2 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1203210000020005",
          "intro": "AMS4 Slot2 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1200220000020005",
          "intro": "AMS1 Slot3 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1201220000020005",
          "intro": "AMS2 Slot3 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1202220000020005",
          "intro": "AMS3 Slot3 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1203220000020005",
          "intro": "AMS4 Slot3 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1200230000020005",
          "intro": "AMS1 Slot4 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1201230000020005",
          "intro": "AMS2 Slot4 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1202230000020005",
          "intro": "AMS3 Slot4 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1203230000020005",
          "intro": "AMS4 Slot4 filament has run out, and purging the old filament went abnormally; please check to see if filament is stuck in the toolhead."
        },
        {
          "ecode": "1200200000030001",
          "intro": "AMS1 Slot1 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1201200000030001",
          "intro": "AMS2 Slot1 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1202200000030001",
          "intro": "AMS3 Slot1 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1203200000030001",
          "intro": "AMS4 Slot1 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1200210000030001",
          "intro": "AMS1 Slot2 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1201210000030001",
          "intro": "AMS2 Slot2 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1202210000030001",
          "intro": "AMS3 Slot2 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1203210000030001",
          "intro": "AMS4 Slot2 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1200220000030001",
          "intro": "AMS1 Slot3 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1201220000030001",
          "intro": "AMS2 Slot3 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1202220000030001",
          "intro": "AMS3 Slot3 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1203220000030001",
          "intro": "AMS4 Slot3 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1200230000030001",
          "intro": "AMS1 Slot4 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1201230000030001",
          "intro": "AMS2 Slot4 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1202230000030001",
          "intro": "AMS3 Slot4 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1203230000030001",
          "intro": "AMS4 Slot4 filament has run out. Purging the old filament; please wait."
        },
        {
          "ecode": "1200200000030002",
          "intro": "AMS1 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1201200000030002",
          "intro": "AMS2 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1202200000030002",
          "intro": "AMS3 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1203200000030002",
          "intro": "AMS4 Slot1 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1200210000030002",
          "intro": "AMS1 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1201210000030002",
          "intro": "AMS2 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1202210000030002",
          "intro": "AMS3 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1203210000030002",
          "intro": "AMS4 Slot2 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1200220000030002",
          "intro": "AMS1 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1201220000030002",
          "intro": "AMS2 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1202220000030002",
          "intro": "AMS3 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1203220000030002",
          "intro": "AMS4 Slot3 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1200230000030002",
          "intro": "AMS1 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1201230000030002",
          "intro": "AMS2 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1202230000030002",
          "intro": "AMS3 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1203230000030002",
          "intro": "AMS4 Slot4 filament has run out and automatically switched to the slot with the same filament."
        },
        {
          "ecode": "1200240000020001",
          "intro": "Filament may be broken in the tool head."
        },
        {
          "ecode": "1200250000020001",
          "intro": "Failed to extrude the filament and the extruder may be clogged."
        },
        {
          "ecode": "1200300000010001",
          "intro": "AMS1 Slot1 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1201300000010001",
          "intro": "AMS2 Slot1 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1202300000010001",
          "intro": "AMS3 Slot1 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1203300000010001",
          "intro": "AMS4 Slot1 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1200310000010001",
          "intro": "AMS1 Slot2 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1201310000010001",
          "intro": "AMS2 Slot2 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1202310000010001",
          "intro": "AMS3 Slot2 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1203310000010001",
          "intro": "AMS4 Slot2 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1200320000010001",
          "intro": "AMS1 Slot3 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1201320000010001",
          "intro": "AMS2 Slot3 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1202320000010001",
          "intro": "AMS3 Slot3 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1203320000010001",
          "intro": "AMS4 Slot3 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1200330000010001",
          "intro": "AMS1 Slot4 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1201330000010001",
          "intro": "AMS2 Slot4 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1202330000010001",
          "intro": "AMS3 Slot4 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1203330000010001",
          "intro": "AMS4 Slot4 RFID coil is broken or the RF hardware circuit has an error."
        },
        {
          "ecode": "1200300000020002",
          "intro": "The RFID-tag on AMS1 Slot1 is damaged."
        },
        {
          "ecode": "1201300000020002",
          "intro": "The RFID-tag on AMS2 Slot1 is damaged."
        },
        {
          "ecode": "1202300000020002",
          "intro": "The RFID-tag on AMS3 Slot1 is damaged."
        },
        {
          "ecode": "1203300000020002",
          "intro": "The RFID-tag on AMS4 Slot1 is damaged."
        },
        {
          "ecode": "1200310000020002",
          "intro": "The RFID-tag on AMS1 Slot2 is damaged."
        },
        {
          "ecode": "1201310000020002",
          "intro": "The RFID-tag on AMS2 Slot2 is damaged."
        },
        {
          "ecode": "1202310000020002",
          "intro": "The RFID-tag on AMS3 Slot2 is damaged."
        },
        {
          "ecode": "1203310000020002",
          "intro": "The RFID-tag on AMS4 Slot2 is damaged."
        },
        {
          "ecode": "1200320000020002",
          "intro": "The RFID-tag on AMS1 Slot3 is damaged."
        },
        {
          "ecode": "1201320000020002",
          "intro": "The RFID-tag on AMS2 Slot3 is damaged."
        },
        {
          "ecode": "1202320000020002",
          "intro": "The RFID-tag on AMS3 Slot3 is damaged."
        },
        {
          "ecode": "1203320000020002",
          "intro": "The RFID-tag on AMS4 Slot3 is damaged."
        },
        {
          "ecode": "1200330000020002",
          "intro": "The RFID-tag on AMS1 Slot4 is damaged."
        },
        {
          "ecode": "1201330000020002",
          "intro": "The RFID-tag on AMS2 Slot4 is damaged."
        },
        {
          "ecode": "1202330000020002",
          "intro": "The RFID-tag on AMS3 Slot4 is damaged."
        },
        {
          "ecode": "1203330000020002",
          "intro": "The RFID-tag on AMS4 Slot4 is damaged."
        },
        {
          "ecode": "1200300000030003",
          "intro": "AMS1 Slot1 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1201300000030003",
          "intro": "AMS2 Slot1 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1202300000030003",
          "intro": "AMS3 Slot1 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1203300000030003",
          "intro": "AMS4 Slot1 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1200310000030003",
          "intro": "AMS1 Slot2 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1201310000030003",
          "intro": "AMS2 Slot2 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1202310000030003",
          "intro": "AMS3 Slot2 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1203310000030003",
          "intro": "AMS4 Slot2 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1200320000030003",
          "intro": "AMS1 Slot3 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1201320000030003",
          "intro": "AMS2 Slot3 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1202320000030003",
          "intro": "AMS3 Slot3 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1203320000030003",
          "intro": "AMS4 Slot3 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1200330000030003",
          "intro": "AMS1 Slot4 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1201330000030003",
          "intro": "AMS2 Slot4 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1202330000030003",
          "intro": "AMS3 Slot4 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1203330000030003",
          "intro": "AMS4 Slot4 RFID cannot be read because of a structural error."
        },
        {
          "ecode": "1200300000010004",
          "intro": "RFID cannot be read because of an encryption chip failure in AMS1."
        },
        {
          "ecode": "1201300000010004",
          "intro": "RFID cannot be read because of an encryption chip failure in AMS2."
        },
        {
          "ecode": "1202300000010004",
          "intro": "RFID cannot be read because of an encryption chip failure in AMS3."
        },
        {
          "ecode": "1203300000010004",
          "intro": "RFID cannot be read because of an encryption chip failure in AMS4."
        },
        {
          "ecode": "1200450000020001",
          "intro": "The filament cutter sensor is malfunctioning. Please check whether the connector is properly plugged in."
        },
        {
          "ecode": "1200450000020002",
          "intro": "The filament cutter's cutting distance is too large. The X motor may lose steps."
        },
        {
          "ecode": "1200450000020003",
          "intro": "The filament cutter handle has not released. The handle or blade may be stuck."
        },
        {
          "ecode": "1200500000020001",
          "intro": "AMS1 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "1201500000020001",
          "intro": "AMS2 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "1202500000020001",
          "intro": "AMS3 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "1203500000020001",
          "intro": "AMS4 communication is abnormal; please check the connection cable."
        },
        {
          "ecode": "1200510000030001",
          "intro": "AMS is disabled; please load filament from spool holder."
        },
        {
          "ecode": "1200700000010001",
          "intro": "AMS1 Filament speed and length error: The slot 1 filament odometry may be faulty."
        },
        {
          "ecode": "1201700000010001",
          "intro": "AMS2 Filament speed and length error: The slot 1 filament odometry may be faulty."
        },
        {
          "ecode": "1202700000010001",
          "intro": "AMS3 Filament speed and length error: The slot 1 filament odometry may be faulty."
        },
        {
          "ecode": "1203700000010001",
          "intro": "AMS4 Filament speed and length error: The slot 1 filament odometry may be faulty."
        },
        {
          "ecode": "1200710000010001",
          "intro": "AMS1 Filament speed and length error: The slot 2 filament odometry may be faulty."
        },
        {
          "ecode": "1201710000010001",
          "intro": "AMS2 Filament speed and length error: The slot 2 filament odometry may be faulty."
        },
        {
          "ecode": "1202710000010001",
          "intro": "AMS3 Filament speed and length error: The slot 2 filament odometry may be faulty."
        },
        {
          "ecode": "1203710000010001",
          "intro": "AMS4 Filament speed and length error: The slot 2 filament odometry may be faulty."
        },
        {
          "ecode": "1200720000010001",
          "intro": "AMS1 Filament speed and length error: The slot 3 filament odometry may be faulty."
        },
        {
          "ecode": "1201720000010001",
          "intro": "AMS2 Filament speed and length error: The slot 3 filament odometry may be faulty."
        },
        {
          "ecode": "1202720000010001",
          "intro": "AMS3 Filament speed and length error: The slot 3 filament odometry may be faulty."
        },
        {
          "ecode": "1203720000010001",
          "intro": "AMS4 Filament speed and length error: The slot 3 filament odometry may be faulty."
        },
        {
          "ecode": "1200730000010001",
          "intro": "AMS1 Filament speed and length error: The slot 4 filament odometry may be faulty."
        },
        {
          "ecode": "1201730000010001",
          "intro": "AMS2 Filament speed and length error: The slot 4 filament odometry may be faulty."
        },
        {
          "ecode": "1202730000010001",
          "intro": "AMS3 Filament speed and length error: The slot 4 filament odometry may be faulty."
        },
        {
          "ecode": "1203730000010001",
          "intro": "AMS4 Filament speed and length error: The slot 4 filament odometry may be faulty."
        },
        {
          "ecode": "12FF200000020005",
          "intro": "Filament may be broken in the tool head."
        },
        {
          "ecode": "12FF200000020006",
          "intro": "Failed to extrude the filament and the extruder may be clogged."
        },
        {
          "ecode": "0C0003000002000F",
          "intro": "Parts skip setted before first layer inspection, the inspection will not be supported for the current print job."
        },
        {
          "ecode": "0500040000020010",
          "intro": "The RFID-tag on AMS1 Slot1 cannot be identified."
        },
        {
          "ecode": "0500040000020011",
          "intro": "The RFID-tag on AMS1 Slot2 cannot be identified."
        },
        {
          "ecode": "0500040000020012",
          "intro": "The RFID-tag on AMS1 Slot3 cannot be identified."
        },
        {
          "ecode": "0500040000020014",
          "intro": "The RFID-tag on AMS2 Slot1 cannot be identified."
        },
        {
          "ecode": "0500040000020015",
          "intro": "The RFID-tag on AMS2 Slot2 cannot be identified."
        },
        {
          "ecode": "0500040000020016",
          "intro": "The RFID-tag on AMS2 Slot3 cannot be identified."
        },
        {
          "ecode": "0500040000020017",
          "intro": "The RFID-tag on AMS2 Slot4 cannot be identified."
        },
        {
          "ecode": "0500040000020018",
          "intro": "The RFID-tag on AMS3 Slot1 cannot be identified."
        },
        {
          "ecode": "0500040000020019",
          "intro": "The RFID-tag on AMS3 Slot2 cannot be identified."
        },
        {
          "ecode": "050004000002001A",
          "intro": "The RFID-tag on AMS3 Slot3 cannot be identified."
        },
        {
          "ecode": "050004000002001B",
          "intro": "The RFID-tag on AMS3 Slot4 cannot be identified."
        },
        {
          "ecode": "050004000002001C",
          "intro": "The RFID-tag on AMS4 Slot1 cannot be identified."
        },
        {
          "ecode": "050004000002001D",
          "intro": "The RFID-tag on AMS4 Slot2 cannot be identified."
        },
        {
          "ecode": "050004000002001E",
          "intro": "The RFID-tag on AMS4 Slot3 cannot be identified."
        },
        {
          "ecode": "050004000002001F",
          "intro": "The RFID-tag on AMS4 Slot4 cannot be identified."
        },
        {
          "ecode": "0500040000020013",
          "intro": "The RFID-tag on AMS1 Slot4 cannot be identified."
        },
        {
          "ecode": "12FF800000020001",
          "intro": "The filament on the spool holder may be tangled or stuck."
        },
        {
          "ecode": "1200800000020001",
          "intro": "AMS1 Slot1 filament may be tangled or stuck."
        },
        {
          "ecode": "1200810000020001",
          "intro": "AMS1 Slot2 filament may be tangled or stuck."
        },
        {
          "ecode": "1200820000020001",
          "intro": "AMS1 Slot3 filament may be tangled or stuck."
        },
        {
          "ecode": "1200830000020001",
          "intro": "AMS1 Slot4 filament may be tangled or stuck."
        },
        {
          "ecode": "1201800000020001",
          "intro": "AMS2 Slot1 filament may be tangled or stuck."
        },
        {
          "ecode": "1201810000020001",
          "intro": "AMS2 Slot2 filament may be tangled or stuck."
        },
        {
          "ecode": "1201820000020001",
          "intro": "AMS2 Slot3 filament may be tangled or stuck."
        },
        {
          "ecode": "1201830000020001",
          "intro": "AMS2 Slot4 filament may be tangled or stuck."
        },
        {
          "ecode": "1202800000020001",
          "intro": "AMS3 Slot1 filament may be tangled or stuck."
        },
        {
          "ecode": "1202810000020001",
          "intro": "AMS3 Slot2 filament may be tangled or stuck."
        },
        {
          "ecode": "1202820000020001",
          "intro": "AMS3 Slot3 filament may be tangled or stuck."
        },
        {
          "ecode": "1202830000020001",
          "intro": "AMS3 Slot4 filament may be tangled or stuck."
        },
        {
          "ecode": "1203800000020001",
          "intro": "AMS4 Slot1 filament may be tangled or stuck."
        },
        {
          "ecode": "1203810000020001",
          "intro": "AMS4 Slot2 filament may be tangled or stuck."
        },
        {
          "ecode": "1203820000020001",
          "intro": "AMS4 Slot3 filament may be tangled or stuck."
        },
        {
          "ecode": "1203830000020001",
          "intro": "AMS4 Slot4 filament may be tangled or stuck."
        },
        {
          "ecode": "0300170000010001",
          "intro": "The speed of the hotend fan is too slow or stopped. It may be stuck or the connector may not be plugged in properly."
        },
        {
          "ecode": "0300170000020002",
          "intro": "The speed of the hotend fan is slow. It may be stuck and need cleaning."
        },
        {
          "ecode": "0300900000010001",
          "intro": "Chamber heating failed. The chamber heater may be failing to blow hot air."
        },
        {
          "ecode": "0300900000010002",
          "intro": "Chamber heating failed. The chamber may not be enclosed, or the ambient temperature may be too low, or the heat dissipation vent of the power supply may be blocked."
        },
        {
          "ecode": "0300900000010003",
          "intro": "Chamber heating failed. The temperature of power supply may be too high."
        },
        {
          "ecode": "0300900000010004",
          "intro": "Chamber heating failed. The speed of the heating fan is too low."
        },
        {
          "ecode": "0300900000010005",
          "intro": "Chamber heating failed. The thermal resistance is too high."
        },
        {
          "ecode": "0300910000010001",
          "intro": "The temperature of chamber heater 1 is abnormal. The heater may have a short circuit."
        },
        {
          "ecode": "0300910000010002",
          "intro": "The temperature of chamber heater 1 is abnormal. The heater may have an open circuit or the thermal fuse may have taken effect."
        },
        {
          "ecode": "0300910000010003",
          "intro": "The temperature of chamber heater 1 is abnormal. The heater is over temperature."
        },
        {
          "ecode": "0300910000010006",
          "intro": "The temperature of chamber heater 1 is abnormal. The sensor may have a short circuit."
        },
        {
          "ecode": "0300910000010007",
          "intro": "The temperature of chamber heater 1 is abnormal. The sensor may have an open circuit."
        },
        {
          "ecode": "0300910000010008",
          "intro": "Chamber heater 1 failed to rise to target temperature."
        },
        {
          "ecode": "0300920000010001",
          "intro": "The temperature of chamber heater 2 is abnormal. The heater may have a short circuit."
        },
        {
          "ecode": "0300920000010002",
          "intro": "The temperature of chamber heater 2 is abnormal. The heater may have an open circuit or the thermal fuse may be in effect."
        },
        {
          "ecode": "0300920000010003",
          "intro": "The temperature of chamber heater 2 is abnormal. The heater is over temperature."
        },
        {
          "ecode": "0300920000010006",
          "intro": "The temperature of chamber heater 2 is abnormal. The sensor may have a short circuit."
        },
        {
          "ecode": "0300920000010007",
          "intro": "The temperature of chamber heater 2 is abnormal. The sensor may have an open circuit."
        },
        {
          "ecode": "0300920000010008",
          "intro": "Chamber heater 2 failed to rise to target temperature."
        },
        {
          "ecode": "0300930000010001",
          "intro": "Chamber temperature is abnormal. The chamber heater's temperature sensor may have a short circuit."
        },
        {
          "ecode": "0300930000010002",
          "intro": "Chamber temperature is abnormal. The chamber heater's temperature sensor may have an open circuit."
        },
        {
          "ecode": "0300930000010003",
          "intro": "Chamber temperature is abnormal. The chamber heater's temperature sensor at the air outlet may have a short circuit."
        },
        {
          "ecode": "0300930000010004",
          "intro": "Chamber temperature is abnormal. The chamber heater's temperature sensor at the air outlet may have an open circuit."
        },
        {
          "ecode": "0300930000010005",
          "intro": "Chamber temperature is abnormal. The chamber heater's temperature sensor at the air inlet may have a short circuit."
        },
        {
          "ecode": "0300930000010006",
          "intro": "Chamber temperature is abnormal. The chamber heater's temperature sensor at the air inlet may have an open circuit."
        },
        {
          "ecode": "0300930000010007",
          "intro": "Chamber temperature is abnormal. The temperature sensor at the power supply may have a short circuit."
        },
        {
          "ecode": "0300930000010008",
          "intro": "Chamber temperature is abnormal. The temperature sensor at power supply may have an open circuit."
        },
        {
          "ecode": "0500030000010023",
          "intro": "The CTC module is malfunctioning. Please restart the device."
        },
        {
          "ecode": "0300900000010010",
          "intro": "The communication of chamber temperature controller is abnormal."
        },
        {
          "ecode": "12FF200000030007",
          "intro": "Checking the filament location of all AMS slots, please wait."
        },
        {
          "ecode": "0500040000020020",
          "intro": ""
        },
        {
          "ecode": "0300940000030001",
          "intro": "Chamber cooling may be too slow. You can open the chamber to help cooling if the gas in chamber is non-toxic."
        },
        {
          "ecode": "0300180000010001",
          "intro": "The value of extrusion force sensor is low, the nozzle seems to not be installed."
        },
        {
          "ecode": "0300180000010003",
          "intro": "The extrusion force sensor is not available, the link between the MC and TH may be broken or the sensor is broken."
        },
        {
          "ecode": "0300180000010004",
          "intro": "The data from extrusion force sensor is abnormal, the sensor should be broken."
        },
        {
          "ecode": "0300190000010001",
          "intro": "The eddy current sensor on Y-axis is not available, the wire should be broken."
        },
        {
          "ecode": "0300190000020002",
          "intro": "The sensitivity of Y-axis eddy current sensor is too low."
        },
        {
          "ecode": "0300940000030002",
          "intro": "Chamber temperature setting value exceed the limit, the boundary value will be set."
        },
        {
          "ecode": "12FF200000020007",
          "intro": "Failed to check the filament location in the tool head; please click for more help."
        },
        {
          "ecode": "0300180000010002",
          "intro": "The sensitivity of the extrusion force sensor is low, the hotend may not installed correctly."
        },
        {
          "ecode": "03001A0000020001",
          "intro": "The nozzle is covered with filaments, or the build plate is put in crooked."
        },
        {
          "ecode": "03001A0000020002",
          "intro": "The nozzle is clogged with filament."
        },
        {
          "ecode": "1200200000020006",
          "intro": "Failed to extrude AMS1 Slot1 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1201200000020006",
          "intro": "Failed to extrude AMS2 Slot1 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1202200000020006",
          "intro": "Failed to extrude AMS3 Slot1 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1203200000020006",
          "intro": "Failed to extrude AMS4 Slot1 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1200210000020006",
          "intro": "Failed to extrude AMS1 Slot2 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1201210000020006",
          "intro": "Failed to extrude AMS2 Slot2 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1202210000020006",
          "intro": "Failed to extrude AMS3 Slot2 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1203210000020006",
          "intro": "Failed to extrude AMS4 Slot2 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1200220000020006",
          "intro": "Failed to extrude AMS1 Slot3 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1201220000020006",
          "intro": "Failed to extrude AMS2 Slot3 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1202220000020006",
          "intro": "Failed to extrude AMS3 Slot3 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1203220000020006",
          "intro": "Failed to extrude AMS4 Slot3 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1200230000020006",
          "intro": "Failed to extrude AMS1 Slot4 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1201230000020006",
          "intro": "Failed to extrude AMS2 Slot4 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1202230000020006",
          "intro": "Failed to extrude AMS3 Slot4 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "1203230000020006",
          "intro": "Failed to extrude AMS4 Slot4 filament; the extruder may be clogged or the filament may be too thin, causing the extruder to slip."
        },
        {
          "ecode": "0300020000010009",
          "intro": "The nozzle temperature control is abnormal; the hot end may not be installed. If you want to heat the hot end without it being installed, please turn on maintenance mode on the settings page."
        },
        {
          "ecode": "0300940000020003",
          "intro": "Chamber failed to reach the desired temperature. The machine will stop waiting for the chamber temperature."
        },
        {
          "ecode": "0C00030000020010",
          "intro": "Foreign objects detected on hotbed, Please check and clean the hotbed."
        },
        {
          "ecode": "0500050000010001",
          "intro": "The factory data of AP board is abnormal, please replace the AP board with a new one."
        }
      ]
    },
    "device_error": {
      "ver": 202311050300,
      "en": [
        {
          "ecode": "03004000",
          "intro": "Homing Z axis failed."
        },
        {
          "ecode": "03004001",
          "intro": "The printer timed out waiting for the nozzle to cool down before homing."
        },
        {
          "ecode": "03004002",
          "intro": "Mesh bed leveling failed."
        },
        {
          "ecode": "03004003",
          "intro": "Nozzle temperature malfunction."
        },
        {
          "ecode": "03004004",
          "intro": "Heatbed temperature malfunction."
        },
        {
          "ecode": "03004005",
          "intro": "The heatbreak fan speed is abnormal."
        },
        {
          "ecode": "03004006",
          "intro": "The nozzle is clogged."
        },
        {
          "ecode": "03004008",
          "intro": "The AMS failed to change filament."
        },
        {
          "ecode": "03004009",
          "intro": "Homing XY axis failed."
        },
        {
          "ecode": "0300400A",
          "intro": "Mechanical resonance frequency identification failed."
        },
        {
          "ecode": "0300400B",
          "intro": "Internal communication exception."
        },
        {
          "ecode": "0300400C",
          "intro": "Printing was cancelled."
        },
        {
          "ecode": "0300400D",
          "intro": "Resume failed after power loss."
        },
        {
          "ecode": "03008000",
          "intro": "Printing was paused for unknown reason. You can tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008001",
          "intro": "Printing was paused by the user. You can tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008002",
          "intro": "First layer defects were detected. If the defects are acceptable, tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008003",
          "intro": "Spaghetti defects were detected. If the defects are acceptable, tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008004",
          "intro": "The filament ran out. Please load new filament in Temperature/Axis and tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008005",
          "intro": "Printing was paused because the front cover of tool head fell off. Please mount it back and tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008006",
          "intro": "Build plate localization marker was not found. Please stop the print job and find the build plate. You can also tap \"Resume\" to force-resume the print job."
        },
        {
          "ecode": "05004001",
          "intro": "Failed to connect to Bambu Cloud. Please check your network connection."
        },
        {
          "ecode": "05004002",
          "intro": "Unsupported print file path or name. Please resend the printing job."
        },
        {
          "ecode": "05004003",
          "intro": "There was a problem parsing gcode.3mf. Please resend the printing job."
        },
        {
          "ecode": "05004004",
          "intro": "Printing jobs are not allowed to be sent while printing."
        },
        {
          "ecode": "05004005",
          "intro": "Print jobs are not allowed to be sent while updating firmware."
        },
        {
          "ecode": "05004006",
          "intro": "There is not enough free storage space for the print job. Restoring to factory settings can release available space."
        },
        {
          "ecode": "05004007",
          "intro": "Print jobs are not allowed to be sent while force updating or when repair updating is required."
        },
        {
          "ecode": "05004008",
          "intro": "Starting printing failed. please power cycle the printer and resend the print job."
        },
        {
          "ecode": "07008001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "07008003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008004",
          "intro": "Failed to pull back the filament from the toolhead to AMS. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008005",
          "intro": "Failed to feed the filament outside the AMS. Please clip the end of the filament flat and check to see if the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008007",
          "intro": "Failed to extrude the filament. Please check if the extruder is clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008010",
          "intro": "AMS assist motor is overloaded. Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07008011",
          "intro": "AMS filament ran out. Please put a new filament into AMS and click the \"Retry\" button."
        },
        {
          "ecode": "07018001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "07018003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018004",
          "intro": "Failed to pull back the filament from the toolhead to AMS. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018005",
          "intro": "Failed to feed the filament outside the AMS. Please clip the end of the filament flat and check to see if the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018007",
          "intro": "Failed to extrude the filament. Please check if the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018010",
          "intro": "AMS assist motor is overloaded. Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018011",
          "intro": "AMS filament ran out. Please put a new filament into AMS and click the \"Retry\" button."
        },
        {
          "ecode": "07028001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "07028003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028004",
          "intro": "Failed to pull back the filament from the toolhead to AMS. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028005",
          "intro": "Failed to feed the filament outside the AMS. Please clip the end of the filament flat and check to see if the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028007",
          "intro": "Failed to extrude the filament. Please check if the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028010",
          "intro": "AMS assist motor is overloaded. Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028011",
          "intro": "AMS filament ran out. Please put a new filament into AMS and click the \"Retry\" button."
        },
        {
          "ecode": "07038001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "07038003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038004",
          "intro": "Failed to pull back the filament from the toolhead to AMS. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038005",
          "intro": "Failed to feed the filament outside the AMS. Please clip the end of the filament flat and check to see if the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038007",
          "intro": "Failed to extrude the filament. Please check if the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038010",
          "intro": "AMS assist motor is overloaded. Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038011",
          "intro": "AMS filament ran out. Please put a new filament into AMS and click the \"Retry\" button."
        },
        {
          "ecode": "0C008001",
          "intro": "First layer defects were detected. If the defects are acceptable, click \"Resume\" button to resume the print job."
        },
        {
          "ecode": "0C008002",
          "intro": "Spaghetti failure was detected."
        },
        {
          "ecode": "0C00C003",
          "intro": "Possible defects were detected in the first layer."
        },
        {
          "ecode": "0C00C004",
          "intro": "Possible spaghetti failure was detected."
        },
        {
          "ecode": "03008007",
          "intro": "There was an unfinished print job when the printer powered off. Tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008008",
          "intro": "Nozzle temperature malfunction."
        },
        {
          "ecode": "03008009",
          "intro": "Heatbed temperature malfunction."
        },
        {
          "ecode": "05004009",
          "intro": "Print jobs are not allowed to be sent while updating logs."
        },
        {
          "ecode": "0500400A",
          "intro": "The file name is not supported. Please rename and restart the printing job."
        },
        {
          "ecode": "0300800A",
          "intro": "Purged filaments have piled up in excess chute, which may cause a tool head collision. Please clean the filament. If cleaned or acceptable, tap the resume button to resume the print job."
        },
        {
          "ecode": "0C008005",
          "intro": "Purged filament has piled up in the excess chute, which may cause a tool head collision."
        },
        {
          "ecode": "0C00C006",
          "intro": "Purged filament may have piled up in the excess chute."
        },
        {
          "ecode": "0300400E",
          "intro": "The motor self-check failed."
        },
        {
          "ecode": "0300800B",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the resume button."
        },
        {
          "ecode": "07008012",
          "intro": "Failed to get AMS mapping table; please click \"Retry\" to continue."
        },
        {
          "ecode": "07018012",
          "intro": "Failed to get AMS mapping table; please click \"Retry\" to continue."
        },
        {
          "ecode": "07028012",
          "intro": "Failed to get AMS mapping table; please click \"Retry\" to continue."
        },
        {
          "ecode": "07038012",
          "intro": "Failed to get AMS mapping table; please click \"Retry\" to continue."
        },
        {
          "ecode": "07008013",
          "intro": "Timeout purging old filament: Please check if the filament is stuck or the extruder is clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07018013",
          "intro": "Timeout purging old filament: Please check if the filament is stuck or the extruder is clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07028013",
          "intro": "Timeout purging old filament: Please check if the filament is stuck or the extruder is clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07038013",
          "intro": "Timeout purging old filament: Please check if the filament is stuck or the extruder is clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07004001",
          "intro": "Filament is still loaded from the AMS after it has been disabled. Please unload the filament, load from the spool holder, and restart printing."
        },
        {
          "ecode": "07014001",
          "intro": "Filament is still loaded from the AMS after it has been disabled. Please unload the filament, load from the spool holder, and restart printing."
        },
        {
          "ecode": "07024001",
          "intro": "Filament is still loaded from the AMS after it has been disabled. Please unload the filament, load from the spool holder, and restart printing."
        },
        {
          "ecode": "07034001",
          "intro": "Filament is still loaded from the AMS after it has been disabled. Please unload the filament, load from the spool holder, and restart printing."
        },
        {
          "ecode": "0500400B",
          "intro": "There was a problem downloading a file. Please check you network connection and resend the printing job."
        },
        {
          "ecode": "1000C001",
          "intro": "High bed temperature may lead to filament clogging in the nozzle. Please ensure ventilation for the printer."
        },
        {
          "ecode": "1000C002",
          "intro": "Printing CF material with stainless steel may cause nozzle damage."
        },
        {
          "ecode": "0500400C",
          "intro": "Please insert a MicroSD card and restart the printing job."
        },
        {
          "ecode": "0500400D",
          "intro": "Please run a self-test and restart the printing job."
        },
        {
          "ecode": "0300800C",
          "intro": "Skipping step detected, auto-recover complete; please resume print and check if there are any layer shift problems."
        },
        {
          "ecode": "0C008009",
          "intro": "Build plate localization marker was not found."
        },
        {
          "ecode": "0500400E",
          "intro": "Printing was cancelled."
        },
        {
          "ecode": "0300800D",
          "intro": "Some objects have fallen down, or the extruder is not extruding normally. If the defects are acceptable, click \"Resume\" button to resume the print job."
        },
        {
          "ecode": "07FF8001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07FF8002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "07FF8003",
          "intro": "Please pull out the filament on the spool holder from the extruder or check if there is filament  broken in the extruder, if AMS is to be used later,please connect PTFE tube to the coupler and click the \"retry\" button."
        },
        {
          "ecode": "07FF8004",
          "intro": "Failed to pull back the filament from the toolhead to AMS. Please check whether the filament or the spool is stuck. After troubleshooting, click the \"retry\" button."
        },
        {
          "ecode": "07FF8005",
          "intro": "Failed to feed the filament outside the AMS. Please clip the end of the filament flat and check to see if the spool is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07FF8006",
          "intro": "Please feed from the spool holder until the tool head filament sensor is triggered, and then click \"Retry\"."
        },
        {
          "ecode": "07FF8007",
          "intro": "Please observe the nozzle. If the filament has been extruded, click \"Done\"; if it is not, please push the filament forward slightly and then click \"Retry\"."
        },
        {
          "ecode": "07FF8010",
          "intro": "AMS assist motor is overloaded. Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07FF8011",
          "intro": "AMS filament ran out. Please put a new filament into AMS and click the \"Retry\" button."
        },
        {
          "ecode": "07FF8012",
          "intro": "Failed to get AMS mapping table; please click \"Retry\" to continue."
        },
        {
          "ecode": "07FF8013",
          "intro": "Timeout purging old filament: Please check if the filament is stuck or the extruder is clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "07FF4001",
          "intro": "Filament is still loaded from the AMS after it has been disabled. Please unload the filament, load from the spool holder, and restart printing."
        },
        {
          "ecode": "0300800E",
          "intro": "The print file is not available. Please check to see if the storage media has been removed."
        },
        {
          "ecode": "0500C010",
          "intro": "MicroSD Card error: please reinsert, format or replace it."
        },
        {
          "ecode": "0500C011",
          "intro": ""
        },
        {
          "ecode": "05004012",
          "intro": "The door seems to be open, so printing was paused."
        },
        {
          "ecode": "05008013",
          "intro": "The print file is not available. Please check to see if the storage media has been removed."
        },
        {
          "ecode": "0300800F",
          "intro": "The door seems to be open, so printing was paused."
        },
        {
          "ecode": "05004014",
          "intro": "Failed to slice the printing job; please check the settings and restart the print job."
        },
        {
          "ecode": "03008010",
          "intro": "The heatbreak fan speed is abnormal."
        },
        {
          "ecode": "07FFC003",
          "intro": "Please pull out the filament on the spool holder from the extruder or check if there is filament  broken in the extruder, if AMS is to be used later,please connect PTFE tube to the coupler."
        },
        {
          "ecode": "07FFC006",
          "intro": "Please feed from the spool holder until the tool head filament sensor is triggered."
        },
        {
          "ecode": "05004015",
          "intro": "There is not enough free storage space for the print job. Please format or clean MicroSD card to release available space."
        },
        {
          "ecode": "12008001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8001",
          "intro": "Failed to cut the filament. Please check the cutter. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12008002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "12018002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "12028002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "12038002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "12FF8002",
          "intro": "The cutter is stuck. Please pull out the cutter handle and click the \"Retry\" button."
        },
        {
          "ecode": "12008003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038003",
          "intro": "Failed to pull out the filament from the extruder. Please check whether the extruder is clogged or whether the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8003",
          "intro": "Please pull out the filament on the spool holder from the extruder or check if there is filament  broken in the extruder, if AMS is to be used later,please connect PTFE tube to the coupler and click the \"retry\" button."
        },
        {
          "ecode": "12FFC003",
          "intro": "Please pull out the filament on the spool holder from the extruder or check if there is filament  broken in the extruder, if AMS is to be used later,please connect PTFE tube to the coupler."
        },
        {
          "ecode": "12008004",
          "intro": "Failed to pull back the filament from the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018004",
          "intro": "Failed to pull back the filament from the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028004",
          "intro": "Failed to pull back the filament from the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038004",
          "intro": "Failed to pull back the filament from the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8004",
          "intro": "Failed to pull back the filament from the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12008005",
          "intro": "Failed to feed the filament. Please load the filament, then click the \"Retry\" button."
        },
        {
          "ecode": "12018005",
          "intro": "Failed to feed the filament. Please load the filament and then click the \"Retry\" button."
        },
        {
          "ecode": "12028005",
          "intro": "Failed to feed the filament. Please load the filament, then click the \"Retry\" button."
        },
        {
          "ecode": "12038005",
          "intro": "Failed to feed the filament. Please load the filament, then click the \"Retry\" button."
        },
        {
          "ecode": "12FF8005",
          "intro": "Failed to feed the filament. Please load the filament, then click the \"Retry\" button."
        },
        {
          "ecode": "12008006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038006",
          "intro": "Failed to feed the filament into the toolhead. Please check whether the filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8006",
          "intro": "Please feed from the spool holder until the tool head filament sensor is triggered, and then click the \"Retry\" button."
        },
        {
          "ecode": "12FFC006",
          "intro": "Please feed from the spool holder until the tool head filament sensor is triggered."
        },
        {
          "ecode": "12008007",
          "intro": "Failed to extrude the filament. Please check whether the filament is stuck or the extruder clogged. After troubleshooting, click the \"retry\" button."
        },
        {
          "ecode": "12018007",
          "intro": "Failed to extrude the filament. Please check if the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028007",
          "intro": "Failed to extrude the filament. Please check if the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038007",
          "intro": "Failed to extrude the filament. Please check if the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8007",
          "intro": "Check nozzle. Click \"Done\" if filament was extruded, otherwise push filament forward slightly and click \"Retry.\""
        },
        {
          "ecode": "12008010",
          "intro": "Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018010",
          "intro": "Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028010",
          "intro": "Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038010",
          "intro": "Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8010",
          "intro": "Please check if the spool or filament is stuck. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12008011",
          "intro": "AMS filament has run out. Please insert a new filament into the AMS and click the \"Retry\" button."
        },
        {
          "ecode": "12018011",
          "intro": "AMS filament has run out. Please insert a new filament into the AMS and click the \"Retry\" button."
        },
        {
          "ecode": "12028011",
          "intro": "AMS filament has run out. Please insert a new filament into the AMS and click the \"Retry\" button."
        },
        {
          "ecode": "12038011",
          "intro": "AMS filament has run out. Please insert a new filament into the AMS and click the \"Retry\" button."
        },
        {
          "ecode": "12FF8011",
          "intro": "AMS filament has run out. Please insert a new filament into the AMS and click the \"Retry\" button."
        },
        {
          "ecode": "12008012",
          "intro": "Failed to get AMS mapping table. Please click the \"Retry\" button to continue."
        },
        {
          "ecode": "12018012",
          "intro": "Failed to get AMS mapping table; please click the \"Retry\" button to continue."
        },
        {
          "ecode": "12028012",
          "intro": "Failed to get AMS mapping table; please click the \"Retry\" button to continue."
        },
        {
          "ecode": "12038012",
          "intro": "Failed to get AMS mapping table; please click the \"Retry\" button to continue."
        },
        {
          "ecode": "12FF8012",
          "intro": "Failed to get AMS mapping table; please click the \"Retry\" button to continue."
        },
        {
          "ecode": "12008013",
          "intro": "Timeout while purging old filament. Please check if the filament is stuck or the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018013",
          "intro": "Timeout while purging old filament. Please check if the filament is stuck or the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028013",
          "intro": "Timeout while purging old filament. Please check if the filament is stuck or the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038013",
          "intro": "Timeout while purging old filament. Please check if the filament is stuck or the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12FF8013",
          "intro": "Timeout while purging old filament. Please check if the filament is stuck or the extruder clogged. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12004001",
          "intro": "Filament is still loaded from the AMS when it has been disabled. Please unload AMS filament, load from spool holder, and restart print job."
        },
        {
          "ecode": "12014001",
          "intro": "Filament is still loaded from the AMS when it has been disabled. Please unload AMS filament, load from spool holder, and restart print job."
        },
        {
          "ecode": "12024001",
          "intro": "Filament is still loaded from the AMS when it has been disabled. Please unload AMS filament, load from spool holder, and restart print job."
        },
        {
          "ecode": "12034001",
          "intro": "Filament is still loaded from the AMS when it has been disabled. Please unload AMS filament, load from spool holder, and restart print job."
        },
        {
          "ecode": "12FF4001",
          "intro": "Filament is still loaded from the AMS when it has been disabled. Please unload AMS filament, load from spool holder, and restart print job."
        },
        {
          "ecode": "12008014",
          "intro": "Failed to check the filament location in the tool head, please refer to the HMS. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018014",
          "intro": "Failed to check the filament location in the tool head, please refer to the HMS. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028014",
          "intro": "Failed to check the filament location in the tool head, please refer to the HMS. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038014",
          "intro": "Failed to check the filament location in the tool head; please refer to the HMS. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "05004016",
          "intro": "The MicroSD Card is write-protected. Please replace the MicroSD Card."
        },
        {
          "ecode": "05004017",
          "intro": "Binding failed. Please retry or restart the printer and retry."
        },
        {
          "ecode": "05004018",
          "intro": "Binding configuration information parsing failed,  please try again."
        },
        {
          "ecode": "05004019",
          "intro": "The printer has already been bound. Please unbind it and try again."
        },
        {
          "ecode": "0500401A",
          "intro": "Cloud access failed. Possible reasons include network instability caused by interference, inability to access the internet, or router firewall configuration restrictions. You can try moving the printer closer to the router or checking the router configuration and then try again."
        },
        {
          "ecode": "0500401B",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0500401C",
          "intro": "Cloud access is rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0500401D",
          "intro": "Cloud access failed, which may be caused by network instability due to interference. You can try moving the printer closer to the router before you try again."
        },
        {
          "ecode": "0500401E",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0500401F",
          "intro": "Authorization timed out. Please make sure that your phone or PC has access to the internet, and ensure that the Bambu Studio/Bambu Handy APP is running in the foreground during the binding operation."
        },
        {
          "ecode": "05004020",
          "intro": "Cloud access rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05004021",
          "intro": "Cloud access failed, which may be caused by network instability due to interference. You can try moving the printer closer to the router before you try again."
        },
        {
          "ecode": "05004022",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05004023",
          "intro": "Cloud access rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05004024",
          "intro": "Cloud access failed. Possible reasons include network instability caused by interference, inability to access the internet, or router firewall configuration restrictions. You can try moving the printer closer to the router or checking the router configuration before you try again."
        },
        {
          "ecode": "05004025",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05004026",
          "intro": "Cloud access rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05004027",
          "intro": "Cloud access failed; this may be caused by network instability due to interference. You can try moving the printer closer to the router before you try again."
        },
        {
          "ecode": "05004028",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05004029",
          "intro": "Cloud access is rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0500402A",
          "intro": "Failed to connect to the router, which may be caused by wireless interference or being too far away from the router. Please try again or move the printer closer to the router and try again."
        },
        {
          "ecode": "0500402B",
          "intro": "Router connection failed due to incorrect password. Please check the password and try again."
        },
        {
          "ecode": "0500402C",
          "intro": "Failed to obtain IP address, which may be caused by wireless interference resulting in data transmission failure or DHCP address pool of the router being full. Please move the printer closer to the router and try again. If the issue persists, please check router settings to see whether the IP addresses have been exhausted."
        },
        {
          "ecode": "03008011",
          "intro": "The current build plate is not the same as in G-code. Please stop the print job and replace the build plate. You can also tap \"Resume\" to force-resume the print job."
        },
        {
          "ecode": "03008012",
          "intro": ""
        },
        {
          "ecode": "03008013",
          "intro": "Printing was paused by the user. You can tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "0500402D",
          "intro": "System exception."
        },
        {
          "ecode": "0C00800A",
          "intro": "The detected build plate is not the same as in G-code."
        },
        {
          "ecode": "0500402E",
          "intro": "The system does not support the file system currently used by the Micro SD card. Please replace the Micro SD card or format the current Micro SD card to FAT32."
        },
        {
          "ecode": "0500402F",
          "intro": "The Micro SD card sector data is damaged. Please use the SD card repair tool to repair or format it. If it still cannot be identified, please replace the Micro SD card."
        },
        {
          "ecode": "05008030",
          "intro": ""
        },
        {
          "ecode": "03008014",
          "intro": "The nozzle is covered with filament, or the build plate is installed incorrectly. Please clean the nozzle or adjust the position of the build plate. Then you can tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "03008015",
          "intro": "The filament has run out, please load new filament in the \"filament\" page, then return back to the print page and tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "05014017",
          "intro": "Binding failed. Please retry or restart the printer and retry."
        },
        {
          "ecode": "05014018",
          "intro": "Binding configuration information parsing failed,  please try again."
        },
        {
          "ecode": "05014019",
          "intro": "The printer has already been bound. Please unbind it and try again."
        },
        {
          "ecode": "0501401A",
          "intro": "Cloud access failed. Possible reasons include network instability caused by interference, inability to access the internet, or router firewall configuration restrictions. You can try moving the printer closer to the router or checking the router configuration and then try again."
        },
        {
          "ecode": "0501401B",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0501401C",
          "intro": "Cloud access is rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0501401D",
          "intro": "Cloud access failed, which may be caused by network instability due to interference. You can try moving the printer closer to the router before you try again."
        },
        {
          "ecode": "0501401E",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "0501401F",
          "intro": "Authorization timed out. Please make sure that your phone or PC has access to the internet, and ensure that the Bambu Studio/Bambu Handy APP is running in the foreground during the binding operation."
        },
        {
          "ecode": "05014020",
          "intro": "Cloud access rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014021",
          "intro": "Cloud access failed, which may be caused by network instability due to interference. You can try moving the printer closer to the router before you try again."
        },
        {
          "ecode": "05014022",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014023",
          "intro": "Cloud access rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014024",
          "intro": "Cloud access failed. Possible reasons include network instability caused by interference, inability to access the internet, or router firewall configuration restrictions. You can try moving the printer closer to the router or checking the router configuration before you try again."
        },
        {
          "ecode": "05014025",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014026",
          "intro": "Cloud access rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014027",
          "intro": "Cloud access failed; this may be caused by network instability due to interference. You can try moving the printer closer to the router before you try again."
        },
        {
          "ecode": "05014028",
          "intro": "Cloud response is invalid. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014029",
          "intro": "Cloud access is rejected. If you have tried multiple times and are still failing, please contact customer service."
        },
        {
          "ecode": "05014031",
          "intro": "Device discovery binding is in progress, and the QR code cannot be displayed on the screen. You can wait for the binding to finish or abort the device discovery binding process in the APP/Studio and retry scanning the QR code on the screen for binding."
        },
        {
          "ecode": "05014032",
          "intro": "QR code binding is in progress, so device discovery binding cannot be performed. You can scan the QR code on the screen for binding or exit the QR code display page on screen and try device discovery binding."
        },
        {
          "ecode": "03008016",
          "intro": "The nozzle is clogged up with filaments. Please check the nozzle. Then you can tap \"Resume\" to resume the print job."
        },
        {
          "ecode": "05014033",
          "intro": "Your APP region is not matched with your printer, please download the APP in the corresponding region and register your account again."
        },
        {
          "ecode": "12008015",
          "intro": "Failed to pull back the filament from the toolhead. Please check if the filament is stuck or the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12018015",
          "intro": "Failed to pull back the filament from the toolhead. Please check if the filament is stuck or the filament is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12028015",
          "intro": "Failed to pull back the filament from the toolhead. Please check if the filament is stuck or is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "12038015",
          "intro": "Failed to pull back the filament from the toolhead. Please check if the filament is stuck or is broken inside the extruder. After troubleshooting, click the \"Retry\" button."
        },
        {
          "ecode": "1000C003",
          "intro": "Enabling traditional timelapse might lead to defects. Continue?"
        },
        {
          "ecode": "05014034",
          "intro": "The slicing progress has not been updated for a long time, and the printing task has exited. Please confirm the parameters and reinitiate printing."
        },
        {
          "ecode": "05014035",
          "intro": "The device is in the process of binding and cannot respond to new binding requests."
        },
        {
          "ecode": "1001C001",
          "intro": "Timelapse is not supported because Spiral vase is enabled in slicing presets."
        },
        {
          "ecode": "1001C002",
          "intro": "Timelapse is not supported because Print sequence is set to \"By object\"."
        },
        {
          "ecode": "05008036",
          "intro": "Your sliced file is not consistent with the current printer model. Continue?"
        },
        {
          "ecode": "05004037",
          "intro": "Your sliced file is not compatible with current printer model. This file can't be printed on this printer."
        },
        {
          "ecode": "05004038",
          "intro": "The nozzle diameter in sliced file is not consistent with the current nozzle setting. This file can't be printed."
        },
        {
          "ecode": "03008017",
          "intro": "Foreign objects detected on  hotbed, Please check and clean the hotbed, Then tap \"Resume\" button to resume the print job."
        }
      ]
    }
  }
}