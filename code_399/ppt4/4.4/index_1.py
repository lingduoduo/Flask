# -*- coding: utf-8 -*-
from werkzeug.wrappers import Request,Response

class example(object):
    def __call__(self, environ,start_response):
        start_response( '200 OK',[ ( 'Content-Type','text/plain' ) ] )
        return [ b'hello world~~' ]

        # request = Request( environ )
        # text = "hello world, %s"%( request.args.get( 'a','i love Python' ) )
        # response = Response(text,mimetype="text/plain"  )
        # return response( environ,start_response )


if __name__ == "__main__":
    from werkzeug.serving import run_simple
    app = example()
    run_simple('0.0.0.0', 5000, app)