# Restaurant Hub

A modern web application for restaurant management with a beautiful UI, custom fonts, and responsive design.

## Overview

Restaurant Hub is a full-stack application built with Next.js and Django, providing a comprehensive solution for restaurant management. It features a beautifully designed frontend for customers and a powerful backend for restaurant owners.

## Features

- Modern, responsive UI with custom fonts
- Menu management
- Chef profiles
- About section
- Contact information
- Blog functionality
- Testimonial showcase

## Project Structure

The project is organized as a monorepo using pnpm workspaces:

```
restaurant-hub/
├── apps/
│   ├── api/                   # Django backend
│   │   ├── config/            # Django project settings
│   │   ├── restaurant_api/    # Django app for restaurant functionality
│   │   ├── prisma/            # Prisma schema for database management
│   │   └── scripts/           # Utility scripts
│   ├── docs/                  # Documentation
│   │   └── chef-website-template/ # Original template reference
│   └── web/                   # Next.js frontend
│       ├── app/               # Next.js app directory
│       ├── components/        # React components
│       ├── lib/               # Utility functions
│       └── public/            # Static assets including fonts
├── package.json               # Root package.json
└── pnpm-workspace.yaml        # Workspace configuration
```

## Technologies Used

### Frontend
- Next.js 13+ (App Router)
- React
- Tailwind CSS
- Custom fonts (Emblema One and Poppins)
- TypeScript

### Backend
- Django
- Django REST Framework
- Prisma (for database interactions)
- SQLite (development) / PostgreSQL (production)

## Getting Started

### Git Repository Configuration

This project may contain nested Git repositories. If you encounter the following warning:

```
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
```

You have two options:

1. **Convert to a Git submodule** (Recommended if you need to track the nested repo separately):
   ```bash
   git rm --cached apps/web  # Remove the inner repo from Git tracking
   git submodule add <url> apps/web  # Add as proper submodule
   ```

2. **Remove the nested .git directory** (Recommended for a single unified repository):
   ```bash
   rm -rf apps/web/.git  # On macOS/Linux
   # OR
   rmdir /s /q apps\web\.git  # On Windows
   ```

   Then add and commit the changes:
   ```bash
   git add apps/web
   git commit -m "Remove nested git repository, combine into single repo"
   ```

### Prerequisites

- Node.js (v18+)
- pnpm (v8+)
- Python (v3.10+)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sisovin/restaurant-hub.git
   cd restaurant-hub
   ```

2. Install frontend dependencies:
   ```bash
   pnpm install
   ```

3. Set up the backend:
   ```bash
   cd apps/api
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   cd apps/api
   python manage.py migrate
   ```

5. Load initial data (optional):
   ```bash
   python manage.py loaddata initial_data
   ```

### Running the Development Environment

1. Start the backend:
   ```bash
   cd apps/api
   # On Windows:
   .\autoStart.bat
   # Or manually:
   python manage.py runserver
   ```

2. Start the frontend:
   ```bash
   cd apps/web
   pnpm dev
   ```

3. Open your browser and navigate to [http://localhost:3000](http://localhost:3000)

## Custom Fonts Implementation

This project uses custom fonts that are implemented as follows:

1. Font files are stored in `/apps/web/public/fonts/`:
   - EmblemaOne-Regular.ttf
   - Poppins-Regular.ttf
   - Poppins-Medium.ttf
   - Poppins-SemiBold.ttf

2. Font declarations are in `/apps/web/app/fonts.css`:
   ```css
   @font-face {
     font-family: 'Emblema One';
     src: url('/fonts/EmblemaOne-Regular.ttf') format('truetype');
     /* ... other properties ... */
   }
   
   @font-face {
     font-family: 'Poppins';
     src: url('/fonts/Poppins-Regular.ttf') format('truetype');
     /* ... other properties ... */
   }
   ```

3. Tailwind configuration in `/apps/web/tailwind.config.ts` includes the custom fonts:
   ```js
   fontFamily: {
     heading: ['"Emblema One"', 'system-ui', 'sans-serif'],
     body: ['"Poppins"', 'sans-serif'],
   }
   ```

4. Usage in components:
   ```jsx
   <h1 className="font-heading">Heading Text</h1>
   <p className="font-body">Body text</p>
   ```

## API Documentation

The backend provides a RESTful API for the frontend to consume. The API endpoints are:

- `GET /api/menu/` - Get all menu items
- `GET /api/chefs/` - Get all chef profiles
- `POST /api/contact/` - Submit a contact form
- And more...

Full API documentation is available at [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) when the backend is running.

## Deployment

### Frontend Deployment

The Next.js frontend can be deployed to Vercel:

```bash
cd apps/web
vercel
```

### Backend Deployment

The Django backend can be deployed to platforms like Heroku, AWS, or DigitalOcean:

```bash
# Example for Heroku
cd apps/api
heroku create
git push heroku main
heroku run python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- UI design inspiration from [HTML Codex](https://htmlcodex.com)
- Font files from [Google Fonts](https://fonts.google.com/)