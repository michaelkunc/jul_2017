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

--create customer table
drop table if exists customers;

create table customers (
  customer_id int not null,
  name varchar(500),
  address_1 varchar(100),
  address_2 varchar(100),
  city varchar(100),
  state_prov_id int references state_prov(state_prov_id),
  country_id int references state_prov(country_id),
  postal_code varchar(20), 
  ship_to boolean,
  sold_to boolean,
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (customer_id)
);


-- create state_prov
drop table if exists states_provs;

create table states_provs (
  state_prov_id int not null,
  name varchar(500),
  country_id int references country(country_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (state_prov_id)  
);

-- create country table
drop table if exists countries;

create table countries (
  country_id int not null,
  name varchar(500) not null,
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (country_id)  
);

-- create products table
drop table if exists products;

create table products (
  product_id int not null,
  product_number varchar(100) not null,
  name varchar(500),
  description varchar(2000),
  uom varchar(20) not null,
  manufacturer_id int,
  family_id int references family(family_id),
  subfamily_id int references subfamily(subfamily_id),
    created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (product_id)
);



--create table subfamily
drop table if exists subfamily;

create table subfamily (
  subfamily_id int not null,
  name varchar(500),
  family_id int references family(family_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (subfamily_id)
);
  
  

  
