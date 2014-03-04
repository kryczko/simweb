#!//opt/local/bin/python2.7

import web

urls = ('/', 'index')

class index:
    def GET(self):
        return "Hello, world!\n\n\n I like Caitlin :)"
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()