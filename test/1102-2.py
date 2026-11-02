<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>11월 2일</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                font-family: "맑은 고딕";
                font-size: 0;
            }
            div {
                width: 500px;
                height: 500px;
            }
            .parent {
                background-color: red;
                width: 500px;
                height: 500px;
                overflow: scroll;
            }
            .child {
                width: 700px;
                height: 500px;
                background-image: url("../images/fantasy.jpg");
                background-repeat: no-repeat;
                background-size: 500px;
                background-attachment: fixed;
            }
            .mygreen {
                width: 500px;
                height: 500px;
                background: green url("../images/fantasy.jpg") no-repeat center/200px fixed;
            }
        </style>
    </head>
    <body>
        <div class="parent">
            <div class="child"></div>
        </div>
        <div class="mygreen"></div>
    </body>
</html>