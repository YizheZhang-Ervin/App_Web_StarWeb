# 导入串口所需模块
import serial 
import serial.tools.list_ports
import threading

class EasySerial:
    def __init__(self,dataCrudInstance):
        self.availablePorts=self.searchAavailableSerial()  # 是否有可读取的串口
        self.serialData="" # 读取的数据
        self.serialReadFlag=False  # 读取标志位
        self.serialInstance=None  # 当前串口
        self.serialThread=None # 读取数据用的线程
        self.easyDataInstance = dataCrudInstance  # 写入数据的工具

    # 可用串口查询
    def searchAavailableSerial(self):
        port_list = list(serial.tools.list_ports.comports())
        return port_list

    #打开串口
    def openSerial(self,port,bps,timeout):
        try:
            # 打开串口，并得到串口对象
            self.serialInstance = serial.Serial(port, bps, timeout=timeout)
            # 判断是否打开成功
            if self.serialInstance.is_open:
                # 标记开始读取
                self.serialReadFlag = True
                self.serialThread = threading.Thread(target=self.readData, args=())
                self.serialThread.start()
                return 200
            else:
                return 500
        except Exception as e:
            print("端口打开失败", e)
            return 500

    # 关闭串口
    def closeSerial(self):
        # 标记结束读取
        self.serialReadFlag=False
        # 关闭串口
        self.serialInstance.close()

    # 读取串口数据
    def readData(self,encoding="gbk"):
        while self.serialReadFlag:
            if self.serialInstance.in_waiting:
                self.serialData = self.serialInstance.read(self.serialInstance.in_waiting).decode(encoding)
                # 数据写入表
                self.easyDataInstance.create([[self.serialData]])

    # 写入串口数据
    def writeData(self,text,encoding="gbk"):
        result = self.serialInstance.write(text.encode(encoding))
        return result

# 运行入口
if __name__=="__main__":
    # 尝试打开串口
    serial001 = EasySerial()
    # 判断是否有可用串口
    if len(serial001.availablePorts)>0:
        status = serial001.openSerial(port="COM4",bps=9600,timeout=None)
        #判断串口是否成功打开
        if status==200:
            # 写入数据
            count = serial001.writeData("自定义字符串","gbk")
            print("写入字节数：",count)
            # 关闭串口
            serial001.closeSerial()
        else:
            print(f"串口未成功打开,请尝试其他串口:{serial001.availablePorts}")
    else:
        print("无可用串口")