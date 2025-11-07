CREATE TABLE IF NOT EXISTS messages (
  id SERIAL PRIMARY KEY,
  text TEXT NOT NULL
);

INSERT INTO messages (text) VALUES ('Hola món des de PostgreSQL!')
ON CONFLICT DO NOTHING;
