import subprocess

#ボイスロイド科目名発声ずんだもん
def talk_voiceroid(input_cid, input_str):
    #voiceroid 実行
    try:
        subprocess.run("SeikaSay2.exe -cid {cid} -t \"{msg}\" ".format(cid=input_cid, msg=input_str))
        print(input_str)
    except Exception as e:
        print("音声出力エラー{}\nvoiceboxとassistantSeikaの起動を確認してください".format(e))