from flask import jsonify
from dao.posts import PostsDAO

class PostsHandler:

    posts_cont = ["postid","pdate","message","mediatype", "media","uid","gid"]

    def build_post_dict(self, row):
        result = {}
        result['postid'] = row[0]
        result['pdate'] = row[1]
        result['message'] = row[2]
        result['mediatype'] = row[3]
        result['media'] = row[4]
        result['uid'] = row[5]
        result['gid'] = row[6]
        return result

    def build_users_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['first_name'] = row[2]
        result['last_name'] = row[3]
        result['email'] = row[4]
        result['phone'] = row[5]
        result['rid'] = row[6]
        result['rdate'] = row[7]
        result['rtype'] = row[8]
        return result


    def getAllPosts(self):
        dao = PostsDAO()
        posts_list = dao.getAllPosts()
        result_list = []
        for row in posts_list:
            result = self.build_post_dict(row)
            result_list.append(result)
        return jsonify(Posts=result_list)

        # get posts in a group
    def getPostsByGroup(self, gid):
        dao = PostsDAO()
        post_list = dao.getPostsByGroup(gid)
        result_list = []
        for row in post_list:
            result = self.build_post_dict(row)
            result['uname'] = row[7]
            result['original_post'] = row[8]
            result['likes'] = row[9]
            result['dislikes'] = row[10]
            result_list.append(result)
        return jsonify(Posts=result_list)


    def getPostsById(self, gid, pid):
        dao = PostsDAO()
        row = dao.getPostById(gid, pid)
        if not row:
            return jsonify(Error = "Post Not Found or not in this group"), 404
        else:
            post_info = self.build_post_dict(row)
            post_info['uname'] = row[7]
            users = dao.getUsers_and_Reactions(pid)
            users_list = []
            for user in users:
                result = self.build_users_dict(user)
                users_list.append(result)
            response = {"Post": post_info, "Reactions_Users" : users_list}
            return jsonify(response)


    def createNewPost(self, p_info):
        # dao = PostsDAO()
        # p_date= p_info['post_date']
        # media= p_info['media']
        # message= p_info['message']
        # gid = p_info['gid']
        # reply = p_info['reply_to_post']
        #
        # gid = dao.createNewGroup(p_date=p_date, media=media, message=message, gid=gid, reply=reply)
         p_info['pid']=5
         self.posts.append(p_info)
         return jsonify(p_info)


    #get posts made my a certain user
#TODO: check that its working
    def getPostsByUser(self, uid):
        # dao = PostsDAO()
        # post_list = dao.getPostsByUser(uid)
        # result_list = []
        # for row in post_list:
        #     post = dao.getPostById(row[0])
        #     result = self.build_post_dict(post)
        #     result_list.append(result)
        # return jsonify(Posts=result_list)
        posts = [{
            'pid' : 10,
            'p_date': '2019-01-25',
            'media' : 'default',
            'message' : 'Im tired'
        },
        {
            'pid' : 8,
            'p_date': '2019-01-25',
            'media' : 'default',
            'message' : 'Me too'
        }]
        return jsonify(posts)
