from funcs_of_subtime import *

#各要素のインデックス
SUB_NAME = 0    #課題名
SUB_PERIOD = 2  #提出期限
SUB_STATE = 4   #提出状況

####################################################
####################################################
#######　一科目あたりの情報を抽出する関数群    #######
### (以下の変数の返り値は全て一次元配列になっている)###

#一科目当たりのレポート名抽出
def extra_report_name(items):
    #レポート名格納配列
    report_name = []
    for i in range(0,len(items)):
        report_name.append(items[i][SUB_NAME])
    return report_name


#課題ごとの提出期限抽出
def extra_submission_period(items):
    #提出期限格納配列
    submission_period = []
    for i in range(0,len(items)):
        submission_period.append(get_submission_deadline_formating(items[i][SUB_PERIOD]))
    return submission_period

#課題ごとの提出状況
def extra_submission_status(items):
    #提出期限格納配列
    submission_status = []
    for i in range(0,len(items)):
        submission_status.append(items[i][SUB_STATE])
    return submission_status

#未提出のものだけの提出期限までの差を求める
def find_diff_with_submission_deadline(sub_state, sub_period):
    dwd = []
    for i in range(0, len(sub_period)):
        if sub_state[i] == '未提出':
            #提出期限までの差を求める
            dwd.append(get_submission_diff_with_deadline(sub_period[i]))
    return dwd