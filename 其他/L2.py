import psutil
import time

# 网速监控 

sent_before = 0
recv_before = 0

for i in range(2):
    net = psutil.net_io_counters()

    recv_now = net.bytes_recv - recv_before
    recv_before = net.bytes_recv

    sent_now = net.bytes_sent - sent_before
    sent_before = net.bytes_sent

    bytes_recv = '{0:.2f} Mb/s'.format(recv_now / 1024 / 1024)
    bytes_sent = '{0:.2f} Mb/s'.format(sent_now / 1024 / 1024)

    print(u"网卡接收流量 %s 网卡发送流量 %s" % (bytes_recv, bytes_sent))
    time.sleep(1)

mem = psutil.virtual_memory()
# memory_total = '{0:.2f} Gb'.format(mem.total / 1024 / 1024 / 1024)
# memory_available = '{0:.2f} Gb'.format(mem.available / 1024 / 1024 / 1024)
memory_percent = '{0:.1f} %'.format(mem.percent)
memory_used = '{0:.2f} Gb'.format(mem.used / 1024 / 1024 / 1024)
# memory_free = '{0:.2f} Gb'.format(mem.free / 1024 / 1024 / 1024)

# print(memory_total)
# print(memory_free)
# print(memory_percent)

print(u"已用内存 %s 内存利用率 %s" % (memory_used, memory_percent))

cpu_percent = '{0:.1f} %'.format(psutil.cpu_percent(1))
print(u"cpu利用率 %s" % (cpu_percent))