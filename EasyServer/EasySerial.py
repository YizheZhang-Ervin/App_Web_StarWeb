# 导入串口所需模块
import serial 
import serial.tools.list_ports
import threading

# 命令查串口 python -m serial.tools.list_ports

# 可用串口查询
def searchAavailableSerial():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) == 0:
        print('无可用串口')
    return port_list

# 打开端口
def openSerial(port="COM3",bps=115200,timeout=5):
    # port 端口: GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
    # bps 波特率: 标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    # timeout 超时设置: None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    # 打开串口，并得到串口对象
    ser=serial.Serial(port,bps,timeout=timeout)
    print(ser.port)      # 获取到当前打开的串口名
    print(ser.baudrate)  # 获取波特率
    return ser

# 写数据
def writeData(ser,string="自定义字符串"):
    # ser 串口
    # string 自定义字符串
    result=ser.write(string.encode("gbk"))
    print("写总字节数:",result)
    ser.close()#关闭串口

# 按16进制写数据
def writeDataHex(ser,hexString=0x06):
    # ser 串口
    # hexString 自定义16进制字符串
    result=ser.write(chr(hexString).encode("utf-8"))
    print("写总字节数:",result)
    ser.close()#关闭串口

# 读数据
def readData(ser):
    # print(ser.read(10).decode("gbk"))      #读十个字节
    # print(ser.readline().decode("gbk"))    #读一行
    # print(ser.readlines())                 #读取多行，返回列表，必须匹配超时（timeout)使用
    # print(ser.in_waiting)                  #获取输入缓冲区的剩余字节数
    # print(ser.out_waiting)                 #获取输出缓冲区的字节数
    result = ser.read()                      #读一个字节
    print(result)
    return result
    

# 按16进制读数据
def readDataHex(ser):
    #十六进制的读取一个字节
    result = ser.read().hex()
    print(result)
    return result

# 循环接收数据
def loopReadData(ser):
    while True:
        if ser.in_waiting:
            str=ser.read(ser.in_waiting ).decode("gbk")
            if(str=="exit"):#退出标志
                break
            else:
                print("收到数据：",str)
    ser.close()#关闭串口

###################### 以上函数使用方法
# # 列出所有可用端口
# port_list = searchAavailableSerial()
# print(f"可用端口为：{port_list}")
# # 打开端口
# ser = openSerial(port="COM3",bps=115200,timeout=5)
# # 写入数据
# writeData(ser,string="自定义字符串")
# writeDataHex(ser,hexString=0x06)
# # 读取数据
# data = readData(ser)
# data = readDataHex(ser)
# loopReadData(ser)

#############################################################################

# 高级版
class EasySerial:
    def __init__(self):
        self.DATA="" #读取的数据
        self.BOOL=True  #读取标志位
        self.ser = None  # 当前串口
        self.availablePorts = []
        self.canOpenSerial = self.searchAavailableSerial()  # 是否有可读取的串口
        self.isOpenSerial = False   # 标记是否打开串口

    # 可用串口查询
    def searchAavailableSerial(self):
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) == 0:
            print('无可用串口')
        else:
            self.canOpenSerial = True
            self.availablePorts = port_list
            print(f"可用串口列表：{port_list}")

    def openSerial(self,port,bps,timeout):
        try:
            # 打开串口，并得到串口对象
            self.ser = serial.Serial(port, bps, timeout=timeout)
            #判断是否打开成功
            if(self.ser.is_open):
                self.isOpenSerial=True
                threading.Thread(target=self.ReadData, args=()).start()
        except Exception as e:
            print("端口打开失败", e)

    #关闭串口
    def closeSerial(self):
        self.BOOL=False
        self.ser.close()

    # 读取数据
    def readData(self):
        while self.BOOL:
            if self.ser.in_waiting:
                self.DATA = self.ser.read(self.ser.in_waiting).decode("gbk")
                print(self.DATA)

    #写数据
    def writeData(self,text):
        result = self.ser.write(text.encode("gbk"))  # 写数据
        return result

# 运行入口
if __name__=="__main__":
    # 尝试打开串口
    serial001 = EasySerial()
    # 判断是否有可用串口
    if serial001.canOpenSerial:
        isOpenSerial = serial001.openSerial(port="COM4",bps=9600,timeout=None)
        #判断串口是否成功打开
        if serial001.isOpenSerial:
            # 写入数据
            count = serial001.writeData("自定义字符串")
            print("写入字节数：",count)
            # 读串口数据
            serial001.readData()
            # 关闭串口
            serial001.closeSerial()
        else:
            print(f"串口未成功打开,请尝试其他串口:{serial001.availablePorts}")
    else:
        print("无可用串口")