import codecs
import tornado.web
from machinelearning import clustering

class Handler(tornado.web.RequestHandler):
    def get(self,api_type,line,family,number_of_clusters,number_of_days):
        cluster = clustering.Clusters()

        api_type = codecs.encode(api_type.lower(),'utf-8')
        family = codecs.encode(family.lower(),'utf-8')
        families = family.split(',')

        results = cluster.product_avg_ticket(api_type,int(line),families,int(number_of_clusters),int(number_of_days))

        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

        self.write(results)