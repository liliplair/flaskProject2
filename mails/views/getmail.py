from flask import Blueprint, render_template, request
from ..mymail.Mail import Mail

gm = Blueprint('gm', __name__)


# 登录后从数据库读取用户信息
def get_userinfo():
    pass
    address = "1295476850@qq.com"
    password = "qhdskagavvxijbaj"
    imap = 'imap.qq.com'
    return imap, address, password


imap, add, pwd = get_userinfo()
mail = Mail(imap, add, pwd)


@gm.route('/getmail')
# @app.route('/refresh')
def getmail():
    mail.read_mails()
    return render_template('getmail.html', mails=mail.mails)


@gm.route("/showmail")
def showmail():
    # 登陆判定
    index = int(request.args.get('index'))
    detail = mail.mails.get(index)
    return render_template('showmail.html', detail=detail)
