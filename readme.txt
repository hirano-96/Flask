おべんきょ

Lv1 WebにおけるREST APIとは何か
    参考資料
    ・RESTful APIとは何なのか
        https://qiita.com/NagaokaKenichi/items/0647c30ef596cedf4bf2
    ・REST APIとは？ざっくりと理解してみる【初心者向け】の「WebにおけるRESTの４原則を図にすると..」欄
        https://tech.012grp.co.jp/entry/rest_api_basics
    ・ステートレスとは
        https://qiita.com/mtakehara21/items/efcbbc3ba58a62c10eb6
    Question
    1.REST APIは通信プロトコルに何を利用するか
    2.REST APIではすべての情報が一意のXXXで表現される。XXXは何か
    3.REST APIはステートレスでやり取りされる。ステートレスとはどういうものか
    4.REST APIは情報の操作をHTTPメソッドで定義する。HTTPメソッドの代表的な項目を4つ挙げよ
    5.REST APIとRESTful APIに違いはあるか

    Answer
    1.HTTP
    2.URL
    3.サーバ側が、受け取った情報を保持しないもの。
    　そのため、すべての情報を渡す必要があり、データ量は多くなるが、
    　複数のWebサーバにまたがって処理を行うことが容易になる。
    4.GET,POST,PUT,DELETE
    5.ない。



Lv2 REST APIの実装とテスト
    事前準備
    ・仮想環境を用意する
        https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

    ・python, flaskのインストール
        python　→　入ってた
        flask　→　pip install flask

    ・postmanのインストール
        なんかいけた

    参考資料
    ・【入門】Flask + Python で REST API を設計・実装
        https://hogetech.info/network/web/restapi
    ・参考資料をもとに以下を確認すること
        1. サンプルコードを実行し、サーバーが立ち上がること
            app.py作成（中身はコピー）
            仮想環境にいる状態で　flask run

        2. postmanからGETリクエストを送り、ツイートが1件も表示されないこと
            https://ponsuke-tarou.hatenablog.com/entry/2021/01/24/171658

            CollectionsにGetRequestを作成し、
            app.pyで指定しているGet用のURLに送る
            →　返ってきた（データはないので空の状態。少なくとも404にはならなくなった。）

        3. postmanからPOSTリクエストを送り、ツイートが登録できること
            3.1. HTTPメソッドはPOSTになっているか
                CollectionsにPostRequestを作成

            3.2. Body部に必要な項目は確認したか
                app.pyのPOSTメソッドを確認し、パラメータとして「tweet」項目を渡すように
                PostRequestに設定

            3.3. 送信する形式はJSONに指定したか
                json形式で渡すように指定

        4. postmanからGETリクエストを送り、3.で登録したツイートが表示されること
            2で作成したGetRequestを再発行

        5. postmanからDELETEリクエストを送り、3.で登録したツイートが削除できること
            CollectionsにDeleteRequestを作成し、URL内でIDを指定して発行

        6. postmanからGETリクエストを送り、5.で削除したツイートが表示されないこと
            2で作成したGetRequestを再発行
            
        7. サンプルコードにGETリクエストを追加し、指定したidのツイートを取得するAPIを実装できること
            7.1. コードを記述後、反映させるためにサーバーの再起動はしたか
            できた。



Lv3 JWT(読み: ジョット) = JSON Web Tokenとは何か
    とりあえず試してみる
    ・FlaskAPIでJWT認証を実装する(後編) ※前編はJWT自体の実装なので読まなくていい
        https://www.w2solution.co.jp/tech/2022/08/18/flaskapi%E3%81%A7jwt%E8%AA%8D%E8%A8%BC%E3%82%92%E5%AE%9F%E8%A3%85%E3%81%99%E3%82%8B%EF%BC%88%E5%BE%8C%E7%B7%A8%EF%BC%89/

    概要を知りたい場合
    ・OAuth 2.0 / OIDC を理解する上で重要な3つの技術仕様
        https://logmi.jp/tech/articles/322822
        動画版(~30分くらいまでで解説されてる): https://www.youtube.com/watch?v=PKPj_MmLq5E


