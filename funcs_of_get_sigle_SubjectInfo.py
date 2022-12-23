from helium import *
import time

################この関数で直したいこと####################
#情報ネットワーク以外にも対応させる
#ネットワークの通信状況に応じてスクレイピングの待ち時間を変化させる
#高速化
#講義日をもとに提出期限日が3月31日の時も課題提出を予測できるようにする
#スレッド処理の実装

#情報ネットワークの課題をスクレイピングするための関数（heliumを活用）
def get_SubjectInfo(sub_name, student_number, password):
    start_chrome('https://navi.mars.kanazawa-it.ac.jp/portal/student')
    write(student_number, into='学籍番号')
    write(password, into='パスワード')
    click('ログイン')
    click('KITナビ')
    click(sub_name)
    print("ページ遷移中...")
    list=[]
    items=[]
    for i in range (0, 15):
        try:
            click("【レポート課題】：情報ネットワーク(火2)_第" + str(i+1) + "回レポート")
            wait_until(S(".JugyoSummary").exists)
            item = (find_all(S(".JugyoSummary > tbody > tr > td")))
            Config.implicit_wait_secs = 4
            print("第{}週目の課題情報取得完了".format(i+1))
            store=[]
            for j in range(len(item)):
                store.append(item[j].web_element.text)
            items.append(store)
            #items[i][0] = str(i+1) + items[i][0] #課題名の先頭に番号を振る（レポートが一日一つだけでている場合のみ、正常に稼働する）
            click("閉じる")
            time.sleep(3)
        except Exception as e:
            print("{}第{}週目の課題は見つからなかったよ".format(e, i+1))
    
    print ("~finish~")
    kill_browser()
    return items

