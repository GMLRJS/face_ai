import cx_Oracle

class DaoFacelogin:
    def __init__(self):
        self.connect = cx_Oracle.connect("team1_202212F", "java", "192.168.141.13:1521/xe")
        self.cur = self.connect.cursor()
  
        
    def selectPW(self, mem_id):
        
        # 회원의 비밀번호를 가져오는 쿼리
        sql = f"""
            SELECT PASSWORD
            FROM MEMBER
            WHERE MEM_ID = '{mem_id}'
               
        """
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        list = []
        list.append(data[0][0])

        return list
    
    
    def __del__(self):
        self.cur.close()
        self.connect.close()
        
if __name__ == '__main__' :
    df = DaoFacelogin()
    pw = df.selectPW("dohee")
    print(pw[0])
        
