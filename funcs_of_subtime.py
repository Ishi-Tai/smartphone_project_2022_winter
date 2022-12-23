import datetime
import re

####################################################
####################################################
###########   　提出期限に関する関数群   ############

#提出期限の情報を整形
#'2022/12/06 10:35～2022/12/12 23:59' から ['2022', '12', '12', '23', '59']　に変換
def get_submission_deadline_formating(subjects_limit):
    buf = re.findall(r'\d+',subjects_limit)
    del buf[0:5]
    return buf

#現在時刻を適切な形式で取得（提出期限と比較するため）
def get_nowtime():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    #print(now) 
    now = now.strftime('%Y/%m/%d/%H/%M')
    return now.split("/") #返り値の例：['2022','12','25','12','59']


#提出期限日までの日数を計算する
def get_submission_diff_with_deadline(deadline):
    #現在時刻を求める
    nowtime = get_nowtime()
    #西暦の差を求める
    diff_yy = int(deadline[0]) - int(nowtime[0])
    #月の差を求める
    diff_mm = int(deadline[1]) - int(nowtime[1])
    #日の差を求める
    diff_dd = int(deadline[2]) - int(nowtime[2])
    #時間の差を求める
    diff_hh = int(deadline[3]) - int(nowtime[3])
    #分の差を求める
    diff_MM = int(deadline[4]) - int(nowtime[4])
    #各単位の差をリストにして返す
    diffwithdeadline = [diff_yy, diff_mm, diff_dd, diff_hh, diff_MM]
    return diffwithdeadline #返り値の例：[0, 0, -1, 1, 36] ←　現在時刻と提出期限の年月は同じ、しかし１日遅れていることが確定

