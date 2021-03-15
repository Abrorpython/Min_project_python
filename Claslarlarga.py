import sqlite3
class name:
    def __init__(self):
        self.con = sqlite3.connect("bozor.db")
        self.com = self.con.cursor()
        # self.com.execute("""CREATE TABLE bozor(
        # mahsulot TEXT,
        # narxi INTEGER,
        # miqdori TEXT,
        # jami INTEGER
        # )""")
    def qoshish(self,mahsulot,narxi,miqdori,jami):
        self.com.execute(f"""INSERT INTO bozor (mahsulot,narxi,miqdori,jami) VALUES 
        ("{mahsulot}",{narxi},"{miqdori}",{jami})""")
        self.con.commit()
    def mahsulot_qidir(self,qidir):
        self.com.execute(f"""SELECT * FROM bozor WHERE mahsulot = "{qidir}" """)
        print(self.com.fetchall())
    def Pulingiz_boricha(self,pul):
        self.com.execute(f"""SELECT * FROM bozor WHERE narx < {pul} """)
        print(self.com.fetchall())
    def alpha(self,a):
        self.com.execute(f"""SELECT * FROM bozor WHERE mahsulot LIKE "{a}%" """)
        print(self.com.fetchall())
a=name()
#a.qoshish(b,c,d,f)
while True:
    savol=input("Mahsulot qo'shasanmi,qidirasanmi? = 1/2: ")
    if savol=="1":
        b = input("Mahsulot nomini kiriting: ")
        c = int(input("Mahuslot narxini kiriting:"))
        d = input("Mahsulot miqdorini kiriting: ")
        f = int(input("Jami mahsulotni kiritng: "))
        a.qoshish(b,c,d,f)
    elif savol=="2":
        savol1=input("Qanday qidirasan? nomi bo'yicha,Pulingiz yetganicha,harflar bo'yicha = 3/4/5: ")
        if savol1=="3":
            m=input("Mahsulot nomini kirit: ")
            a.mahsulot_qidir(m)
        elif savol1=="4":
            n=int(input("Cho'ntagingizda borini kiriting: "))
            a.Pulingiz_boricha(n)
        elif savol1=="5":
            h=input("Bosh harfini kirit: ")
            a.alpha(h)
