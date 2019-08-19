CREATE TABLE templates (
    id SERIAL PRIMARY KEY,
    language TEXT UNIQUE NOT NULL,
    template TEXT NOT NULL
);

INSERT INTO templates (language, template)
VALUES
    ('en', 'Hello, {}!'),
    ('ja', 'こんにちは、{}！');
