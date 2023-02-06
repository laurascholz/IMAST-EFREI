CREATE TABLE productsearch
(
    product_id INT NOT NULL,
    searchstring_id INT NOT NULL,
    CONSTRAINT FK_productsearch_product FOREIGN KEY (product_id) REFERENCES product(id),
    CONSTRAINT FK_productsearch_searchstring FOREIGN KEY (searchstring_id) REFERENCES searchstring(id)
);
