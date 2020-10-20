
import yaml
import os
class GetData():

    def get_basesrc(self):
        BASESRC = os.getcwd()
        return BASESRC

    def get_datas(self,filepath):
        with open(filepath,encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        return datas