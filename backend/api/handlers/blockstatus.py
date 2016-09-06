import codecs
import tornado.web
from database import query

class Handler(tornado.web.RequestHandler):
    def get(self, category_id, subcategory_id, branch_id=False):
        result = {}

        db_execute = query.MySqlQuery()

	self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

       	self.write(db_execute.get_block_status(category_id, subcategory_id, branch_id))
	#print(db_execute.get_block_status(category_id, subcategory_id, branch_id))
