import socket
import threading


# 把连接成功后的功能封装，这样创建子线程直接调用就可以了
def handle_client_request(ip_port, new_client):
    print('客户端的ip地址和端口是：', ip_port)
    # 实现重复对话功能，避免对话一遍就直接结束了
    while True:
        # 接收客户端发出的请求
        recv_data = new_client.recv(1024)
        # 如果客户端关闭连接，那么接收数据的长度就是0
        print('接收数据的长度是：', len(recv_data))
        # 根据接收数据长度，判断是否关闭连接
        if recv_data:
            recv_data = recv_data.decode('gbk')
            print(recv_data)

            # 发送消息
            use_send = '排队中...'.encode('gbk')
            send_data = new_client.send(use_send)
        else:
            print('客户下线了：',ip_port)
            break
    # 新的套接字也是需要关闭的
    new_client.close()


# 创建服务端对象
if __name__ == '__main__':
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 先设置端口号复用，这样程序结束后会立即释放端口号
    # 三个参数：参数1：表示当前套接字   参数2：设置端口号复用选项   参数3：设置端口号复用选项对应的值
    tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    # bind有两个值，第一个值是ip地址，一般不写，第二个是端口号
    tcp_sever_socket.bind(('', 8989))
    # 设置监听
    tcp_sever_socket.listen(128)
    # 每次连接成功之后，就会产生一个新的套接字,tcp_server_socket只负责等待客户端的连接请求，不负责传递消息

    while True:
        new_client, ip_port = tcp_sever_socket.accept()
        child_process = threading.Thread(target=handle_client_request, args=(ip_port, new_client))
        # 设置守护进程，主线程销毁，子线程销毁
        child_process.setDaemon(True)
        child_process.start()

    # 关闭服务端的套接字，那么以后就能对服务端发送请求了
    # tcp_sever_socket.close()   # 因为服务端要一直运行，所以这行代码不会执行，没有意义
