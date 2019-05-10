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
                dic['uid'] = row[5]
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
                dic['pid'] = row[4]
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
            result = { 'Like' : [], 'Dislike' : []}
            for row in query_result:
                person = {}
                person['uName'] = row[1]
                person['date']  = row[2]
                person['uid']   = row[3]
                if row[0] == 'L' : result['Like'].append(person)
                else             : result['Dislike'].append(person)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_reactions_count_to_post(pid):
        dao = DashboardDao()
        try:
            query_result = dao.get_reactions_count_to_post(pid)
            result = {}
            for row in query_result:
                dic = {}
                dic['pid']  = row[1]
                dic['count']   = row[2]
                if row[0] == 'L' : result['Like'] = dic
                else             : result['Dislike'] = dic
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
            result_dic = {}
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
            result_dic['count'] = len(result)
            result_dic['posts'] = result
            return jsonify(result_dic)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_posts_count_by_date():
        dao = DashboardDao()
        try:
            query_result = dao.get_all_posts_count_by_date()
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_posts_by_user_date(uid):
        dao = DashboardDao()
        try:
            query_result = dao.get_all_posts_by_user_date(uid)
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_all_replies_by_date():
        dao = DashboardDao()
        try:
            query_result = dao.get_all_replies_by_date()
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_likes_by_date():
        dao = DashboardDao()
        try:
            query_result = dao.get_likes_by_date()
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_dislikes_by_date():
        dao = DashboardDao()
        try:
            query_result = dao.get_dislikes_by_date()
            result = []
            for row in query_result:
                dic = {}
                dic['date'] = row[0]
                dic['count'] = row[1]
                result.append(dic)
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_active_users_by_date():
        dao = DashboardDao()
        try:
            query_result = dao.get_active_users_by_date()
            result = {}
            for row in query_result:
                result[str(row[0])] = []
            for row in query_result:
                result[str(row[0])].append({ 'uname' : row[1], 'count' : row[2] })
            return jsonify(result)
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))
