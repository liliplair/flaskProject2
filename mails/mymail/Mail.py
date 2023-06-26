from imbox import Imbox


class Mail:
    mails = {}
    address = ""
    password = ""
    imap = " "

    def __init__(self):
        pass

    def __init__(self, imap, address, password):
        self.imap = imap
        self.address = address
        self.password = password

    # 读取未读邮件
    def read_mails(self):
        def simplify_text(str0):
            return str0
        if self.mails :
            return
        with Imbox(self.imap, self.address, self.password, ssl=True) as imbox:
            # unread=True 表示只列出未读信息
            # flagged=True 表示获取红旗邮件
            # send_to=xxx@qq.com 表示只获取某个邮件地址的信息
            all_imbox_msg = imbox.messages(unread=True)
            index = 1
            for uid, msg in all_imbox_msg:
                text = simplify_text(msg.body['plain'])
                self.mails[index] = {
                    'subject': msg.subject,
                    'sent_from_name': msg.sent_from[0]['name'],
                    'date': msg.date,
                    # 'text': msg.body['html'],
                    'text': msg.body['plain'],
                    'uid': uid
                }
                index += 1
                if index > 10:
                    return

    # 标记为已读
    def change_to_read(self, index):
        index = int(index)
        read_mail = self.mails.get(index)
        uid = read_mail.get('uid')
        with Imbox(self.imap, self.address, self.password, ssl=True) as imbox:
            imbox.mark_seen(uid)
        del self.mails[index]

    # 标记为删除(垃圾箱)
    def change_to_dele(self, index):
        index = int(index)
        read_mail = self.mails.get(index)
        uid = read_mail.get('uid')
        with Imbox(self.imap, self.address, self.password, ssl=True) as imbox:
            imbox.delete(uid)
        del self.mails[index]
