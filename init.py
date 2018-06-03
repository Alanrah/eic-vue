import os
from flask import Flask, request, url_for, send_from_directory,jsonify,redirect
from flask import make_response
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.preprocessing import image as kimage
from keras.applications.imagenet_utils import preprocess_input
import base64
import shutil
import pymysql
import json
#ip = "10.108.104.228"
ip="10.108.107.106"
def vgg_device(weights_path=None):
    img_width, img_height = 150, 150
    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(6))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    if weights_path:
        model.load_weights(weights_path)
    return model
model_device = vgg_device('categorical-Nadam-lr=0.0002.h5')

def num_recognition(weights_path=None):
    num_classes = 10
    img_width, img_height = 28, 28
    if K.image_data_format() == 'channels_first':
        input_shape = (1, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 1)
    # create model
    model = Sequential()
    model.add(Conv2D(32, (5, 5), input_shape=input_shape, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if weights_path:
        model.load_weights(weights_path)
    return model

model_num = num_recognition('6-layers-CNN.h5')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()+"/static"
print(app.config['UPLOAD_FOLDER'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/static/<dn>/<dp>/<filename>')
def uploaded_file(dn,dp,filename):
    route=app.config['UPLOAD_FOLDER'] + '/'+dn +'/' +dp +'/' 
    return send_from_directory(route,filename)

@app.route('/device', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        fileString = request.form['fileString']
        filename = request.form['filename']
        print(filename)
        if fileString and allowed_file(filename):
            imgdata= base64.b64decode(fileString)
            kimagePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            fileImage = open(kimagePath, 'wb')
            fileImage.write(imgdata)
            fileImage.close()
            img = kimage.load_img(kimagePath, target_size=(150, 150))
            x = kimage.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            preds = model_device.predict(x)
            proba = model_device.predict_proba(x, verbose=0)
            pred = model_device.predict_classes(x, verbose=0)
            class_index = ['交换机', '塔式服务器', '打印机', '机架式服务器', '机柜', '路由器']
            class_index_en = ['switch', 'towerServer', 'printer', 'rockServer', 'cabinet', 'router']
            to = class_index_en[pred[0]]+'/'+filename
            move_to = shutil.copy(kimagePath, app.config['UPLOAD_FOLDER']+'/devicePic/'+to)
            save_url = 'http://'+ip+':5000/static/devicePic/'+to
            result = save_url+','+class_index[pred[0]]
            print(result)
            rst = make_response(result)
            rst.set_cookie('url',save_url)
            rst.headers['Access-Control-Allow-Origin'] = '*'
            rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            #rst.headers[' Access-Control-Allow-Credentials']=True
            allow_headers = "Referer,Accept,Origin,User-Agent,Content-Type"
            rst.headers['Access-Control-Allow-Headers'] = allow_headers
            return rst, 201

@app.route('/position', methods=['GET', 'POST'])#处理数字图片
def upload_numfile():
    if request.method == 'POST':
        fileString = request.form['fileString']
        filename = request.form['filename']
        print(filename)
        if fileString and allowed_file(filename):
            imgdata= base64.b64decode(fileString)
            kimagePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            fileImage = open(kimagePath, 'wb')
            fileImage.write(imgdata)
            fileImage.close()
            img = kimage.load_img(kimagePath, grayscale=True, target_size=(28, 28))
            x = kimage.img_to_array(img)
            x = x.reshape((1,) + x.shape)
            proba = model_num.predict_proba(x, verbose=0)
            result = model_num.predict_classes(x, verbose=0)
            result = str(result[0])
            to = result + '/' + filename
            move_to = shutil.copy(kimagePath, app.config['UPLOAD_FOLDER'] + '/numPic/' + to)
            save_url = 'http://'+ip+':5000/static/numPic/' + to
            result = save_url + ',' + result
            print(result)
            rst = make_response(result)
            rst.headers['Access-Control-Allow-Origin'] = '*'
            rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            allow_headers = "Referer,Accept,Origin,User-Agent,Content-Type"
            #rst.headers[' Access-Control-Allow-Credentials'] = True
            rst.headers['Access-Control-Allow-Headers'] = allow_headers
            return rst, 201

@app.route('/fetch', methods=['GET', 'POST'])
def fetch_data_from_db():
    if request.method == 'POST':
        user = request.form['user']
        if user:
            #grant all privileges on *.* to catherine@10.108.107.106 identified by 'bnrc123';
            conn = pymysql.connect(host="10.108.104.228", port=3306, user='catherine', passwd='bnrc123', db='machineRoom', charset='UTF8')
            cur = conn.cursor()
            id_sql = "select u_id from admin where u_name='"+ user +"';"
            cur.execute(id_sql);
            x=cur.fetchall();
            id=x[0][0]

            room_sql = "select * from roomInfo where r_id in (select r_id from manageRoom where u_id= "+str(id)+");"
            cur.execute(room_sql);
            room = cur.fetchall();
            room_arr=[]
            for i in range(len(room)):
                room_str = {'r_id': 0, 'r_name': "", 'r_owner': "", 'r_pos': "", 'r_length': 0, 'r_width': 0,"r_height":0,"r_pic":""}
                room_str['r_id']=room[i][0]
                room_str['r_name'] = room[i][1]
                room_str['r_owner'] = room[i][2]
                room_str['r_pos'] = room[i][3]
                room_str['r_length'] = room[i][4]
                room_str['r_width'] = room[i][5]
                room_str['r_height'] = room[i][6]
                room_str['r_pic'] = room[i][7]
                room_arr.append(room_str)

            sql="select * from deviceInfo,deviceDetailInfo where r_id=any(select r_id from manageRoom where u_id=(select u_id from admin where u_name= '"+ user +"')) and deviceInfo.d_id=deviceDetailInfo.d_id;"
            cur.execute(sql);
            results = cur.fetchall();#获取查询的所有记录
            device_arr=[]
            for i in range(len(results)):
                json_str = {'u_id':id,'r_id': 0, 'c_id': 0, 'd_id': 0, 'd_name': "", 'd_u': 0, 'last_modified': "", 'c_un': 0,
                            'd_status': 0, 'd_id': 0, 'd_length': 0, 'd_width': 0, 'd_height': 0, 'd_pic': "",
                            'pos_pic': "", 'd_producer': "", 'd_seq': ""}
                json_str['r_id']=results[i][0]
                json_str['c_id'] = results[i][1]
                json_str['d_id'] = results[i][2]
                json_str['d_name'] = results[i][3]
                json_str['d_u'] = results[i][4]
                #json_str['last_modified'] = results[i][5]
                json_str['c_un'] = results[i][6]
                json_str['d_status'] = results[i][7]
                json_str['d_id'] = results[i][8]
                json_str['d_length'] = results[i][9]
                json_str['d_width'] = results[i][10]
                json_str['d_height'] = results[i][11]
                json_str['d_pic'] = results[i][12]
                json_str['pos_pic'] = results[i][13]
                json_str['d_producer'] = results[i][14]
                json_str['d_seq'] = results[i][15]
                device_arr.append(json_str)
            result=[room_arr,device_arr]
            result = json.dumps(result)
            cur.close()
            conn.close()
            rst = make_response(result)
            rst.headers['Access-Control-Allow-Origin'] = '*'
            rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            allow_headers = "Referer,Accept,Origin,User-Agent,Content-Type"
            #rst.headers[' Access-Control-Allow-Credentials'] = True
            rst.headers['Access-Control-Allow-Headers'] = allow_headers
            return rst, 200
    return  400
@app.route('/operate/delete',methods=['GET', 'POST'])
def operate_data_from_db():
    if request.method == 'POST':
        user = request.form['user']
        device_id = request.form['device_id']
        if user :
            conn = pymysql.connect(host="10.108.104.228", port=3306, user='catherine', passwd='bnrc123',
                                   db='machineRoom', charset='UTF8')
            cur = conn.cursor()
            sql1 = "delete from deviceInfo where d_id="+str(device_id)+";"
            cur.execute(sql1)
            result1 = cur.fetchall();
            sql2 ="delete from deviceDetailInfo where d_id="+str(device_id)+";"
            cur.execute(sql2);
            result2 = cur.fetchall();
            cur.close()
            conn.commit()
            conn.close();
            result="ok"
            rst = make_response(result)
            rst.headers['Access-Control-Allow-Origin'] = '*'
            rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            allow_headers = "Referer,Accept,Origin,User-Agent,Content-Type"
            # rst.headers[' Access-Control-Allow-Credentials'] = True
            rst.headers['Access-Control-Allow-Headers'] = allow_headers
            return rst,200
    return 400


@app.route('/operate/addroom',methods=['GET', 'POST'])
def add_room_from_db():
    if request.method == 'POST':
        u_id = request.form['uid']
        r_name = request.form['name']
        r_owner = request.form['owner']
        r_pos = request.form['pos']
        r_length = request.form['length']
        r_width = request.form['width']
        r_height = request.form['height']
        if u_id :
            conn = pymysql.connect(host="10.108.104.228", port=3306, user='catherine', passwd='bnrc123',
                                   db='machineRoom', charset='UTF8')
            cur = conn.cursor()
            sql1 = "insert into roomInfo (r_name, r_owner, r_pos, r_length, r_width, r_height , create_datetime) values('"+r_name+"','"+r_owner+"','"+r_pos+"',"+r_length+","+r_width+","+r_height+",now());"
            get_id ="SELECT @@IDENTITY;"
            cur.execute(sql1)
            cur.execute(get_id)
            result1 = cur.fetchall();
            r_id  = result1[0][0]
            sql3 = "insert into manageRoom(u_id,r_id) values ("+str(u_id)+","+str(r_id)+");"
            cur.execute(sql3);
            result3 = cur.fetchall();
            cur.close()
            conn.commit()
            conn.close();
            result="ok"
            rst = make_response(result)
            rst.headers['Access-Control-Allow-Origin'] = '*'
            rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            allow_headers = "Referer,Accept,Origin,User-Agent,Content-Type"
            # rst.headers[' Access-Control-Allow-Credentials'] = True
            rst.headers['Access-Control-Allow-Headers'] = allow_headers
            return rst,200
    return 400

@app.route('/operate/insertDevice',methods=['GET', 'POST'])
def insert_device_from_db():
    if request.method == 'POST':
        r_id = int(request.form['r_id'])
        c_id = int(request.form['c_id'])
        d_name = request.form['d_name']
        d_u = int(request.form['d_u'])
        d_pic = request.form['d_pic']
        pos_pic = request.form['pos_pic']
        print(r_id,c_id,d_name,d_u,d_pic,pos_pic)
        if r_id :
            conn = pymysql.connect(host="10.108.104.228", port=3306, user='catherine', passwd='bnrc123',
                                   db='machineRoom', charset='UTF8')
            cur = conn.cursor()
            sql1=""
            sql2=""
            d_id = ""
            if c_id>0:#设备放在机柜里
                sql1 = "insert into deviceInfo (r_id, c_id, d_name, d_u, last_modified) values('" + str(r_id) + "','" + str(c_id) + "','" + d_name + "'," + str(d_u) + ",now());"
                get_id = "SELECT @@IDENTITY;"
                cur.execute(sql1)
                cur.execute(get_id)
                result1 = cur.fetchall();
                d_id = result1[0][0]
            elif c_id==0:
                sql1 = "insert into deviceInfo (r_id, c_id, d_name, d_u, last_modified) values('" + str(
                    r_id) + "','" + str(c_id) + "','" + d_name + "'," + str(0) + ",now());"
                get_id = "SELECT @@IDENTITY;"
                cur.execute(sql1)
                cur.execute(get_id)
                result1 = cur.fetchall();
                d_id = result1[0][0]
            else:#是机柜
                sql1 = "insert into deviceInfo (r_id, d_name, d_u, last_modified) values('" + str(r_id) + "','" + d_name + "'," + str(0) + ",now());"
                get_id = "SELECT @@IDENTITY;"
                cur.execute(sql1)
                cur.execute(get_id)
                result1 = cur.fetchall();
                d_id = result1[0][0]
                update = "update deviceInfo set c_id="+str(d_id)+" where d_id = "+str(d_id)+";"
                cur.execute(update)
            sql2 = "insert into deviceDetailInfo (d_id,d_pic,pos_pic) values(" + str(d_id) + ",'" + d_pic + "','" + pos_pic + "');"
            cur.execute(sql2)
            cur.close()
            conn.commit()
            conn.close();
            result = "ok"
            rst = make_response(result)
            rst.headers['Access-Control-Allow-Origin'] = '*'
            rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            allow_headers = "Referer,Accept,Origin,User-Agent,Content-Type"
            # rst.headers[' Access-Control-Allow-Credentials'] = True
            rst.headers['Access-Control-Allow-Headers'] = allow_headers
            return rst, 200

if __name__ == '__main__':
    app.run(host=ip,port = 5000)

