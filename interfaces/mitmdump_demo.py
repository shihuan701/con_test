from mitmproxy import http


def request(flow:http.HTTPFlow):

    if flow.request.pretty_url=='https://www.baidu.com/':
        flow.response = http.HTTPResponse.make(
            200,
            b"hello,shiyi",
            {"Content-Type":"text/html"}
        )


    if 'my.json' in flow.request.pretty_url:
        with open('D:\workspace\python\con_test\datas\my.json') as f:
            flow.response = http.HTTPResponse.make(
                200,
                f.read(),
                {"Content-Type":"application/json"}
            )

