import serial
import io

def getLineChartData():
    pass

def getHistChartData():
    pass

def write():
    ser.write(b'hello')  # 写入字符串
    ser.close()  # 关闭端口

    ser = serial.serial_for_url('loop://', timeout=1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    sio.write("hello\n")
    sio.flush()
    hello = sio.readline()
    print(hello == "hello\n")

def connectWithoutTimeout(port = 'COM3',baudrate = 38400,timeout = 0,rtscts=10,parity=serial.PARITY_EVEN):
    ports = serial.tools.list_ports
    print(f"检测到端口为：{ports}")
    ser = serial.Serial(port, baudrate, timeout=timeout,parity=parity, rtscts=rtscts)
    s = ser.read(100)
    print(f"前100位：{s}")
    line = ser.readline()
    print(f"第一行：{line}")

if __name__ == "__main__":
    connectWithoutTimeout(port='COM4',baudrate=9600,timeout=0,rtscts=8,parity=serial.PARITY_EVEN)