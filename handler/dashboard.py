from flask import jsonify
from psycopg2 import IntegrityError
from dao.dashboard import DashboardDao

class DashboardHandler:

    @staticmethod
    def get_trending_hashtag():
        dao = DashboardDao()
        try:
            query_result = dao.get_trending_hashtags()
            result = []
            for row in query_result:
                dic = {}
                dic['name']  = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_posts():
        dao = DashboardDao()
        try:
            query_result = dao.get_all_posts()
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['message'] = row[1]
                dic['mediaType'] = row[2]
                dic['media'] = row[3]
                dic['gName'] = row[4]
                dic['uName'] = row[5]
                dic['pid'] = row[6]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_replies_to_post(pid):
        dao = DashboardDao()
        try:
            query_result = dao.get_replies_to_post(pid)
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['message'] = row[1]
                dic['mediaType'] = row[2]
                dic['media'] = row[3]
                dic['gName'] = row[4]
                dic['uName'] = row[5]
                dic['pid'] = row[6]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_reactions_to_post(pid):
        dao = DashboardDao()
        try:
            query_result = dao.get_reactions_to_post(pid)
            result = []
            for row in query_result:
                dic = {}
                dic['rType'] = row[0]
                dic['uName'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_posts_by_user(uid):
        dao = DashboardDao()
        try:
            query_result = dao.get_all_posts_by_user(uid)
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['message'] = row[1]
                dic['mediaType'] = row[2]
                dic['media'] = row[3]
                dic['gName'] = row[4]
                dic['uName'] = row[5]
                dic['pid'] = row[6]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_posts_by_date(date):
        dao = DashboardDao()
        try:
            query_result = dao.get_all_posts_by_date(date)
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['message'] = row[1]
                dic['mediaType'] = row[2]
                dic['media'] = row[3]
                dic['gName'] = row[4]
                dic['uName'] = row[5]
                dic['pid'] = row[6]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_posts_by_user_date(uid, date):
        dao = DashboardDao()
        try:
            query_result = dao.get_all_posts_by_user_date(uid, date)
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['message'] = row[1]
                dic['mediaType'] = row[2]
                dic['media'] = row[3]
                dic['gName'] = row[4]
                dic['uName'] = row[5]
                dic['pid'] = row[6]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_replies_by_date(date):
        dao = DashboardDao()
        try:
            query_result = dao.get_all_replies_by_date(date)
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['message'] = row[1]
                dic['mediaType'] = row[2]
                dic['media'] = row[3]
                dic['gName'] = row[4]
                dic['uName'] = row[5]
                dic['pid'] = row[6]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_likes_by_date(date):
        dao = DashboardDao()
        try:
            query_result = dao.get_likes_by_date(date)
            result = []
            for row in query_result:
                dic = {}
                dic['count'] = row[0]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_dislikes_by_date(date):
        dao = DashboardDao()
        try:
            query_result = dao.get_dislikes_by_date(date)
            result = []
            for row in query_result:
                dic = {}
                dic['count'] = row[0]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_active_users_by_date(date):
        dao = DashboardDao()
        try:
            query_result = dao.get_active_users_by_date(date)
            result = []
            for row in query_result:
                dic = {}
                dic['uName'] = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))
