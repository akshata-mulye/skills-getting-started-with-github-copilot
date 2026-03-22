# Backend Test Suite

This directory contains backend tests for the FastAPI application.

## Structure
- `conftest.py`: Shared fixtures and state reset for in-memory activities
- `test_activities.py`: Tests for GET /activities
- `test_signup.py`: Tests for POST /signup
- `test_unregister.py`: Tests for POST /unregister

## Running Tests

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run all tests:
   ```
   pytest
   ```
3. Run with coverage:
   ```
   pytest --cov=src --cov-report=html
   ```
4. View coverage report:
   - Open `htmlcov/index.html` in your browser

## Notes
- Tests reset the in-memory database before each test for isolation.
- All endpoints and error cases are covered.
