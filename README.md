# How to run the application?

Run the following commands on the terminal

```
python -m venv venv
(Mac/Linux) source venv/bin/activate
(Windows) venv/scripts/activate
pip install -r requirements.txt
flask db upgrade
flask run
```

# Project Overview – Flask Todo App

This project guides learners through the complete development of a fully functional Flask Todo application while progressively introducing professional software engineering and Software Quality Assurance (SQA) practices. Beginning with the simplest routing examples, the project evolves through templating, form handling, secure authentication, and SQLAlchemy-based database integration. It then advances into scalable application architecture using the factory pattern, automated testing with pytest, Behaviour-Driven Development (BDD), Test-Driven Development (TDD), and continuous integration with GitHub Actions.

The application is intentionally designed as an **educational learning tool**. Its goal is to expose students to **industry-standard concepts, patterns, and workflows**—including secure coding, modular architecture, automated testing, code quality enforcement, and DevOps-style CI pipelines. While it provides a realistic development experience, it is **not intended to be a perfect or production-grade system**. Instead, it serves as a practical scaffold where learners can observe, practise, and extend key ideas from real-world software engineering in a structured learning environment.

Across steps **step01–step34**, students learn how to build a maintainable, secure, testable, and industry-aligned web application. They gain hands-on experience with Flask, Jinja2, WTForms, SQLAlchemy, authentication, environment variables, linters, formatters, CI pipelines, and modern testing strategies. By the end, learners not only understand how the application works but also how high-quality software is designed, validated, protected, refactored, documented, and delivered in contemporary development teams.

Note: The step numbers provided in brackets serve as a general guide and may not match every implementation precisely. See the steps folder which contain code snapshots per step. Note the step folder is not part of the flask application but is a collection of all the tags/steps used for analysing how the project was developed step by step

# Flask Todo App – Full Project Summary (step01–step34)

## 1. Flask Fundamentals: Routing, Templates, and Project Structure (step01–step06)

### Key Concepts

- Creating a minimal Flask application and registering routes.
- Splitting routes into a `routes.py` module and understanding circular imports.
- Introducing the standard Flask folder structure (`templates/`, `static/css/`).
- Rendering templates using `render_template`.
- Implementing `base.html` and enabling template inheritance.
- Using `url_for` for static files and template links.

### Learning Outcomes

- Understand how Flask handles routing and modular design.
- Apply template inheritance to improve reusability.
- Use `url_for` to generate robust dynamic paths.
- Organise a Flask project using industry-accepted conventions.

## 2. In-Memory CRUD & Jinja2 Templates (step07–step13)

### Key Concepts

- Using Python lists and dictionaries to represent in-memory data.
- Passing data from Python to templates using Jinja2 context variables.
- Using Jinja2 loops, conditionals, and dynamic rendering.
- Creating task list, detail, edit, create, and delete pages.
- Implementing routes with dynamic parameters (e.g., `/task/<id>`).
- Fixing indexing bugs in templates.

### Learning Outcomes

- Build CRUD features using in-memory data structures.
- Use Jinja2 to dynamically render HTML content.
- Pass parameters into routes and templates.
- Understand backend → template data flow.

## 3. Forms, CSRF, Validation, and Authentication (step14–step16)

### Key Concepts

- Using Flask-WTF for secure form handling.
- Enabling CSRF protection with `SECRET_KEY` and `.env`.
- Loading environment variables using `python-dotenv`.
- Creating WTForms classes in `forms.py`.
- Implementing login logic and flash messages.
- Adding server-side validation rules.

### Learning Outcomes

- Build secure Flask forms using Flask-WTF.
- Understand CSRF protection and environment variable usage.
- Process POST requests safely.
- Provide user feedback via flash messages.
- Implement authentication flows securely.

## 4. SQLAlchemy & Database-Backed CRUD (step17–step20)

### Key Concepts

- Installing and configuring SQLAlchemy (SQLite).
- Defining ORM models for `User` and `Todo`.
- Running `db.create_all()` and interacting via Flask shell.
- Implementing authentication with hashed passwords.
- Adding user registration and linking todos to owners.
- Migrating CRUD operations from dictionary → database.

### Learning Outcomes

- Model relational data using ORM classes.
- Configure and operate a database through Flask.
- Securely store user credentials.
- Build persistent CRUD operations based on SQLAlchemy.

## 5. Application Architecture: Factory Pattern & Modularisation (step21)

### Key Concepts

- Introducing the Flask application factory pattern.
- Initialising extensions (db, login manager) within the factory.
- Registering blueprints for modular structure.
- Avoiding circular imports and improving scalability.

### Learning Outcomes

- Build scalable Flask apps using the factory pattern.
- Separate concerns using modules and blueprints.
- Support easier testing and cleaner architecture.

## 6. Testing, Fixtures, Coverage, BDD, TDD (step22–step30)

### Key Concepts

- Creating basic pytest structure with fixtures.
- Writing tests for routes, authentication, and models.
- Achieving ~98% coverage.
- Adding BDD using pytest-bdd (feature files + step definitions).
- Implementing TDD cycles:
  - RED → failing test
  - GREEN → implement feature
  - REFACTOR → improve the code
- Example: adding `completed` field, toggle completion, reopening tasks.

### Learning Outcomes

- Structure unit tests using pytest and fixtures.
- Apply BDD to define behaviours using Given–When–Then.
- Follow the TDD cycle to safely develop new features.
- Interpret and improve test coverage results.
- Build confidence through automated regression checking.

## 7. Code Quality, Formatting, Linting & CI (step31–step34)

### Key Concepts

- Installing and using **Black** for auto-formatting.
- Enforcing formatting rules in a GitHub Actions CI workflow.
- Installing and configuring **Ruff** for linting.
- Demonstrating failing/working CI behaviour.
- Automating code quality checks.

### Learning Outcomes

- Maintain consistent code style using Black.
- Use Ruff to detect unused imports, errors, and violations.
- Configure GitHub Actions to run automated quality checks.
- Understand how CI supports professional software development.

## Overall Learning Outcomes (step01–step34)

By completing the full project, students will be able to:

- Build a complete Flask web application from scratch.
- Apply secure forms, authentication, and CSRF protection.
- Model data using SQLAlchemy ORM.
- Implement scalable architecture using the factory pattern.
- Write unit tests, BDD scenarios, and follow TDD.
- Use linters, formatters, and CI tools to ensure software quality.
- Apply SQA principles across the full SDLC.
