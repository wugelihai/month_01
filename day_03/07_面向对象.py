import socket
import threading


class HttpWebServer(object):
    def __init__(self):
        # 创建服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用，程序退出就释放端口号
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(('', 9000))
        # 设置监听
        tcp_server_socket.listen(128)
        # 让程序保持在线
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):
        recv_client_data = new_socket.recv(4096)
        # 对数据长度进行判断，如果没有发送数据，那么就直接关闭连接
        if len(recv_client_data) == 0:
            new_socket.close()
            print('关闭浏览器了')
            return

        # print(recv_client_data)
        # 对二进制数据进行解码
        recv_client_data = recv_client_data.decode('utf-8')
        print(recv_client_data)

        # 对接收到的数据解码之后进行切片，用空格进行切片操作
        recv_client_list = recv_client_data.split(' ', 2)

        # 切片之后取得下标为1的值就是用户请求页面的数据
        recv_client_path = recv_client_list[1]
        print(recv_client_path)

        # 如果用户请求根目录，那么就返回index.html页面的数据
        if recv_client_path == '/':
            recv_client_path = '/index.html'

        try:
            with open('static' + recv_client_path, 'rb') as file:
                # 读取文件数据
                file_data = file.read()

        except Exception as e:
            # 请求资源不存在，返回404数据
            # 相应行
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            # 响应头
            response_head = 'Server:PWS1.0\r\n'

            with open('static/error.html', 'rb') as file:
                file_data = file.read()

            # 响应体
            response_body = file_data

            # 拼接报文
            response_data = (response_line + response_head + '\r\n').encode('utf-8') + response_body

            new_socket.send(response_data)

        else:

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

        finally:
            # 关闭与客户端的套接字
            new_socket.close()

    def start(self):
        while True:
            # 等待客户端连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 代码执行到此说明连接建立成功

            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置成为守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()


def main():
    web_server = HttpWebServer()
    web_server.start()


if __name__ == '__main__':
    main()
