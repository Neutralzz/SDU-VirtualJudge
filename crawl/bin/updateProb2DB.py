from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
#from .. import *
from crawl.spiders.problem_spider import HduProblemSpider
from scrapy.utils.project import get_project_settings

@defer.inlineCallbacks
def func():
	print("in crawl")
	for i in range(1200,1299):
		print("start crawl HDUOJ : %d"%i)
		yield runner.crawl('hdu_problem',problem_id=str(i))
	reactor.stop()


configure_logging()
runner = CrawlerRunner(get_project_settings())
print("begin");

func()
reactor.run() 

"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
for i in range(1000,1100):
	process.crawl('hdu_problem', problem_id=str(i))
process.start() # the script will block here until the crawling is finished
"""