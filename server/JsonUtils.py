from flask import Flask, request, jsonify, make_response
import json

# This decorator takes the class/namedtuple to convert any JSON
# data in incoming request to. 
def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

def json_repr(obj):
  """Represent instance of a class as JSON.
  Arguments:
  obj -- any object
  Return:
  String that reprent JSON-encoded object.
  """
  def serialize(obj):
    """Recursively walk object's hierarchy."""
    if isinstance(obj, (bool, int, float)):
      return obj
    elif isinstance(obj, dict):
      obj = obj.copy()
      for key in obj:
        obj[key] = serialize(obj[key])
      return obj
    elif isinstance(obj, list):
      return [serialize(item) for item in obj]
    elif isinstance(obj, tuple):
      return tuple(serialize([item for item in obj]))
    elif hasattr(obj, '__dict__'):
      return serialize(obj.__dict__)
    else:
      return repr(obj) # Don't know how to handle, convert to string
  return json.dumps(serialize(obj))