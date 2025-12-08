# third-party imports
from rest_framework.renderers import JSONOpenAPIRenderer    #JSONOpenAPIRenderer is used to render JSON responses for API documentation

# write code for renderers here

class CustomRenderer(JSONOpenAPIRenderer):
    # setting up the default encoding to UTF-8.
    charset = 'utf-8'
    
    # below method intercepts the final response just before it is converted to JSON.
    def render(self, data, media_type=None, renderer_context=None):
        
        # initializing empty dictionary -> this contains HTTP status code and other metadata
        response_data = {}
        
        # check if renderer_context contains data
        if renderer_context:
            # response_status stores the status code
            response_status = renderer_context['response'].status_code
            
            # checking up if status code indicates success, then it will show {'success' : data}
            if 200 <=response_status <= 300:
                response_data['status'] = 'success'
                response_data['data'] = data
            # if their is other than success code then it will show {'error' : data}
            else:
                response_data['status'] = 'error'
                response_data['errors'] = data
                
        else:
            # this line of code ensures rendering doesn't break when context is missing.
            response_data = data
        
        # the transformed response_data is rendered into JSON using parent renderer.
        return super(CustomRenderer, self).render(response_data, renderer_context)