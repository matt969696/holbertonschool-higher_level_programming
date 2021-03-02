-- creates the database hbtn_0d_2
-- and the user user_0d_2
FLUSH PRIVILEGES;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER user_0d_2@localhost;
CREATE USER user_0d_2@localhost IDENTIFIED by 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;
