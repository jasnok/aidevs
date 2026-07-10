INSERT INTO sample_vectors (title, content, embedding)
VALUES
    ('FastAPI', 'Python API backend framework', '[0.9,0.1,0.2]'),
    ('Backend', 'Server API database logic', '[0.8,0.2,0.3]'),
    ('Streamlit', 'Python frontend dashboard', '[0.1,0.9,0.2]');

SELECT
    title,
    content,
    embedding <=> '[0.85,0.15,0.25]'::vector AS cosine_distance
FROM sample_vectors
ORDER BY embedding <=> '[0.85,0.15,0.25]'::vector
LIMIT 3;
