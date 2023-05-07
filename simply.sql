CREATE TABLE `Author_Book` (
    `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `author_id` INTEGER NOT NULL,
    `book_id` INTEGER NOT NULL,
    FOREIGN KEY(`author_id`) REFERENCES `Author`(`id`),
    FOREIGN KEY(`book_id`) REFERENCES `Book`(`id`)
);

CREATE TABLE `Author` (
    `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `image` TEXT NOT NULL,
    `favorite`  BOOLEAN NOT NULL  
);

CREATE TABLE `Book` (
    `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title` TEXT NOT NULL,
    `image` TEXT NOT NULL,
    `price` INTEGER NOT NULL,
    `sale`  BOOLEAN NOT NULL,
    `description` TEXT NOT NULL
);

INSERT INTO `Author_Book` VALUES (null, 1, 1)
INSERT INTO `Author_Book` VALUES (null, 2, 2)
INSERT INTO `Author_Book` VALUES (null, 3, 3)
INSERT INTO `Author_Book` VALUES (null, 4, 4)
INSERT INTO `Author_Book` VALUES (null, 5, 5)
INSERT INTO `Author_Book` VALUES (null, 6, 6)
INSERT INTO `Author_Book` VALUES (null, 7, 7)
INSERT INTO `Author_Book` VALUES (null, 8, 8)
INSERT INTO `Author_Book` VALUES (null, 9, 9)
INSERT INTO `Author_Book` VALUES (null, 10, 10)

INSERT INTO `Author` VALUES (null, 'Edwina', 'Curee', 'ecuree0@skype.com', 'http://dummyimage.com/217x100.png/cc0000/ffffff', 0);
INSERT INTO `Author` VALUES (null, 'Wes', 'Yeates', 'wyeates1@webnode.com', 'http://dummyimage.com/250x100.png/5fa2dd/ffffff', 0);
INSERT INTO `Author` VALUES (null, 'Kipper', 'Stockford', 'kstockford2@hubpages.com', 'http://dummyimage.com/128x100.png/ff4444/ffffff', 1);
INSERT INTO `Author` VALUES (null, 'Arleen', 'Avramow', 'aavramow3@google.cn', 'http://dummyimage.com/200x100.png/cc0000/ffffff', 0);
INSERT INTO `Author` VALUES (null, 'Rubetta', 'McQuorkel', 'rmcquorkel4@furl.net', 'http://dummyimage.com/186x100.png/cc0000/ffffff', 0);
INSERT INTO `Author` VALUES (null, 'Cristobal', 'Anstie', 'canstie5@flickr.com', 'http://dummyimage.com/103x100.png/ff4444/ffffff', 1);
INSERT INTO `Author` VALUES (null, 'Nikki', 'Duckett', 'nduckett6@wsj.com', 'http://dummyimage.com/154x100.png/cc0000/ffffff', 0);
INSERT INTO `Author` VALUES (null, 'Fredi', 'Daugherty', 'fdaugherty7@goo.gl', 'http://dummyimage.com/248x100.png/cc0000/ffffff', 1);
INSERT INTO `Author` VALUES (null, 'Englebert', 'Beneix', 'ebeneix8@cbc.ca', 'http://dummyimage.com/181x100.png/cc0000/ffffff', 0);
INSERT INTO `Author` VALUES (null, 'Catrina', 'Kleimt', 'ckleimt9@guardian.co.uk', 'http://dummyimage.com/161x100.png/5fa2dd/ffffff', 1);


insert into `Book` values (null, 'George Lopez: It''s Not Me, It''s You', 'http://dummyimage.com/133x100.png/ff4444/ffffff', 6.01, 0, 'Suspendisse potenti. Nullam porttitor lacus at turpis.');
insert into `Book` values (null, 'Takva: A Man''s Fear of God', 'http://dummyimage.com/137x100.png/dddddd/000000', 6.97, 1, 'Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.');
insert into `Book` values (null, 'Rebecca of Sunnybrook Farm', 'http://dummyimage.com/159x100.png/ff4444/ffffff', 3.23, 0, 'Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. ');
insert into `Book` values (null, 'Police Academy: Mission to Moscow', 'http://dummyimage.com/103x100.png/5fa2dd/ffffff', '$3.41', false, 'Aenean lectus.');
insert into `Book` values (null, 'Unspeakable Acts ', 'http://dummyimage.com/219x100.png/5fa2dd/ffffff', 2.12, 1, 'Aliquam quis turpis eget elit sodales scelerisque. ');
insert into `Book` values (null, 'Wu yen', 'http://dummyimage.com/242x100.png/5fa2dd/ffffff', 4.19, 1, 'Vivamus vestibulum sagittis sapien.');
insert into `Book` (null, 'Without a Clue', 'http://dummyimage.com/194x100.png/cc0000/ffffff', 6.41, 0, 'Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.');
insert into `Book` values (null, 'Europa Europa (Hitlerjunge Salomon)', 'http://dummyimage.com/206x100.png/dddddd/000000', 7.66, 0, 'Integer ac leo. Pellentesque ultrices mattis odio. ');
insert into `Book` values (null, 'To Be or Not to Be', 'http://dummyimage.com/244x100.png/5fa2dd/ffffff', 3.26, 1, 'Suspendisse potenti. Cras in purus eu magna vulputate luctus. ');
insert into `Book` values (null, 'Solino', 'http://dummyimage.com/246x100.png/cc0000/ffffff', 3.13, 1, 'Nunc purus. Phasellus in felis. Donec semper sapien a libero. Nam dui.');

SELECT
    a.id,
    a.email,
    a.first_name,
    a.last_name,
    a.image,
    a.favorite
FROM author a
WHERE a.id = 3

SELECT * FROM Author a ORDER BY id DESC

SELECT name FROM sqlite_master WHERE type='table' AND name='Author';
