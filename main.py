#json フォルダにあるjsonファイルをすべて読み込み、データを取得する

import os
import json

# json ファイルが格納されているフォルダのパス
json_dir = 'json'

# json ファイルの一覧を取得
files = os.listdir(json_dir)
files.sort()

sum_time_to_resolve = 0
# json ファイルの一覧をループ
for file in files:
    # json ファイルのパスを作成
    file_path = os.path.join(json_dir, file)

    # json ファイルを読み込み
    with open(file_path, 'r') as f:
        # json ファイルの内容を取得
        data = json.load(f)
    team_name = data.get("team_name")
    escalation_policy_name = data.get("escalation_policy_name")
    description = data.get("description")
    seconds_to_resolve = data.get("seconds_to_resolve")

    print(f"{team_name} {escalation_policy_name} {description} {seconds_to_resolve}秒 {seconds_to_resolve / 60}分")
    sum_time_to_resolve = sum_time_to_resolve + seconds_to_resolve

print(f"合計対応時間: {sum_time_to_resolve} 秒 ({sum_time_to_resolve / 60}分)")
print(f"平均対応時間: {sum_time_to_resolve / len(files)} 秒 ({(sum_time_to_resolve / len(files)) / 60}分)")
