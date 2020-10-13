import socket

if __name__ == '__main__':
    # 创建服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用，程序退出就释放端口号
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 绑定端口号
    tcp_server_socket.bind(('',8000))
    # 设置监听
    tcp_server_socket.listen(128)
    # 让程序重复接单
    while True:
        # 等待客户端连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        # 对数据长度进行判断，如果没有发送数据，那么久直接关闭连接


        print(recv_client_data)
        # 对二进制数据进行解码
        recv_client_data = recv_client_data.decode('utf-8')
        print(recv_client_data)

        with open('static/index2.html','rb') as file:
            # 读取文件数据
            file_data = file.read()

            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_head = 'Server:PWS1.0\r\n'

            # 响应体
            response_body = file_data

            # 拼接发送报文
            response_data = (response_line + response_head + '\r\n').encode('utf-8') + response_body

            # 发送数据
            new_socket.send(response_data)

            # 关闭与客户端的套接字
            new_socket.close()