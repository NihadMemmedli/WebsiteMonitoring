import time
import logging
import datetime
import os
from jinja2 import Environment, FileSystemLoader


class Logger :
    _logger = None
    def myLogger(self):
        if None == self._logger:
            self._logger=logging.getLogger('log')
            self._logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            handler=logging.FileHandler('logs/'+'log'+ now.strftime("%Y-%m-%d") +'.log')
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)
        return self._logger

class Html_Generator:

    PATH = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(PATH, '../templates')),
        trim_blocks=False)

    def render_template(self,template_filename, context):
        return self.TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

    def create_report(self,good_status,bad_status,bad_context):
        fname = "report/report.html"
        urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
        context = {
            'good_status': good_status,
            'bad_status' : bad_status,
            'bad_context': bad_context
        }
        #
        with open(fname, 'w') as f:
            html = self.render_template('index.html', context)
            f.write(html)

def timer(func):
    def wrap(*args, **kwargs):
        timestamp1 = time.time()
        f = func(*args, *kwargs)
        timestamp2 = time.time()
        timestamp3 = timestamp2 - timestamp1
        return f, timestamp3
    return wrap

