from settings import conn

cur = conn.cursor()


def is_null(username, password):
	if username=='' or password=='':
		return True
	else:
		return False


def is_existed(username,password):
	sql = "SELECT * FROM user WHERE username ='%s' and password ='%s'" %(username,password)
	conn.ping(reconnect=True)
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True

def exist_user(username):
	sql = "SELECT * FROM user WHERE username ='%s'" % (username)
	conn.ping(reconnect=True)
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True


def add_user(username, password):
    # sql commands
    sql = "INSERT INTO user(username, password) VALUES ('%s','%s')" %(username, password)
    # execute(sql)
    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()
