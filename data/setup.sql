CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL,
  date_of_birth DATE NOT NULL
);
INSERT INTO users (
    id,
    username,
    name,
    last_name,
    email,
    date_of_birth
  )
VALUES (
    1,
    'fmesa',
    'Francisco',
    'Mesa',
    'fmesa@mail.com',
    '2003-01-15'
  ),
  (
    2,
    'dtorres',
    'David',
    'Torres',
    'dtorres@mail.com',
    '2000-05-21'
  ),
  (
    3,
    'jlopez',
    'Juan',
    'López',
    'jlopez@mail.com',
    '1999-12-31'
  ),
  (
    4,
    'adiaz',
    'Ana',
    'Díaz',
    'adiaz@mail.com',
    '1995-06-30'
  ),
  (
    5,
    'jgarcia',
    'Julia',
    'García',
    'jgarcia@mail.com',
    '2002-11-10'
  ),
  (
    6,
    'jgutierrez',
    'Juan',
    'Gutiérrez',
    'jgutierrez',
    '2001-01-01'
  ),
  (
    7,
    'mmartinez',
    'Maria',
    'Martínez',
    'mmartinez@mail.com',
    '1998-02-28'
  ),
  (
    8,
    'mrodriguez',
    'Manuel',
    'Rodríguez',
    'mrodriguez@mail.com',
    '1997-03-15'
  ),
  (
    9,
    'cfernandez',
    'Carlos',
    'Fernández',
    'cfernandez@mail.com',
    '1996-04-30'
  ),
  (
    10,
    'mgonzalez',
    'Marta',
    'González',
    'mgonzalez@mail.com',
    '2004-07-20'
  );
CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  content TEXT NOT NULL
);
INSERT INTO posts (id, title, content)
VALUES (
    1,
    'Introduction to Programming',
    'In this post, we will explore the basics of programming and learn how to write our first program.'
  ),
  (
    2,
    'Data Structures and Algorithms',
    'In this post, we will dive into various data structures and algorithms and understand their importance in software development.'
  ),
  (
    3,
    'Web Development with HTML and CSS',
    'In this post, we will learn how to create a simple website using HTML and CSS, and explore the fundamentals of web development.'
  ),
  (
    4,
    'Introduction to JavaScript',
    'In this post, we will introduce JavaScript, a powerful programming language used for building interactive web applications.'
  ),
  (
    5,
    'Working with APIs',
    'In this post, we will explore how to interact with APIs and retrieve data from external sources to enhance our applications.'
  );