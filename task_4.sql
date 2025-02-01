USE alx_book_store;



USE alx_book_store;


SHOW TABLES;

-- Show the description of the 'Books' table by querying INFORMATION_SCHEMA.COLUMNS
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'Books';

