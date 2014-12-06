//HTTP Server running on Python that accepts HTTP/JSON from Arduino and sends an HTTP response with a JSON Object
//Used with json_temp_time_LCD

from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods = ['POST','PUT']) #localhost/
def post():
    # Get the parsed contents of the form data
    print request.data
    fd= open("data_file.txt","a")
    fd.write(request.data)
    fd.write("\n")
    fd.close()
    return jsonify({'status':'ok'})

@app.route('/test') #localhost/test
def post_test():
    # Get the parsed contents of the form data
    
    return jsonify({'status':'ok'})



# Run
if __name__ == '__main__':
    
      app.run(
               host = "0.0.0.0", #localhost
               port = 8080,
               debug=True #everytime something is changed, the server restarts
            )
