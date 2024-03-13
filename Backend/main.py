from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template, jsonify
import mysql.connector
import os
import datetime


class DBManager:
    # Connect to MySQL
    def __init__(self, database='dyte', host="192.168.1.200", user="root", password="honda4104", password_file=""):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    # Used to Create Table
    def create_db(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS log (level VARCHAR(25), message VARCHAR(255), resourceId VARCHAR(50), timestamp TIMESTAMP, traceId VARCHAR(50), spanId VARCHAR(50), commit VARCHAR(50), parentResourceId VARCHAR(50));')
        self.cursor.execute('CREATE INDEX level_idx ON log(level);')
        self.cursor.execute('CREATE INDEX message_idx ON log(message);')
        self.cursor.execute('CREATE INDEX resourceId_idx ON log(resourceId);')
        self.cursor.execute('CREATE INDEX traceId_idx ON log(traceId);')
        self.cursor.execute('CREATE INDEX spanId_idx ON log(spanId);')
        self.cursor.execute('CREATE INDEX commit_idx ON log(commit);')
        self.cursor.execute(
            'CREATE INDEX parentResourceId_idx ON log(parentResourceId);')
        self.cursor.execute(
            "INSERT INTO log (level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId) VALUES ('success', 'success to connect to DB 1', 'server-1', '2023-09-15 08:00:00', 'abc-quc64qfa-1', 'span-iugrzl1z', '447cefd', 'server-7079') ,('error', 'error to connect to DB 2', 'server-2', '2023-09-15 08:00:00', 'abc-oyypb22q-2', 'span-s8kq74zj', '5789b70', 'server-5147') ,('success', 'success to connect to DB 3', 'server-3', '2023-09-15 08:00:00', 'abc-xzdskw6r-3', 'span-adky3bf8', '33dd8c1', 'server-6248') ,('error', 'error to connect to DB 4', 'server-4', '2023-09-15 08:00:00', 'abc-pmo7mw2v-4', 'span-a48q17on', '1f28729', 'server-7605') ,('success', 'success to connect to DB 5', 'server-5', '2023-09-15 08:00:00', 'abc-i9ms7ua5-5', 'span-9nkto45h', '57156bc', 'server-2088') ,('error', 'error to connect to DB 6', 'server-6', '2023-09-15 08:00:00', 'abc-oqaspeii-6', 'span-ha5xq34l', '36e6455', 'server-8891') ,('success', 'success to connect to DB 7', 'server-7', '2023-09-15 08:00:00', 'abc-3lcnlsg2-7', 'span-b8k0k2j4', '36546d6', 'server-3609') ,('error', 'error to connect to DB 8', 'server-8', '2023-09-15 08:00:00', 'abc-7pfx07to-8', 'span-6alnq5tq', '3a850ee', 'server-7511') ,('success', 'success to connect to DB 9', 'server-9', '2023-09-15 08:00:00', 'abc-edgdlo3m-9', 'span-ucr66g0z', '26ddaa1', 'server-7661') ,('error', 'error to connect to DB 10', 'server-10', '2023-09-15 08:00:00', 'abc-4cnwn1xt-10', 'span-miw5bvkl', '374027a', 'server-5035') ,('success', 'success to connect to DB 11', 'server-11', '2023-09-15 08:00:00', 'abc-exg2wzbb-11', 'span-um6dqd0z', '4298073', 'server-5696') ,('error', 'error to connect to DB 12', 'server-12', '2023-09-15 08:00:00', 'abc-v73a0io9-12', 'span-14l8fqst', 'dc0b8b', 'server-9504') ,('success', 'success to connect to DB 13', 'server-13', '2023-09-15 08:00:00', 'abc-t0qp1w7s-13', 'span-58ozk5hi', '2d227ab', 'server-7863') ,('error', 'error to connect to DB 14', 'server-14', '2023-09-15 08:00:00', 'abc-obc3w1cj-14', 'span-zofrcz6w', '3d084ee', 'server-8992') ,('success', 'success to connect to DB 15', 'server-15', '2023-09-15 08:00:00', 'abc-icc41e1s-15', 'span-jfaoiql4', 'f8aa94', 'server-6652') ,('error', 'error to connect to DB 16', 'server-16', '2023-09-15 08:00:00', 'abc-t0yq4kb4-16', 'span-t0n6pv4m', '56bffcb', 'server-3348') ,('success', 'success to connect to DB 17', 'server-17', '2023-09-15 08:00:00', 'abc-jug0vf58-17', 'span-7d1tjpou', '2575d85', 'server-9032') ,('error', 'error to connect to DB 18', 'server-18', '2023-09-15 08:00:00', 'abc-cayesgyk-18', 'span-yy3q78rz', 'f27b75', 'server-6584') ,('success', 'success to connect to DB 19', 'server-19', '2023-09-15 08:00:00', 'abc-0mw7q6sa-19', 'span-lgicziro', '38c1fff', 'server-6302') ,('error', 'error to connect to DB 20', 'server-20', '2023-09-15 08:00:00', 'abc-2s73tna5-20', 'span-dkhge62p', '2ad7a66', 'server-9892') ,('success', 'success to connect to DB 21', 'server-21', '2023-09-15 08:00:00', 'abc-wzxok52o-21', 'span-0qc335x3', '1d84c88', 'server-9910') ,('error', 'error to connect to DB 22', 'server-22', '2023-09-15 08:00:00', 'abc-9nm1njxs-22', 'span-457xy1xn', '39435e6', 'server-8910') ,('success', 'success to connect to DB 23', 'server-23', '2023-09-15 08:00:00', 'abc-wh6b3eo0-23', 'span-e3v27ou3', 'fdc225', 'server-7396') ,('error', 'error to connect to DB 24', 'server-24', '2023-09-15 08:00:00', 'abc-daf5lr43-24', 'span-i91temzz', '4508341', 'server-4612') ,('success', 'success to connect to DB 25', 'server-25', '2023-09-15 08:00:00', 'abc-pm60xb64-25', 'span-u6k6t802', '557a084', 'server-9807') ,('error', 'error to connect to DB 26', 'server-26', '2023-09-15 08:00:00', 'abc-kweqt2wk-26', 'span-fk4m5uux', '2777a05', 'server-4389') ,('success', 'success to connect to DB 27', 'server-27', '2023-09-15 08:00:00', 'abc-pxioqmyy-27', 'span-79c6a2ca', '4f452bc', 'server-8315') ,('error', 'error to connect to DB 28', 'server-28', '2023-09-15 08:00:00', 'abc-r8qp8pvo-28', 'span-l41pzo6h', '32f7215', 'server-5914') ,('success', 'success to connect to DB 29', 'server-29', '2023-09-15 08:00:00', 'abc-03soht78-29', 'span-42zqygys', '537dc31', 'server-5199') ,('error', 'error to connect to DB 30', 'server-30', '2023-09-15 08:00:00', 'abc-54wn9vsk-30', 'span-wqhak3rj', '44dd302', 'server-9590') ,('success', 'success to connect to DB 31', 'server-31', '2023-09-15 08:00:00', 'abc-imoktgyk-31', 'span-e8sssmw8', '3aabbc3', 'server-4868') ,('error', 'error to connect to DB 32', 'server-32', '2023-09-15 08:00:00', 'abc-6asthidq-32', 'span-5lkcpzlq', '1b67d66', 'server-3101') ,('success', 'success to connect to DB 33', 'server-33', '2023-09-15 08:00:00', 'abc-smc9fiak-33', 'span-m6i52eyr', '14e7d27', 'server-5838') ,('error', 'error to connect to DB 34', 'server-34', '2023-09-15 08:00:00', 'abc-56fnapqe-34', 'span-45oov1zl', '459243a', 'server-2531') ,('success', 'success to connect to DB 35', 'server-35', '2023-09-15 08:00:00', 'abc-c4q1f2sy-35', 'span-a7yjqain', '4cf08f9', 'server-4438') ,('error', 'error to connect to DB 36', 'server-36', '2023-09-15 08:00:00', 'abc-avpb3ira-36', 'span-yamueqee', '56a888a', 'server-2956') ,('success', 'success to connect to DB 37', 'server-37', '2023-09-15 08:00:00', 'abc-evtyg0pm-37', 'span-x69om367', '42d1e81', 'server-5488') ,('error', 'error to connect to DB 38', 'server-38', '2023-09-15 08:00:00', 'abc-tl00jyva-38', 'span-6s1pwtgf', '5aaefa8', 'server-4703') ,('success', 'success to connect to DB 39', 'server-39', '2023-09-15 08:00:00', 'abc-7bfdyome-39', 'span-3dqtxd58', '57bd023', 'server-7171') ,('error', 'error to connect to DB 40', 'server-40', '2023-09-15 08:00:00', 'abc-0vyb8qg3-40', 'span-1l38211a', '29702d8', 'server-1866') ,('success', 'success to connect to DB 41', 'server-41', '2023-09-15 08:00:00', 'abc-xy0da95w-41', 'span-64sal6fs', '13f2520', 'server-9045') ,('error', 'error to connect to DB 42', 'server-42', '2023-09-15 08:00:00', 'abc-x64l3yjd-42', 'span-1set7w6d', 'a74257', 'server-9024') ,('success', 'success to connect to DB 43', 'server-43', '2023-09-15 08:00:00', 'abc-50099qqr-43', 'span-80zmzqbr', '4fefea4', 'server-3830') ,('error', 'error to connect to DB 44', 'server-44', '2023-09-15 08:00:00', 'abc-z264kdeq-44', 'span-9vbksd5g', '39e4d59', 'server-4537') ,('success', 'success to connect to DB 45', 'server-45', '2023-09-15 08:00:00', 'abc-4swdfg8v-45', 'span-muyhcggz', '12bf9cf', 'server-9044') ,('error', 'error to connect to DB 46', 'server-46', '2023-09-15 08:00:00', 'abc-ush6oxbm-46', 'span-2ozp06ri', '3c220d2', 'server-6969') ,('success', 'success to connect to DB 47', 'server-47', '2023-09-15 08:00:00', 'abc-uc1py0ch-47', 'span-fong370h', '2af7542', 'server-7112') ,('error', 'error to connect to DB 48', 'server-48', '2023-09-15 08:00:00', 'abc-cnqc5x7c-48', 'span-lhw9mfvf', 'bb9a4c', 'server-1938') ,('success', 'success to connect to DB 49', 'server-49', '2023-09-15 08:00:00', 'abc-sbjqvt48-49', 'span-z7pv0mq2', '5b12899', 'server-9112') ,('error', 'error to connect to DB 50', 'server-50', '2023-09-15 08:00:00', 'abc-7qucfqnn-50', 'span-j9k65agu', '3c36fc9', 'server-1417') ,('success', 'success to connect to DB 51', 'server-51', '2023-09-15 08:00:00', 'abc-siy57a58-51', 'span-qu0zkciq', 'eda23b', 'server-4973') ,('error', 'error to connect to DB 52', 'server-52', '2023-09-15 08:00:00', 'abc-3l1rapg8-52', 'span-6pg4bg9x', '1ebb2ba', 'server-7524') ,('success', 'success to connect to DB 53', 'server-53', '2023-09-15 08:00:00', 'abc-lq6xnjm9-53', 'span-05qv0f4a', '1e10fd5', 'server-5096') ,('error', 'error to connect to DB 54', 'server-54', '2023-09-15 08:00:00', 'abc-yochq858-54', 'span-4su2wts6', '29458e1', 'server-7715') ,('success', 'success to connect to DB 55', 'server-55', '2023-09-15 08:00:00', 'abc-42mf5shz-55', 'span-812g1zwk', '3366be7', 'server-5710') ,('error', 'error to connect to DB 56', 'server-56', '2023-09-15 08:00:00', 'abc-8dc5bao8-56', 'span-ft4y9rqb', '2341555', 'server-4603') ,('success', 'success to connect to DB 57', 'server-57', '2023-09-15 08:00:00', 'abc-du1g0brv-57', 'span-rae5n9kz', '436479c', 'server-1249') ,('error', 'error to connect to DB 58', 'server-58', '2023-09-15 08:00:00', 'abc-i99oy61e-58', 'span-29zayo7x', '4b7ac7d', 'server-5620') ,('success', 'success to connect to DB 59', 'server-59', '2023-09-15 08:00:00', 'abc-a1xagw29-59', 'span-evheqy4m', '4c97abb', 'server-2686') ,('error', 'error to connect to DB 60', 'server-60', '2023-09-15 08:00:00', 'abc-zd38355o-60', 'span-ylmy590y', '4b3c5b0', 'server-7406');")

        # self.curson.execute(
        # 'CREATE TABLE IF NOT EXISTS user(id MEDIUMINT NOT NULL AUTO_INCREMENT, username VARCHAR(25), access VARCHAR(25))')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(message);') # used for full-text search
        self.connection.commit()

    # Insert Log into Table
    def insert_log(self, request_data):
        level = request_data['level']
        message = request_data['message']
        resourceId = request_data['resourceId']
        timestamp = datetime.datetime.strptime(
            request_data['timestamp'], "%Y-%m-%dT%H:%M:%S%fZ")
        traceId = request_data['traceId']
        spanId = request_data['spanId']
        commit = request_data['commit']
        parentResourceId = request_data['metadata']['parentResourceId']
        self.cursor.execute('INSERT INTO log (level, message , resourceId,timestamp,traceId,spanId,commit,parentResourceId) VALUES ("{0}", "{1}", "{2}","{3}", "{4}", "{5}", "{6}" , "{7}");'.format(
            level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId))
        self.connection.commit()

    # View All Log from Table
    def fetch_all_logs(self):
        self.cursor.execute('SELECT * FROM log;')
        result = self.cursor.fetchall()
        return result

    # Search "level"
    def search_level(self, level):
        # SELECT * FROM log WHERE MATCH(level) AGAINST('{0}'); # used for full-text search
        self.cursor.execute(
            "SELECT * FROM log WHERE level LIKE '%{0}%';".format(level))
        result = self.cursor.fetchall()
        return result

    # Search "message"
    def search_message(self, message):
        self.cursor.execute(
            "SELECT * FROM log WHERE message LIKE '%{0}%';".format(message))
        result = self.cursor.fetchall()
        return result

    # Search "resourceId"
    def search_resourceId(self, resourceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE resourceId LIKE '%{0}%';".format(resourceId))
        result = self.cursor.fetchall()
        return result

    # Search between START dateTime & END datetime
    def search_timestamp(self, start, end):
        self.cursor.execute(
            "SELECT * FROM log WHERE timestamp >= '{0}' and timestamp < '{1}';".format(start, end))
        result = self.cursor.fetchall()
        return result

    # Search "traceId"
    def search_traceId(self, traceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE traceId LIKE '%{0}%'; ".format(traceId))
        result = self.cursor.fetchall()
        return result

    # Search "spanId"
    def search_spanId(self, spanId):
        self.cursor.execute(
            "SELECT * FROM log WHERE spanId LIKE '%{0}%'; ".format(spanId))
        result = self.cursor.fetchall()
        return result

    # Search "commit"
    def search_commit(self, commit):
        self.cursor.execute(
            "SELECT * FROM log WHERE commit LIKE '%{0}%'; ".format(commit))
        result = self.cursor.fetchall()
        return result

    # Search "parentResourceId"
    def search_parentResourceId(self, parentResourceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE parentResourceId LIKE '%{0}%'; ".format(parentResourceId))
        result = self.cursor.fetchall()
        return result


app = Flask(__name__)
CORS(app)
conn = None


@app.route('/')
def initDB():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.create_db()
    return "Started 🚀"

# Post logs to DB


@app.route('/log-ingestor', methods=['POST'])
def logIngestor():
    request_data = request.get_json()
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    conn.insert_log(request_data)
    response = {"status": 200, "message": "Inserted Successfully"}
    return jsonify(response)

# Fetch all logs from DB


@app.route('/fetch-all-logs', methods=['GET'])
def allLogs():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    log = conn.fetch_all_logs()
    response = {"status": 200, "logs": log}
    return jsonify(response)

# Search logs from DB


@app.route('/query-interface', methods=['GET'])
def queryInterface():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    if (request.args.getlist("filter")[0] == "timestamp"):
        logs = conn.search_timestamp(request.args.getlist(
            "start")[0], request.args.getlist("end")[0])
    else:
        if (request.args.getlist("search")[0] == ""):
            return {"status": 200, "message": "search field Empty"}
        if (request.args.getlist("filter")[0] == "level"):
            logs = conn.search_level(request.args.getlist("search")[0])
        if (request.args.getlist("filter")[0] == "message"):
            logs = conn.search_message(request.args.getlist("search")[0])
        if (request.args.getlist("filter")[0] == "resourceId"):
            logs = conn.search_resourceId(request.args.getlist("search")[0])

        if (request.args.getlist("filter")[0] == "traceId"):
            logs = conn.search_traceId(request.args.getlist("search")[0])
        if (request.args.getlist("filter")[0] == "spanId"):
            logs = conn.search_spanId(request.args.getlist("search")[0])
        if (request.args.getlist("filter")[0] == "commit"):
            logs = conn.search_commit(request.args.getlist("search")[0])
        if (request.args.getlist("filter")[0] == "parentResourceId"):
            logs = conn.search_parentResourceId(
                request.args.getlist("search")[0])
    response = {"status": 200, "logs": logs}
    return jsonify(response)


@app.route('/check-account', methods=['POST'])
@cross_origin()
def check_account():
    print(request.get_json.email)
    return jsonify({"userExists": True})


@app.route('/auth', methods=['POST'])
@cross_origin()
def auth():
    if (request.json['email'] == "f13@gmail.com" and request.json['password'] == "12345678"):
        return jsonify({"message": "success"})
    return jsonify({"status": "error"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5051)
