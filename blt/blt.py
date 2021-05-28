# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from typing import NamedTuple
from time import sleep


class BLT:
    enc="utf-8"

    def __init__(self, mac: str = None):
        self.mac = mac


    # def info(self):
    #     stdout, stderr = Popen(["sudo", "hcitool", "info", mac], stdout=PIPE, stderr=PIPE).communicate()
    #     if len(stderr) > 0:
    #         raise LookupError(stderr.decode(self.enc))
    #     result = stdout.decode(self.enc).split("\n")[1:]
    #     print(result)

    def scan(self):
        print("[*] Scanning...")

    @staticmethod
    def list_usb_devices():
        "lsusb | egrep -i 'blue'"
        "hciconfig"

    @staticmethod
    def hcitool_scan():
        """
        Scans for bluetooth devices
        """
        stdout, stderr = Popen(["hcitool", "scan", "rssi"], stdout=PIPE, stderr=PIPE).communicate()
        if len(stderr) > 0:
            raise LookupError(stderr.decode(BLT.enc))
        result = stdout.decode(BLT.enc).split("\n")[1:]
        devices = []
        for d in result[0: len(result)-1]:
            d = d.split("\t")[1:]
            devices.append(BTDevice(d[0], d[1]))
        return devices
    
    @staticmethod
    def hcitool_le_scan(timeout=10):
        """
        Scans for LE bluetooth devices
        """
        # sudo timeout -s SIGINT 5s hcitool -i hci0 lescan > file.txt
        args = ["sudo", "timeout", "-s", "SIGINT", f"{timeout}s", "hcitool", "lescan"]
        stdout, stderr = Popen(args, stdout=PIPE, stderr=PIPE).communicate()
        if len(stderr) > 0:
            raise LookupError(stderr.decode(BLT.enc))
        print(stdout)
        result = stdout.decode(BLT.enc).split("\n")[1:]
        devices = []
        for d in result[0: len(result)]:
            devices.append(BTDevice(d, ""))
        return devices

    @staticmethod
    def info(mac: str, enc="utf-8"):
        stdout, stderr = Popen(["sudo", "hcitool", "info", mac], stdout=PIPE, stderr=PIPE).communicate()
        if len(stderr) > 0:
            raise LookupError(stderr.decode(enc))
        result = stdout.decode(enc).split("\n")[1:]
        print(result)
    
    @staticmethod
    def ping(mac:str, enc="utf-8"):
        for _ in range(1, 10000):
            xterm_1 = f"sudo l2ping -i hci0 -s 999 -f {mac} &"
            Popen(xterm_1, stdout=PIPE, stderr=PIPE, shell=True)
            sleep(3)
        # stdout, stderr = Popen(["sudo", "l2ping", "-s 100", "-f", mac], stdout=PIPE, stderr=PIPE).communicate()
        # print(stdout)
        # if len(stderr) > 0:
        #     raise LookupError(stderr.decode(enc))

class BTDevice(NamedTuple):
    mac: str
    name: str
    def __str__(self):
        return f"{self.mac} {self.name}"

if __name__ == "__main__":
    # d = BLT.hcitool_scan()
    #d = BLT.hcitool_le_scan()
    #print(d)
    