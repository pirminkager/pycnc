##!# bin/python
### This will be the ###
### Introduction     ###

## Import Section
import serial
import os
import argparse

## Variable declaration

serialsettings = {'parity': 'N',
		  'baudrate': 32400,
		  'bytesize': 8,
		  'xonxoff': False,
		  'rtscts': False,
		  'timeout': 10,
		  'inter_byte_timeout': None,
		  'stopbits': 1,
		  'dsrdtr': False,
		  'write_timeout': None}

## Function Definitions

def openSerial(port,arguments):
    try:
        ser = serial.Serial(port)
        ser.applySettingsDict(arguments)
        ser.flushInput()
        ser.flushOutput()
    except:
        print("Couldn't open %s" % (port))
        end()
    return ser

def openFile(file):
    print file
    if file != '':
	try:
	    f = open(file, "r")
	except:
	    print("Couldn't open %s" % (file))
	    end()
    else:
	## Get Filename from input
        file = raw_input('Filename or Path: ')
	f = openFile(file)
    return f

def parseArgs():
    ##Definition
    parser = argparse.ArgumentParser(description='VHFterm')
    parser.add_argument('File', metavar='P', type=str, nargs='?', default='',
                        help='Path to the HPGL file')
    parser.add_argument('Device', metavar='d', type=str, nargs='?', default='/dev/pty/0',
		        help='Path to the device')
    args = parser.parse_args()
    return args

args = parseArgs()

def exit():
    raise SystemExit

def splitFile(f):
    list = f.read()
    list = list.replace("\n","")
    list = list.split(";")
    for i in xrange(0,len(list)):
        list[i] = list[i] + ";"
    return list

def sendFile(f):
    pass

def 

## AS MODULE ##
if __name__ != '__main__':

    def end():
	pass

    args = parseArgs()


## SCRIPTMODE ##
if __name__ == '__main__':

    def end():
	close()
  ## Parse Arguments
    args = parseArgs()
    openFile(args.File)
    openSerial(args.Device,serialsettings)
