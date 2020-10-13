# 1.创建服务端套接字对象
# 2.绑定监听端口号
# 3.设置监听
# 4.等待客户端的连接请求
# 5.接收数据
# 6.发送数据
# 7.关闭套接字

import socket
# 创建服务端对象
if __name__ == '__main__':

    tcp_sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 先设置端口号复用，这样程序结束后会立即释放端口号
    # 三个参数：参数1：表示当前套接字   参数2：设置端口号复用选项   参数3：设置端口号复用选项对应的值
    tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_sever_socket.bind(('', 8989))
    # 设置监听
    tcp_sever_socket.listen(128)
    # 每次连接成功之后，就会产生一个新的套接字,tcp_server_socket只负责等待客户端的连接请求，不负责传递消息
    new_client, ip_port = tcp_sever_socket.accept()
    print(new_client)
    print('客户端的ip地址和端口是：', ip_port)
    # 接收客户端发出的请求
    recv_data = new_client.recv(1024)
    recv_data = recv_data.decode('gbk')
    print(recv_data)

    # 发送消息
    use_send = input('你的名字：')
    use_send = use_send.encode('gbk')
    send_data = new_client.send(use_send)
    # 新的套接字也是需要关闭的
    new_client.close()
    # 关闭服务端的套接字，那么以后就能对服务端发送请求了
    tcp_sever_socket.close()
