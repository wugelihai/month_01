# 1.创建客户端套接字
import socket
if __name__ == '__main__':
    # 创建tcp客户端套接字
    # 1. AF_INET：表示ipv4
    # 2. SOCK_STREAM: tcp传输协议
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.和服务端建立套接字连接
    tcp_client_socket.connect(('10.211.55.5',8080))
    # 如果代码执行到这里，说明连接建立成功
# 3.发送数据
    # 数据传输都是以二进制形式，所以这里要对传输的数据进行编码操作
    send_data = '你好，我在测试'.encode('gbk')
    # 把编码后的数据发送出去
    tcp_client_socket.send(send_data)
# 4.接收数据
    # 接收数据，设置最大接收字节数为1024
    recv_data = tcp_client_socket.recv(1024)
    # print(recv_data)    # 这里如果不解码直接使用，结果就看不懂
    # 接收到的数据是二进制，需要对数据进行解码操作
    recv_data = recv_data.decode('gbk')
    print(recv_data)
# 5.关闭客户端套接字
    tcp_client_socket.close()