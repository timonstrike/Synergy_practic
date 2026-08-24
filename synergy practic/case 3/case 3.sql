CREATE DATABASE IF NOT EXISTS tourism_db;
USE tourism_db;

CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    visa_required BOOLEAN DEFAULT FALSE
);

CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(150) NOT NULL,
    service_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_name VARCHAR(150) NOT NULL,
    country_id INT NOT NULL,
    duration_days INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    client_id INT NOT NULL,
    tour_id INT NOT NULL,
    service_id INT,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

INSERT INTO countries (country_name, visa_required) VALUES ('Италия', true), ('Турция', false);
INSERT INTO services (service_name, service_price) VALUES ('Страховка Премиум', 1500.00), ('Экскурсия по Риму', 4500.00);
INSERT INTO clients (last_name, first_name, phone) VALUES ('Иванов', 'Иван', '+79991112233'), ('Петрова', 'Анна', '+79994445566');
INSERT INTO tours (tour_name, country_id, duration_days, base_price) VALUES ('Римские каникулы', 1, 7, 85000.00), ('Все включено Анталья', 2, 10, 60000.00);
INSERT INTO orders (order_date, client_id, tour_id, service_id, total_price) VALUES ('2026-08-23', 1, 1, 2, 89500.00);