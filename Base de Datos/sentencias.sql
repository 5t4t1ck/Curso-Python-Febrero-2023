create database prueba; #Crea la base de datos
drop database prueba; #Elimina la base de datos

use prueba; #Indicamos a MySQL que estamos utilizando la base de datos prueba

# Crear la tabla usuario, crear el campo id
# creamos el campo email de tipo varchar, crear el campo username

create table usuario(id int, email varchar(255), username varchar(50)); #Se puede utilizar un primary_key auto_increment en campo id
drop table usuario; #Elimina la tabla usuario.

#Crear el campo edad en la tabla usuario.
alter table usuario add edad int;

#Eliminar el campo edad de la tabla usuario.
alter table usuario drop column edad;

#Modificar la tabla
alter table usuario modify column email varchar(50);

#Insertar registros
insert into usuario(email, username)
values ('dsaavedra88@gmail.com','statick');

#Eliminar registros
delete from usuario where email = 'dsaavedra88@gmail.com' limit 1;

# Agregamos al campo id primary_key
alter table usuario add primary key (id);

# Agregar al campo id auto_increment
alter table usuario modify column id int auto_increment;

insert into usuario(email, username) 
values ('usuario@gmail.com','statick');

insert into usuario(email, username) 
values ('usuario1@gmail.com','statick_1');

insert into usuario(email, username) 
values ('usuario2@gmail.com','statick_2');

#Filtramos la busqueda de registro por el campo email
select * from usuario where email="usuario1@gmail.com";

alter table usuario add edad int;

#Filtro según condiciones
select * from usuario where edad <= 34;

# Update
update usuario set edad = 32 where id = '3';

# Delete
delete from usuario where id = '3';

