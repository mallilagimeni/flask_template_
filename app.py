from flask import Flask,render_template
FAI=Flask(__name__)


@FAI.route('/first')
def first():
    return render_template('first.html')


@FAI.route('/sending_data')
def sending_data():
    return render_template('sending_data.html',name='arjun',age=21)

if __name__=='__main__':
    FAI.run(debug=True)