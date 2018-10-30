import web

urls = ("/.*", "hello")
urls = ('/(.*)/', 'redirect')
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

class redirect:
    def GET(self, path):
        web.seeother('/' + path)
        
if __name__ == "__main__":
    app.run()