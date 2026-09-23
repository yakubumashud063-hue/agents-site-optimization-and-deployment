FarmFresh — Flask-based farm produce e-commerce

What this repo contains
- A Flask storefront (app.py) with templates in /templates and static assets in /static
- JSON-backed data files (products.json, users.json, orders.json) for simple demo persistence

Quick start (local development)
1. Create a virtual environment and activate it:
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # PowerShell on Windows

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app locally (development):
   python app.py
   Then open http://127.0.0.1:5000

Production deployment (Render, Heroku, etc.)
- This project includes a Procfile and runtime.txt to support typical PaaS deployments (Heroku/Render).
- Recommended: use a production WSGI server (gunicorn) which is included in requirements.

Render deployment (quick notes):
1. Create a new Web Service on Render and connect your GitHub repo.
2. Set the build command: pip install -r requirements.txt
3. Start command: gunicorn --bind 0.0.0.0:$PORT app:app
4. Add any environment variables via the Render dashboard (e.g., SECRET_KEY). For simple demos the app uses an internal secret.

Heroku deployment (quick notes):
1. heroku create
2. git push heroku main
3. heroku ps:scale web=1

Payment integration
- The repository currently implements a clean checkout flow with payment option selection (card vs cash). No live payment gateway keys are stored here.
- For production card payments, integrate a provider like Stripe: keep keys in environment variables, use Stripe's server-side SDK and client checkout flows, and test with sandbox keys before going live.

Next recommended steps
- Replace the development secret key in app.py with an environment-driven SECRET_KEY and remove any test/demo data before public launch.
- Trim any remaining legacy audit files if you want a minimal repository; these files were added during cleanup and review and can be archived elsewhere.
- (Optional) Add GitHub Actions to build and run tests or deploy on push.

Contact / notes
If you want, deploy the app now to Render or Heroku and I can help add live payment (Stripe checkout) and finalize the cleanup of legacy assets.
