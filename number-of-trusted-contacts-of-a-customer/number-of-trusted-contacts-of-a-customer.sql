/* Write your T-SQL query statement below */

with invoice_contacts as (
    select i.invoice_id, c.customer_name, i.price, i.user_id, count(co.contact_name) as contacts_cnt
    from Invoices i join Customers c on i.user_id=c.customer_id 
    left join Contacts co on i.user_id=co.user_id 
    group by i.invoice_id, c.customer_name, i.price, i.user_id 
), valid_contacts as (
    select co.user_id, count(c.email) as trusted_contacts_cnt 
    from Contacts co left join Customers c 
    on co.contact_email=c.email 
    group by co.user_id
)
    select i.invoice_id, i.customer_name, i.price, i.contacts_cnt, isnull(v.trusted_contacts_cnt, 0) as trusted_contacts_cnt 
    from invoice_contacts i left join valid_contacts v 
    on i.user_id=v.user_id order by i.invoice_id