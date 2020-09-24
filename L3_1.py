import psutil
import serial

sent_before = 0
recv_before = 0


# 发送数据
def Send_Data():
    # string = ""
    global recv_before, sent_before
    # cpu使用率
    cpu_percent = '{0:.1f}%'.format(psutil.cpu_percent(1))
    # 内存使用率
    mem = psutil.virtual_memory()
    memory_percent = '{0:.1f}%'.format(mem.percent)
    # 网络上下行
    net = psutil.net_io_counters()
    # print(net.bytes_recv)
    # print(recv_before)
    recv_now = net.bytes_recv - recv_before
    recv_before = net.bytes_recv
    # print(recv_now)
    # print(recv_before)

    sent_now = net.bytes_sent - sent_before
    sent_before = net.bytes_sent

    if recv_now / 1024 < 1024:
        bytes_recv = '{0:>4d}K'.format(int(recv_now / 1024))
    elif 1024 <= recv_now / 1024 < 10240:
        bytes_recv = '{0:.2f}M'.format(recv_now / 1024 / 1024)
    else:
        bytes_recv = '{0:.1f}M'.format(recv_now / 1024 / 1024)

    if sent_now / 1024 < 1024:
        bytes_sent = '{0:>4d}K'.format(int(sent_now / 1024))
    elif 1024 <= sent_now / 1024 < 10240:
        bytes_sent = '{0:.2f}M'.format(sent_now / 1024 / 1024)
    else:
        bytes_sent = '{0:.2f}M'.format(sent_now / 1024 / 1024)

    # 整合成一个字符串
    string = "C {0:0>6}{1:0>6}{2:>6}{3:>6}".format(
        cpu_percent, memory_percent, bytes_recv, bytes_sent) + 14 * " "
    return string


# for i in range(5):
#     print(Send_Data())
    # print(len(Send_Data()))

ser = serial.Serial("/dev/tty.wchusbserial1460", 9600, timeout=0.5)
while 1:
    Push = Send_Data()
    ser.write(Push.encode())
    print(Push)
