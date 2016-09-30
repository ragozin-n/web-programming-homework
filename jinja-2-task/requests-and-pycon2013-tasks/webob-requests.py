from webob import Request

wiki_request = Request.blank("wikipedia/Lake_Chaubunagungamaug")
wiki_request.host = 'wikipedia.org'
wiki_request.environ["SERVER_NAME"] = 'wikipedia.org'
wiki_request.accept = "text/html"
wiki_request.user_agent = "User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"

httpbin_request_1 = Request.blank("ip")
httpbin_request_1.host = 'httpbin.org'
httpbin_request_1.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_1.accept = '*/*'

httpbin_request_2 = Request.blank("get?foo=bar&1=2&2/0&error=True")
httpbin_request_2.host = 'httpbin.org'
httpbin_request_2.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_2.accept = '*/*'

httpbin_request_3 = Request.blank("post")
httpbin_request_3.host = 'httpbin.org'
httpbin_request_3.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_3.method = 'POST'
content = "foo=bar&1=2&2%2F0=&error=True".encode('utf-8')
httpbin_request_3.content_type = "application/x-www-form-urlencoded"
httpbin_request_3.body = content
httpbin_request_3.content_length = len(content)
httpbin_request_3.headers['Connection'] = 'close'

httpbin_request_4 = Request.blank('cookies/set?country=Ru')
httpbin_request_4.host = 'httpbin.org'
httpbin_request_4.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_4.accept = '*/*'
httpbin_request_4.headers['Connection'] = 'close'

httpbin_request_5 = Request.blank("cookies")
httpbin_request_5.host = 'httpbin.org'
httpbin_request_5.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_5.accept = '*/*'
httpbin_request_5.headers['Connection'] = 'close'

httpbin_request_6 = Request.blank('redirect/4')
httpbin_request_6.host = 'httpbin.org'
httpbin_request_6.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_6.accept = '*/*'
httpbin_request_6.headers['Connection'] = 'close'

httpbin_request_7 = Request.blank("post")
httpbin_request_7.host = 'httpbin.org'
httpbin_request_7.environ["SERVER_NAME"] = 'httpbin.org'
httpbin_request_7.method = 'POST'
content = "firstname=Nikita&lastname=Ragozin&group=fo340001&message=empty_message".encode('utf-8')
httpbin_request_7.content_length = len(content)
httpbin_request_7.content_type = "application/x-www-form-urlencoded"
httpbin_request_7.body = content
httpbin_request_7.headers['Connection'] = 'close'

requests = [wiki_request,
			httpbin_request_3,
			httpbin_request_2,
			httpbin_request_1,
			httpbin_request_4,
			httpbin_request_5,
			httpbin_request_6,
			httpbin_request_7]

for request in requests:
	responce = request.get_response()
	responce.content_type = 'text/plain'
	responce.charset = 'utf-8'
	print(responce)
	print("\n\n------------\n\n")

