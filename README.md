# CraftLaunch 時間計算コマンドラインプラグイン

## 概要

* 通常の計算だけではなく時間計算がしたいなぁと思って作成しました
* 在宅になったので時間計算が必要なのですが毎回Excelで計算するのが面倒になったのです

## インストール方法

* CraftLaunch のインストールフォルダの extension フォルダに commandline_timecalc.py をコピーする
* CraftLaunch の config.py の configure 関数に以下の様に記述する
    
    ```
    import commandline_timecalc
    imp.reload(commandline_timecalc)
    # コマンドライン解析に追加
    window.commandline_list.append(commandline_timecalc.commandline_TimeCalculator())
    ```

## 使い方

* 通常の計算と同じ様にコマンドライン窓に「終了時間時間 - 開始時間」を入力する
* 結果が窓に表示され、クリップボードにコピーされる

    ```
    18:00-8:42 => 9:18:00
    ```

