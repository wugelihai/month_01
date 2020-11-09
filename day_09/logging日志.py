# 用来记录程序运行时的日志信息
import logging

# level=logging.DEBUG设置级别
# %(asctime)s表示当前时间
# %(filename)s表示程序文件名
# %(lineno)d表示行号
# %(levelname)s表示行号
# %(message)s表示日志信息
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s",
                    filename="log.txt",
                    filemode="w")
logging.debug("这是一个debug级别的日志111")
logging.info("这是一个info级别的日志")
logging.warning("这是一个warning级别的日志")
logging.error("这是一个error级别的日志")
logging.critical("这是一个critical级别的日志")
# 默认是warning，只有大于等于warning级别的日志才会输出显示
