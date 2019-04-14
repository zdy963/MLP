class UpdateWebSocket(WebSocketHandler,_AccountBaseHandler):
    """websocket代替轮询获取更新的数据
    """
    # 保存连接用户，用于后续推送消息
    all_shop_admins = set()

    #建立连接的时候，把用户保存到字典里面，用于后续推送消息使用
    def open(self):
        print("new　client opened")
        # 初始化
        all_shop_admins.add(self)

    # 关闭连接的时候需要清空连接用户
    def on_close(self):
        all_shop_admins.remove(self)

    # 项目中调用方法UpdateWebSocket.send_demand_updates(message)来给用户发送消息
    @classmethod
    def send_demand_updates(cls,message):
        # 给第一个用户推送消息
        all_shop_admins[0].write_message(message)

    def on_message(self,message):
        # 接收客户端发来的消息
        logging.info("got message %r", message)

    # 检查跨域请求，允许跨域，则直接return True，否则自定义筛选条件
    def check_origin(self, origin):
        parsed_origin = urllib.parse.urlparse(origin)
        return parsed_origin.netloc.endswith(".carrefourzone.senguo.cc")