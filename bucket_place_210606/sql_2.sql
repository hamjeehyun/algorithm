
select members.name as member_name, COUNT(orders.id), orders.id, order_options.id, order_options_price.price
from orders, order_options, members,
		(select order_options.id as order_option_id, price 
		 from payments, order_options 
		 where payments.order_option_id = order_options.id) order_options_price
where orders.id = order_options.order_id
and members.id = orders.member_id
and order_options_price.order_option_id = order_options.id
group by orders.id

;

