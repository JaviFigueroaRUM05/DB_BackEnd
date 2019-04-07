-- Fill in test data for schema

--Users
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    'TheParodict','admin','Brian' , 'Rodriguez', 'brianrodrig@gmail.com', '7879067012');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    'Hydrogon','admin','Sofia' , 'Saavedra', 'sofia.saavedra@gmail.com', '7876666969');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
   'Javi','admin','Javier' , 'Figueroa', 'javier.figueroa29@upr.edu', '7879637512');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    'ManuelDB','sinsabores','Manuel' , 'Rodriguez', 'manuel.rodriguez@gmail.com', '9395874632');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
   'SmoothCriminal','heehee', 'Michael' , 'Jackson', 'ayuwoki@gmail.com', '8459638521');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
   'MB','feelingood', 'Michael' , 'Buble', 'mbuble@yahoo.com', '7974521683');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
   'EVH','eruption', 'Eddie' , 'VanHalen', 'hotforteacher@gmail.com', '4512222222');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
   'Hollywoodperv','#metoo', 'Harvey' , 'Weinstein', 'metoo@gmail.com', '9116969696');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    'Vulcan','livelong&prosper', 'Leonard' , 'Neemoy', 'spock@gmail.com', '0101010101');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
   'tom','screwfacebook', 'Tom' , 'Frommyspace', 'tom@myspace.com', '9394561248');

--Contacts (only TheParodict, Hydrogon, and Javi have contacts)
insert into contacts(uid, cid) VALUES((select uid from users where uname='TheParodict'),
    (select uid from users where uname='Hydrogon'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='TheParodict'),
    (select uid from users where uname='MB'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='TheParodict'),
    (select uid from users where uname='Javi'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='TheParodict'),
    (select uid from users where uname='EVH'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Hydrogon'),
    (select uid from users where uname='TheParodict'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Hydrogon'),
    (select uid from users where uname='Vulcan'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Hydrogon'),
    (select uid from users where uname='SmoothCriminal'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Javi'),
    (select uid from users where uname='Hydrogon'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Javi'),
    (select uid from users where uname='Hollywoodperv'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Javi'),
    (select uid from users where uname='tom'));
insert into contacts(uid, cid) VALUES((select uid from users where uname='Javi'),
    (select uid from users where uname='ManuelDB'));

--Groups
insert into cgroup(gname)VALUES('The first chat');
insert into cgroup(gname)VALUES('Admins');
insert into cgroup(gname)VALUES('trambolico');


--Group Participants (how do we make sure admins are participants?)
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='The first chat'), 't');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='The first chat'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='Admins'), 't');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='Admins'), 't');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Javi'),
    (select gid from cgroup where gname='Admins'), 't');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='trambolico'), 't');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Javi'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='ManuelDB'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='tom'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='EVH'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='MB'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Vulcan'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='SmoothCriminal'),
    (select gid from cgroup where gname='trambolico'), 'f');
insert into participants(uid, gid, isAdmin) VALUES((select uid from users where uname='Hollywoodperv'),
    (select gid from cgroup where gname='trambolico'), 'f');

--Posts
insert into post(pdate, message, mediaType, uid, gid) VALUES('2019-03-17 18:40:00','Hello world', 'n',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:41:00','Cactus','n',
    (select uid from users where uname='Hydrogon'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:42:00','When does the Narwhal Bacon?','n',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message,mediaType, uid, gid) VALUES('2019-03-17 18:43:00','Midnight!','n',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:40:00','Hello my Admins!','n',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:41:00','DB is my favorite Class!','n',
    (select uid from users where uname='Javi'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:42:00','Im drowning in my classes #pleasehelp','n', --#
    (select uid from users where uname='Hydrogon'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:43:00','LOL!','n',
    (select uid from users where uname='Javi'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:40:00','Hello!','n',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:41:00','Back from the dead to touch more kids!','n',
    (select uid from users where uname='SmoothCriminal'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:42:00','Dude, wtf!','n',
    (select uid from users where uname='Hollywoodperv'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:43:00','All this talk of sensuality seems illogical.','n',
    (select uid from users where uname='Vulcan'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, mediaType,uid, gid) VALUES('2019-03-17 18:44:00','Notice me, senpai!','n',
    (select uid from users where uname='Hydrogon'), (select gid from cgroup where gname='trambolico'));

--Replies
insert into replies(replyID, opID) VALUES((select postid from post where message='Midnight!'),
(select postid from post where  message='When does the Narwhal Bacon?'));
insert into replies(replyID, opID) VALUES((select postid from post where message='LOL!'),
(select postid from post where message='Im drowning in my classes #pleasehelp'));
insert into replies(replyID, opID) VALUES((select postid from post where message='Dude, wtf!'),
(select postid from post where message='Back from the dead to touch more kids!'));
insert into replies(replyID, opID) VALUES((select postid from post where message='Notice me, senpai!'),
(select postid from post where message='All this talk of sensuality seems illogical.'));

--Hashtags
insert into hashtag(hname) VALUES('#pleasehelp');

--Tagged
insert into tagged(postid, hid) VALUES((select postid from post where message='Im drowning in my classes #pleasehelp'),
(select hid from hashtag where hname='#pleasehelp'));

--Reactions
insert into reaction (rdate, rtype, postID, uid) VALUES('2019-03-17 18:43:00', 'L',
    (select postid from post where message='Im drowning in my classes #pleasehelp'),
    (select uid from users where uname='Javi'));
