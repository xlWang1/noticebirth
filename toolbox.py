import random,requests,json,pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Toolboox():
    def __init__(self):
        self.flag  = True
        while self.flag == True:
            print(f'请输入您要执行的业务:\n1.电话号码\n2.身份证号码\n3.姓名\n4.个人信息(姓名+身份证+电话号码)\n5.翻译\n6.退出\n')
            self.Input = input()
            match self.Input:
                case '1':
                    print(self.Phone_Num(),'\n')
                case '2':
                    print(self.SFZ(),'\n')
                case '3':
                    print(self.Name(),'\n')
                case '4':
                    self.getinfo()
                case '5':
                    self.translate()
                case '6':
                    self.Tuichu()
                case _ :
                    print(f'请输入1-5中的一位整数\n')

    def Is_num(self):

        while self.flag == True:
            try:
                float(self.Input)
                self.flag == False
                break

            except:
                print(f'请输入数字，不要输入其他字符\n')
            self.Input = input()

    def Phone_Num(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]

        # 最后八位数字
        suffix = random.randint(10000000, 99999999)
        self.phonenum = "1{}{}{}".format(second, third, suffix)
        return self.phonenum

    def SFZ(self):

        # 随机生成一个区域码(6位数)
        region_code = str(random.randint(110000, 659004))
        # 生成年份(4位数)
        year = str(random.randint(1949, 2022))
        # 生成月份(2位数)
        month = str(random.randint(1, 12)).rjust(2, '0')
        # 生成日期(2位数)
        day = str(random.randint(1, 28)).rjust(2, '0')
        # 生成顺序码(3位数)
        order = str(random.randint(1, 999)).rjust(3, '0')
        # 生成校验码(1位数)
        check_code = self.get_check_code(region_code + year + month + day + order)
        # 拼接身份证号码并返回
        self.ID = region_code + year + month + day + order + check_code
        return self.ID

    def get_check_code(self,id17):
        # 系数列表
        factor_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # 校验码列表
        check_code_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        # 根据前17位计算出校验码
        check_code = 0
        for i in range(len(id17)):
            check_code += int(id17[i]) * factor_list[i]
        check_code %= 11
        return check_code_list[check_code]

    def Name(self):
        fistname = ['王','李','张','刘','陈','杨','黄','吴','赵','周','徐','孙','马','朱','胡' ,'林','郭','何','高','罗','郑','梁','谢','宋','唐','许','邓','冯','韩','曹','屈']
        lastname = ['壮', '昱杰', '开虎', '凯信', '永斌', '方洲', '长发', '可人', '天弘', '炫锐', '富明', '俊枫','小玉', '蓝', '琬郡', '琛青', '予舴', '妙妙', '梓茵', '海蓉', '语娜', '馨琦', '晓馥', '佳翊']
        self.name = fistname[random.randint(0,len(fistname))-1] + lastname[random.randint(0,len(lastname))-1]
        return self.name

    def Tuichu(self):
        self.flag = False

    def getinfo(self):
        self.info = []
        self.Name()
        self.info.append(self.name)
        self.SFZ()
        self.info.append(self.ID)
        self.Phone_Num()
        self.info.append(self.phonenum)
        for i in self.info:
            print(i,end='  ')
        print('\n')

    def translate(self):
        # 百度翻译
        # url = 'https://fanyi.baidu.com/sug'
        # key = input(f'请输入要进行翻译的内容：\n')
        # print('')
        # data = {
        #     'kw':key
        # }
        # headers = {
        #     'Referer':'https: // fanyi.baidu.com /',
        #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        #     'Content-Type':'application/json',
        #     'Cookie':'BIDUPSID=25E6CA1EF0ACD1BDBE248E2374675291; PSTM=1681270176; MCITY=-75%3A; BAIDUID=2A78BED0B343D3F0EE508DEE7DD0E8F3:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=Uh5ajFoVkdqb2dqRH5Lc1VkZ2VUZFlrRFpBM3BLYTFjMlJyVVNnfnRNRlhmUHBrRVFBQUFBJCQAAAAAAAAAAAEAAACMu5J~uKHKwMH6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFfv0mRX79Jkb; BDUSS_BFESS=Uh5ajFoVkdqb2dqRH5Lc1VkZ2VUZFlrRFpBM3BLYTFjMlJyVVNnfnRNRlhmUHBrRVFBQUFBJCQAAAAAAAAAAAEAAACMu5J~uKHKwMH6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFfv0mRX79Jkb; BAIDUID_BFESS=2A78BED0B343D3F0EE508DEE7DD0E8F3:SL=0:NR=10:FG=1; ZFY=gPnRyMGu2C1Hssmg00FXAhW:AAI2d2qQ8AgOIlmXsW9w:C; APPGUIDE_10_6_6=1; H_PS_PSSID=39668_39672_39663_39688_39676_39679_39712_39733_39739; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1703492150; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1703492150; ab_sr=1.0.1_ZTMyNTQyMjJkNzkxZWYyMjIxNDdiNDI0YjAzYTkxZTFjYTI4MWU3MzAzMzg1ZWVkZGRmZWIzMzJlZmJmYjllZGYyZmExMzYyZWIzNGU5MTMzMjFiNWRhOWQ4NDQxOTRiYTg0NDI1ZjY3YzFlZGExYWU2MWRhMjU5MzFmNzExYzhmZmRiZDUxODE1ZmJlZDE2YWQxNTg3N2FhMDFiMzBkNDczN2Q3ODM3Mzg0NzQzM2Q5NzAyMTY2ZGM1NjgyODkw'
        # }
        # resp = json.loads(requests.post(url = url,json = data,headers = headers,verify=False).text)
        # trans = resp['data']
        #
        # if trans == []:
        #     print(f'暂无该词翻译，请检查输入\n')
        # else:
        #     for word in trans:
        #         print((word['k'] + '：' + word['v']))
        # print('')
        # 小牛翻译
        apikey = "269970816da01a167d48a9a9dd85e52e"
        url = 'http://api.niutrans.com/NiuTransServer/translation?'
        tar_lan = ''
        tar_lan_num = input("请输入目标语言：\n1:中文\n2:英文\n3:返回上一级\n")
        flag = True
        while flag:
            if tar_lan_num == '1':
                tar_lan = 'zh'
                flag = False
            elif tar_lan_num == '2':
                tar_lan = 'en'
                flag = False
            elif tar_lan_num == '3':

                flag = False
            else:
                tar_lan_num = input("输入错误，请重新输入目标语言：\n1:中文\n2:英文\n3:返回上一级\n")
        if tar_lan != '':
            sentence = input("请输入要翻译的文本：\n")
            data = {
                    "from": 'auto',
                    "to": tar_lan,
                    "apikey": apikey,
                    "src_text": sentence
                    }
            res = requests.post(url, data=data)
            res_dict = json.loads(res.text)
            if "tgt_text" in res_dict:
                result = res_dict['tgt_text']
                print("\n" + result + "\n")
            else:
                result = res
                print(result)
        else:
            print(" ")

if __name__ == '__main__':
    Toolboox()
