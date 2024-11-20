INSERT INTO customers (name, contact_info) VALUES 
    ('Alice Smith', 'alice@example.com'),
    ('Bob Johnson', 'bob.johnson@example.com'),
    ('Charlie Brown', 'charlie.brown@example.com'),
    ('Diana Prince', 'diana.prince@example.com'),
    ('Edward Kim', 'edward.kim@example.com');


INSERT INTO teams (team_name, members) VALUES 
    ('Development Team', '[{"name": "John Doe", "role": "Developer"}, {"name": "Jane Roe", "role": "Lead Developer"}]'),
    ('Marketing Team', '[{"name": "Emily White", "role": "Marketing Specialist"}, {"name": "Tom Black", "role": "SEO Expert"}]'),
    ('Support Team', '[{"name": "Anna Green", "role": "Customer Support"}, {"name": "Paul Blue", "role": "Support Manager"}]');
INSERT INTO projects (customer_id, name, description, status, assigned_team) VALUES 
    (1, 'Project Alpha', 'An e-commerce website for Alice', 'ongoing', 1),
    (2, 'Project Beta', 'Marketing campaign for Bob', 'completed', 2),
    (3, 'Project Gamma', 'Customer support system for Charlie', 'in progress', 3),
    (4, 'Project Delta', 'New mobile app for Diana', 'planned', 1);
