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
            div{
                width: 100px;
                height: 100px;
            }
            .red-box {
                background-color: red;
                margin-left: 50px;
                z-index: 3;
                position: relative;
            }
            .green-box {
                background-color: green;
                position: relative;
                left: 100px;
                top: -30px;
                z-index: 1;
            }
            .blue-box {
                background-color: blue;
                position: absolute;
                left: 30px;
                top: 20px;
                z-index: 2;
            }
            .yellow-box {
                background-color: yellow;
            }
            .pink-box {
                background-color: pink;
                position: sticky;
                left: 100px;
                top: 0;
            }
            .indigo-box {
                background-color: indigo;
            }
            body {
                height: 2000px;
            }
            .p_red {
                background-color: red;
                font-size: 20px;
                float: left;
                width: 400px;
            }
            .p_blue {
                background-color: blue;
                font-size: 20px;
                float: left;
                width: 400px;
            }
            .d_pink {
                background-color: pink;
                font-size: 20px;
                clear: both;
            }
            .p_gold {
                background-color: gold;
                font-size: 20px;
                width: 400px;
                display: inline-block;
            }
            .p_orange {
                background-color: orange;
                font-size: 20px;
                width: 400px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box red-box"></div>
        <div class="box green-box"></div>
        <div class="box blue-box"></div>
        <div class="box yellow-box"></div>
        <div class="box pink-box"></div>
        <div class="box indigo-box"></div>
        <p class="p_red">첫번째 p tag</p>
        <p class="p_blue">두번째 p tag</p>
        <div class="d_pink">div tag</div>
        <p class="p_gold">첫번째 p tag</p>
        <p class="p_orange">두번째 p tag</p>
    </body>
</html>