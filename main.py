from flask import Flask, render_template, jsonify

app = Flask(__name__)

CATS = [{
  'id': 1,
  'title': 'Persian Cat',
  'location': 'Bengaluru, India',
  'price': 'Rs. 8,500'
}, {
  'id': 2,
  'title': 'Bengal Cat',
  'location': 'Delhi, India',
  'price': 'Rs. 1,70,000'
}, {
  'id': 4,
  'title': 'British Shorthair',
  'location': 'San Francisco, USA',
  'price': '$ 799'
}]


@app.route("/")
def littlepaws():
  return render_template('homepage.html', cats=CATS, company_name='littlepaws')


@app.route("/api/cats")
def list_cats():
  return jsonify(CATS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
