# Flask Auth Backend

## Setup
1. Copy `.env.example` to `.env`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python -m app.main`

## API Endpoints
- POST `/api/auth/register` - Register new user
- POST `/api/auth/login` - Login user
- POST `/api/auth/logout` - Logout user (requires JWT)
- GET `/api/auth/me` - Get current user (requires JWT)
