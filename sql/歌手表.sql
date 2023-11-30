-- show databases;

-- use test11;
-- 
--  create table singer(
--  	id int,
--  	name varchar(10),
--  	gender varchar(2),
--  	song varchar(10)
--  );

-- insert into singer(id, name, gender, song) VALUES
-- (1, '周杰伦', '男', '雨下一整晚'),
-- (2, '林俊杰', '男', '浪漫血液'),
-- (3, '许嵩', '男', '有桃花'),
-- (4, 'TS', '女', 'lover'),
-- (5, '本兮', '女', '情歌悠扬'),
-- (6, '说说', '女', '不问天'),
-- (7, '小缘', '女', '时针'),
-- (8, '菠萝', '女', '如果'),
-- (9, '毛不易', '男', '不染'),
-- (10, '花たん', '女', '无心');

-- 给数据表增加字段
-- alter table singer add age int;

-- 更新某个字段的数据
-- update singer set age=id+30 where id%2!=0;

-- 操作只能一步一步来？

-- 查询所有数据
-- select * from singer where id > 5; 

-- select name, song, gender from singer where id > 5;
-- select name, song, gender from singer where gender = '女';


-- 分组聚合
-- select 聚合函数(值：如id) from singer (where gender = '女') group by xxx;
-- 聚合函数有：
-- sum 求和
-- avg 求平均值
-- min 求最小值
-- max 求最大值
-- count 求数量

-- group by 后面有哪个字段，前面才能显示哪个字段
-- 没有的字段只能用聚合函数显示
-- select gender, count(id) from singer group by gender;

-- 对结果排序 在查询语句最后加上 order by 字段名 [ asc(升序) | desc(降序) ]
-- select * from singer order by age desc; 

-- 对查询结果进行数量限制或者分页显示 最后加上 limit n[,m]
-- n表示跳过查询的前n条数据，m表示展示多少条数据
-- select * from singer order by age desc; 
-- select * from singer order by age desc limit 2, 3;

-- 语句各个语法有顺序
-- select age, count(*) from singer where age > 20 group by age order by age asc limit 2, 5;
-- select id , max(age), count(name)  from singer group by id order by id desc limit 2, 5;























