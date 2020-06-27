import ping3

class ServerInfo:
    filedata=[]

    def getServerList(self):
        global filedata
        data = []
        with open("../config/ServerInfo.txt", "r", encoding='utf8') as f:
            for line in f.readlines():
                if len(line)>0:
                    if line.endswith('\n'):
                        data.append(line.strip('\n'))
                    else:
                        data.append(line)
            f.close()
        filedata = data.copy()
        return filedata


    def addSgSvrInfo(self,ipstr):
        global filedata
        filedata.append(ipstr)
        print(filedata)
        self.writeFile(filedata)

    def modSgSvrInfo(self):
        pass

    def delSgSvrInfo(self,ipstr):
        global filedata
        for item in filedata:
            if ipstr == item:
                idx = filedata.index(item)
                filedata.pop(idx)
        self.writeFile(filedata)
        return 1

    def writeFile(self,content):
        with open("../config/ServerInfo.txt", "w", encoding='utf8') as f:
            for item in content:
                f.write(item+'\n')
            f.close()

    def NetCheck(self,ipstr):
        resdict = {}
        for item in ipstr:
            #print(type(item))
            #print(ping3.ping(item) is None)
            if ping3.ping(item) is None:
                resdict[item]="连接失败"
            else:
                resdict[item]="连接成功"
        #print(resdict)
        return resdict

if __name__ == '__main__':
    print(ping3.ping('192.168.0.150'))
    ServerInfo1 = ServerInfo()
    ServerInfo1.NetCheck(['192.168.0.150'])