##!# bin/python
### This will be the ###
### Introduction     ###

## Import Section
import serial
import os
import argparse

## Variable declaration
defaultport = '/dev/ttys000'
buffersize = 10

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
        ## ser.applySettingsDict(arguments)
        ## ser.flushInput()
        ## ser.flushOutput()
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
    parser.add_argument('File', metavar='P', type=str, nargs='?', default='',help='Path to the HPGL file')
    parser.add_argument('Device', metavar='d', type=str, nargs='?', default=defaultport,help='Path to the device')
    args = parser.parse_args()
    return args

args = parseArgs()

def splitFile(f):
    list = f.read()
    list = list.replace("\n","")
    list = list.split(";")
    for i in xrange(0,len(list)):
        list[i] = list[i] + ";"
    return list



## AS MODULE ##
if __name__ != '__main__':
    def end():
        pass
    args = parseArgs()

## SCRIPTMODE ##
if __name__ == '__main__':
    def end():
        ser.close()
        quit()
    ## Parse Arguments
    args = parseArgs()
    f = openFile(args.File)
    list = splitFile(f)
    ser = openSerial(args.Device,serialsettings)
    eof = False
    index = 0
    buffer = 0
    lenlist = len(list)
    while eof != True:
        try:
            if buffer < buffersize:
                ser.write(list[index])
                index = index + 1
                buffer = buffer + 1
            bytesavailable = ser.inWaiting()
            if bytesavailable > 0:
                reponse = ser.Read(bytesavailable)
                print(response)
                buffer = buffer - response.count(';')

            if index == lenlist:
                eof = True

        except:
            print("Error while sending file")
            end()
    print
