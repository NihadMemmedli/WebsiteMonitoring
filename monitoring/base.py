from main.helper.helper import *
import requests

class Monitoring:
    def __init__(self,urls):
        self._good_status = []
        self._bad_status = []
        self._bad_context = []
        self._urls = urls

    @timer
    def request(self,url):
        try:
            r = requests.get(url)
            return r
        except:
            logger.error("Request is not worked")

    @staticmethod
    def check_status(respond):
        if respond.status_code == 200:
            return True
        else:
            return False
    @staticmethod
    def check_context(context,respond):
        if context.lower() in respond.text.lower():
            return True
        else:
            return False

    def html_generator(self):
        gen = Html_Generator()
        gen.create_report(self._good_status,self._bad_status,self._bad_context)

    def job(self):
        for item in self._urls:
            url = item[0]
            context = item[1]
            r = self.request(url)
            resp = r[0]
            time = r[1]
            if self.check_context(context, resp):
                logger.info("url {} + status {} + reponse time {} ".format(url, resp.status_code, time))
                if url not in self._good_status:
                    self._good_status.append(url)

            elif self.check_status(resp):
                logger.info("url {} + status {} + reponse time {} ".format(url, resp.status_code, time))
                logger.error("Context not matching {} ".format(url))
                if url not in self._bad_context:
                    self._bad_context.append(url)
            else:
                logger.error("url {} + status {} + reponse time {} ".format(url, resp.status_code, time))
                if url not in self._bad_context:
                    self._bad_status.append(url)

        self.html_generator()

s = Logger()
logger = s.myLogger()