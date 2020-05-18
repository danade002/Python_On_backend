#!/usr/bin/env python
# coding: utf-8

# In[14]:


import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, this is running on the backend") 
if __name__ == "__main__":
    app=tornado.web.Application([  
        
        (r"/", basicRequestHandler )
    ])
        
    port=8189
    
    app.listen(port)
    print(f"Application is running on port{port}")
    


# In[ ]:




