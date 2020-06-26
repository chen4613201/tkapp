import os
import wmi


class AddrInfo:

    filedata = []

    def getAllDataFromFile(self):
        global filedata
        iplist = []
        data = []
        if os.path.exists("../config/NetInfo.txt")==False:
            self.createInitFile()

        with open("../config/NetInfo.txt", "r", encoding='utf8') as f:
            for line in f.readlines():
                if len(line)>0:
                    data.append(line)
            f.close()
        filedata = data[:]
        for item in data:
            item = item.strip("\n")
            iplist.append(item.split(',')[0])

        del iplist[0]
        return data,iplist


    def getSingleRecord(self, dataRecord):
        global filedata
        for item in filedata:
            if dataRecord == item.split(',')[0]:
                return item.split(',')


    def modSingleRecord(self,dataRecord):
        global filedata
        matchnum = 0
        dataRecordIp = dataRecord.split(',')[0]
        #print(dataRecordIp)
        #print(type(dataRecordIp))
        for item in filedata:
            if dataRecordIp == item.split(',')[0]:
                idx = filedata.index(item)
                filedata[idx] = dataRecord
                matchnum += 1

        if matchnum == 0:
            filedata.append(dataRecord)

        with open("../config/NetInfo.txt", "w", encoding='utf8') as f:
            for line in filedata:
                if line.endswith('\n'):
                    f.write(line)
                else:
                    f.write('%s\n' % line)
            f.close()


    def delSingleRecord(self,dataRecord):
        global filedata
        print(dataRecord)
        print(filedata.index(dataRecord))
        idx = filedata.index(dataRecord)
        del filedata[idx]
        with open("../config/NetInfo.txt", "w", encoding='utf8') as f:
            for line in filedata:
                if line.endswith('\n'):
                    f.write(line)
                else:
                    f.write('%s\n' % line)
            f.close()
        return '删除成功'


    def createInitFile(self):
        with open("../config/NetInfo.txt", "w", encoding='utf8') as f:
            f.write('[IPv4地址],[子网掩码],[地址网关],[DNS服务器]')
            f.close()


    def mod_net_info(self,ip,mask,gateway,fdns,sdns):
        wmiserver = wmi.WMI()
        netAdpt = wmiserver.Win32_NetworkAdapterConfiguration(IPEnabled=True)
        gatewayCostMetric=[1]
        DnsServer = []
        DnsServer += fdns
        DnsServer += sdns
        if len(netAdpt) < 1:
            print("没有可用的网络适配器")
            exit()
        print(netAdpt)

        objNetAdpt = netAdpt[0]
        print(objNetAdpt)
        ret_value = []

        try:
            objNetAdpt.EnableStatic(IPAddress=ip,SubnetMask=mask)
            ret_value.append("IPv4地址设置成功")
        except Exception as e:
            ret_value.append("IPv4地址设置失败"+str(e)+"\n")

        try:
            objNetAdpt.SetGateways(DefaultIPGateway=gateway,GatewayCostMetric=gatewayCostMetric)
            ret_value.append("网关设置成功")
        except Exception as e:
            ret_value.append("网关设置失败"+str(e)+"\n")

        try:
            objNetAdpt.SetDNSServerSearchOrder(DNSServerSearchOrder=DnsServer)
            ret_value.append("DNS设置成功")
        except Exception as e:
            ret_value.append("DNS设置失败"+str(e)+"\n")

        return ret_value
