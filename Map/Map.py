class Map():

    def __init__(self,filename):
        self.filename = filename
    
    def draw_html(self,d):
        file = open(self.filename, 'r')
        style = ' '.join(['#%s { fill:%s!IMPORTANT; }' % (key, value) for (key, value) in d.items()])
        html = "<html><head><style>" + style + "</style></head><body>" + file.read() + "</body></html>"
        return html