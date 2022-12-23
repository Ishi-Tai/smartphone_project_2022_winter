###########################################################
# 情報ネットワークの課題しか対応していない最初期のバージョン
# 同じ年の課題にしか対応していない     
# 音声メッセージを利用するためには「VOICEVOX」と「assistantSeika（管理者権限で）」を実行しておく
##########################################################

from funcs_of_subtime import *
from funcs_of_extra import *
from funcs_of_get_sigle_SubjectInfo import *
from funcs_of_voice import *
import slack
import os
from dotenv import load_dotenv
import datetime


#提出期限との差のインデックス(変数配列「dwds」で使用する)
YEAR = 0
MONTH = 1
DAY = 2
HOUR = 3
MINUTE = 4

##########################
#######CIDリスト##########
SHIKOKU ='7001'  #四国めたん
ZUNDA = '7007'   #ずんだもん
AOYAMA = '7025'  #青山流星
KENZAKI = '7046' #剣崎雌雄



def main():
    #ログイン情報
    sub_name = "情報ネット"   
    stud_num = input("学籍番号を入力(半角):" )
    pw =input("パスワードを入力(半角): ")

    ##slackBOTの設定
    print("SlackBOT接続中..")
    env_path = ".env"
    load_dotenv(env_path)
    try:
        client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])
        #学校からアクセスするときはこれを使う
        client.proxy = "http://wwwproxy.kanazawa-it.ac.jp:8080"
    except Exception as e:
        print("SlackBOTの設定でエラーが発生しました。\nエラーコード：" + str(e))
        exit()


    #取得した一科目分の２次元配列を取得する
    items = get_SubjectInfo(sub_name, stud_num, pw)
    #一科目当たりのレポート名
    repo_names = extra_report_name(items)
    #各課題の提出期限
    sub_periods = extra_submission_period(items)
    #課題ごとの提出状況抽出
    sub_states = extra_submission_status(items)
    #未提出のものだけの提出期限までの差を求める
    dwds = find_diff_with_submission_deadline(sub_states, sub_periods)

    # repo_names = ['情報ネットワーク(火2)_第1回レポート', '情報ネットワーク(火2)_第2回レポート', '情報ネットワーク(火2)_第3回レポート', '情報ネットワーク(火2)_第4回レポート', '情報ネットワ 回レポート']
    # dwds = [[0, 0, 5, 10, 36],[0, 0, 2, 10, 36],[0, 0, 0, 10, 36]]
    sub_name = sub_name + "ワーク"
    #未提出課題がなかった時はこれで終了
    if len(dwds)== 0:
        talk_voiceroid(SHIKOKU, "課題は見つからなかったわよ。お利口さんねぇ") 
        client.chat_postMessage(channel="bot開発", text="課題は見つからなかったわよ。お利口さんねぇ" + "\nby 四国めたん（シークレットキャラ！）")
        exit()


    #課題数のカウント 
    cnt_report_7 = 0
    cnt_report_2_7 = 0
    cnt_report_0_2 = 0
    cnt_report_dead = 0
    cnt_report_new_year = 0
    #期限日までの差によって声を変える
    for i in range(0, len(dwds)):
        #期限年が現在と同じとき
        if dwds[i][YEAR] == 0:
            if dwds[i][MONTH] == 0:
                if dwds[i][DAY] > 7:
                    cnt_report_7 += 1
                elif dwds[i][DAY] > 2:
                    cnt_report_2_7 += 1
                elif dwds[i][DAY] >= 0:
                    cnt_report_0_2 += 1
                else:
                    cnt_report_dead += 1
        #if dwds[i][YEAR] == 1:

    
    #メッセージテンプレ
    mes_temp1 = sub_name + "で、現在提出日まで１週間以上の課題は、" + str(cnt_report_7) + "個なのだ"
    mes_temp2 = sub_name + "で、期限日まで１週間を切った課題が、" + str(cnt_report_2_7) + "個あります。急ぐのだ！"
    mes_temp3 = sub_name + "で、提出期限がやばい課題が" + str(cnt_report_0_2) + "個あるぞ！さっさとやりやがれ！さもなければ三枚におろすぞ！"
    #情報の出力
    if cnt_report_7 > 0:
        talk_voiceroid(ZUNDA, mes_temp1) 
        client.chat_postMessage(channel="bot開発", text=mes_temp1 + "\nby ずんだもん")
        mes_temp2 = "さらに" + mes_temp2
        mes_temp3 = "さらに" + mes_temp3
    if cnt_report_2_7 > 0:
        talk_voiceroid(ZUNDA, mes_temp2)
        client.chat_postMessage(channel="bot開発", text=mes_temp2  + "\nby ずんだもん")
        mes_temp2 = "さらに" + mes_temp2
        mes_temp3 = "さらに" + mes_temp3
    if cnt_report_0_2 > 0:
        talk_voiceroid(KENZAKI, mes_temp3)
        client.chat_postMessage(channel="bot開発", text=mes_temp3 + "\nby 剣崎雌雄")
    if cnt_report_dead > 0:
        talk_voiceroid(KENZAKI, "提出遅れがあったぞ。この天邪鬼野郎") 
        client.chat_postMessage(channel="bot開発", text="提出遅れやがったな。天邪鬼" + "\nby 剣崎雌雄")




main()
#一日に一回実行
# pasttime = get_nowtime()
# while(1):
#     nowtime = get_nowtime()
#     if (int(nowtime[2]) - int(pasttime[2])) > 1:
#         main()
#         pasttime = nowtime
#     else:
#         print(".")
#         time.sleep(1)





