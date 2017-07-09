--create db 
drop database if exists electronics;
create database electronics;
use electronics;

--order_headers
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

--order_lines
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

--shipping_types
drop table if exists shipping_types;

create table shipping_types (
  shipping_type_id int not null,
  description varchar(100),
  cost decimal(5,2),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (shipping_type_id)  
);

--customers
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


--states_provs
drop table if exists states_provs;

create table states_provs (
  state_prov_id int not null,
  name varchar(500),
  country_id int references country(country_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (state_prov_id)  
);

--countries
drop table if exists countries;

create table countries (
  country_id int not null,
  name varchar(500) not null,
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (country_id)  
);

-- products
drop table if exists products;

create table products (
  product_id int not null auto_increment,
  product_number varchar(100) not null,
  name varchar(500),
  description varchar(2000),
  uom varchar(20) not null,
  manufacturer_id int,
  family_id int references product_family(family_id),
  subfamily_id int references product_subfamily(subfamily_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (product_id)
);

--product_subfamily
drop table if exists product_subfamily;

create table product_subfamily (
  subfamily_id int not null auto_increment,
  name varchar(500),
  family_id int references product_family(family_id),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (subfamily_id)
);
  
--product_family table
drop table if exists product_family;

create table product_family (
  family_id int not null auto_increment,
  name varchar(500),
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (family_id)  
);  

--product costs (will need to make a view so current prices are available)
drop table if exists product_costs;

create table product_costs (
  cost_id int not null auto_increment,
  product_id int references product(product_id),
  mtl_cost decimal(6, 2),
  labor_cost decimal(6,2),
  burden_cost decimal(6,2),
  created_date timestamp default current_timestamp,
  primary key (cost_id)
);


--create view to get current_product_cost
create or replace view current_product_costs as 
  select pc.product_id, pc.mtl_cost, pc.labor_cost, pc.burden_cost, pc.cost_id, pc.created_date
  from product_costs pc
  inner join (
    select max(cost_id) as cost_id, product_id
    from product_costs
    group by 2
    ) most_recent
  on pc.cost_id = most_recent.cost_id
;

drop table if exists products_prices;

create table products_prices (
    price_list_id int references price_lists(price_list_id),
    product_id int references products(product_id),
    list_price decimal(6,2),
    created_date timestamp default current_timestamp
);

drop table if exists price_lists;

create table price_lists (
  price_list_id int not null auto_increment,
  active boolean,
  list_start_date date,
  list_end_date date,
  created_date timestamp default current_timestamp,
  last_updated_date timestamp default current_timestamp,
  primary key (price_list_id)
);

--create view for current prices 
create or replace view current_product_prices as
select pp.product_id, pp.list_price, pl.price_list_id
from products_prices pp
inner join price_lists pl
on pp.price_list_id = pl.price_list_id
where pl.price_list_id = true
;


  
