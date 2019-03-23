-- Fill in test data for schema
--Persons
--insert into person(first_name, last_name, email, phone) VALUES( 'Brian' , 'Rodriguez', 'brianrodrig@gmail.com', '7879067012');
--insert into person(first_name, last_name, email, phone) VALUES( 'Sofia' , 'Saavedra', 'sofia.saavedra@gmail.com', '7876666969');
--insert into person(first_name, last_name, email, phone) VALUES( 'Javier' , 'Figueroa', 'javier.figueroa29@upr.edu', '7879637512');
--insert into person(first_name, last_name, email, phone) VALUES( 'Manuel' , 'Rodriguez', 'manuel.rodriguez@gmail.com', '9395874632');
insert into person(first_name, last_name, email, phone) VALUES( 'Michael' , 'Jackson', 'ayuwoki@gmail.com', '8459638521');
insert into person(first_name, last_name, email, phone) VALUES( 'Michael' , 'Buble', 'mbuble@yahoo.com', '7974521683');
insert into person(first_name, last_name, email, phone) VALUES( 'Eddie' , 'VanHalen', 'hotforteacher@gmail.com', '4512222222');
insert into person(first_name, last_name, email, phone) VALUES( 'Harvey' , 'Weinstein', 'metoo@gmail.com', '9116969696');
insert into person(first_name, last_name, email, phone) VALUES( 'Leonard' , 'Neemoy', 'spock@gmail.com', '0101010101');
insert into person(first_name, last_name, email, phone) VALUES( 'Tom' , 'Frommyspace', 'tom@myspace.com', '9394561248');

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
    (select pid from person where email='ayuwoki@gmail.com'),'SmoothCriminal','heehee');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    (select pid from person where email='mbuble@yahoo.com'),'MB','feelingood');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    (select pid from person where email='hotforteacher@gmail.com'),'EVH','eruption');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    (select pid from person where email='metoo@gmail.com'),'Hollywoodperv','#metoo');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    (select pid from person where email='spock@gmail.com'),'Vulcan','livelong&prosper');
insert into users(uname, password, first_name, last_name, email, phone) VALUES(
    (select pid from person where email='tom@myspace.com'),'tom','screwfacebook');

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

--Group admins
insert into admins(uid, gid) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='The first chat'));
insert into admins(uid, gid) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='Admins'));
insert into admins(uid, gid) VALUES((select uid from users where uname='Javi'),
    (select gid from cgroup where gname='Admins'));
insert into admins(uid, gid) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='Admins'));
insert into admins(uid, gid) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='trambolico'));
insert into admins(uid, gid) VALUES((select uid from users where uname='Javi'),
    (select gid from cgroup where gname='trambolico'));
insert into admins(uid, gid) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='trambolico'));
insert into admins(uid, gid) VALUES((select uid from users where uname='ManuelDB'),
    (select gid from cgroup where gname='trambolico'));
insert into admins(uid, gid) VALUES((select uid from users where uname='tom'),
    (select gid from cgroup where gname='trambolico'));
insert into admins(uid, gid) VALUES((select uid from users where uname='EVH'),
    (select gid from cgroup where gname='trambolico'));

--Group Participants (how do we make sure admins are participants?)
insert into participants(uid, gid) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='The first chat'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='The first chat'));
insert into participants(uid, gid) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='Admins'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='Admins'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Javi'),
    (select gid from cgroup where gname='Admins'));
insert into participants(uid, gid) VALUES((select uid from users where uname='TheParodict'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Hydrogon'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Javi'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='ManuelDB'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='tom'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='EVH'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='MB'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Vulcan'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='SmoothCriminal'),
    (select gid from cgroup where gname='trambolico'));
insert into participants(uid, gid) VALUES((select uid from users where uname='Hollywoodperv'),
    (select gid from cgroup where gname='trambolico'));

--Posts
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:40:00','Hello world',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:41:00','Cactus',
    (select uid from users where uname='Hydrogon'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:42:00','When does the Narwhal Bacon?',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:43:00','Midnight!',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='The first chat'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:40:00','Hello my Admins!',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:41:00','DB is my favorite Class!',
    (select uid from users where uname='Javi'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:42:00','Im drowning in my classes #pleasehelp', --#
    (select uid from users where uname='Hydrogon'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:43:00','LOL!',
    (select uid from users where uname='Javi'), (select gid from cgroup where gname='Admins'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:40:00','Hello!',
    (select uid from users where uname='TheParodict'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:41:00','Back from the dead to touch more kids!',
    (select uid from users where uname='SmoothCriminal'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:42:00','Dude, wtf!',
    (select uid from users where uname='Hollywoodperv'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:43:00','All this talk of sensuality seems illogical.',
    (select uid from users where uname='Vulcan'), (select gid from cgroup where gname='trambolico'));
insert into post(pdate, message, uid, gid) VALUES('2019-03-17 18:44:00','Notice me, senpai!',
    (select uid from users where uname='Hydrogon'), (select gid from cgroup where gname='trambolico'));

--Replies
insert into replies(postid, replyid) VALUES((select postid from post where message='Midnight!'),
(select postid from post where  message='When does the Narwhal Bacon?'));
insert into replies(postid, replyid) VALUES((select postid from post where message='LOL!'),
(select postid from post where message='Im drowning in my classes #pleasehelp'));
insert into replies(postid, replyid) VALUES((select postid from post where message='Dude, wtf!'),
(select postid from post where message='Back from the dead to touch more kids!'));
insert into replies(postid, replyid) VALUES((select postid from post where message='Notice me, senpai!'),
(select postid from post where message='All this talk of sensuality seems illogical.'));

--Hashtags
insert into hashtag(hname) VALUES('#pleasehelp');

--Tagged
insert into tagged(postid, hid) VALUES((select postid from post where message='Im drowning in my classes #pleasehelp'),
(select hid from hashtag where hname='#pleasehelp'));

--Reactions
insert into reaction (rdate, rtype, postid) VALUES('2019-03-17 18:43:00', 'L',
    (select postid from post where message='Im drowning in my classes #pleasehelp'));

--Reacts
insert into reacts(uid, rid) VALUES((select uid from users where uname='Javi'),
    (select rid from reaction where rdate='2019-03-17 18:43:00'));

