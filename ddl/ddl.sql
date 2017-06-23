--create db 
drop database if exists electronics;
create database electronics;

--create order_headers tables
drop table if exists order_headers;

create table order_headers (
  header_id int not null,
  order_number varchar(20) not null,
  sold_to_id varchar(5) references customers(customer_id),
  ship_to_id varchar(5) references customers(customer_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  po_id varchar(10),
  currency varchar(5),
  primary key (header_id)

);

--create order_lines
drop table if exists order_lines;

create table order_lines (
  line_id int not null,
  header_id varchar(20) references order_headers(header_id),
  line_number int not null,
  schedule_ship_date date,
  quantity int,
  product_id int references products(product_id),
  price_list_id int references price_lists(price_list_id),
  discount decimal(2,2),
  net_price decimal(6,2),
  shipping_type_id int references shipping_types(shipping_type_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (line_id)
);

--create shipping_types
drop table if exists shipping_types;

create table shipping_types (
  shipping_type_id int not null,
  description varchar(100),
  cost decimal(5,2),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (shipping_type_id)  
);

