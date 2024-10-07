# Frontend - Chatbot AI Application

## Project Overview

The frontend of the Chatbot AI application is built with **Next.js** and utilizes **TypeScript** for type safety. This application provides an interactive interface where users can communicate with the AI chatbot, upload documents for processing, and view messages in real time. It is styled using **Tailwind CSS** to ensure a responsive and modern design.

## Project Structure

```
app
├── components
│   ├── ChatBot.tsx
│   ├── ChatInput.tsx
│   └── Message.tsx
├── fonts
│   ├── GeistMonoVF.woff
│   └── GeistVF.woff
├── globals.css
├── layout.tsx
└── page.tsx
├── Dockerfile
├── next.config.mjs
├── next-env.d.ts
├── package.json
├── package-lock.json
├── postcss.config.mjs
├── README.md
├── tailwind.config.ts
└── tsconfig.json
```

### Explanation of Key Directories:
- **components**: Includes reusable components for the chatbot, including `ChatBot`, `ChatInput`, and `Message` components for managing chat messages.
- **fonts**: Contains custom font files used in the application.
- **globals.css**: Global CSS styles are defined here.
- **Dockerfile**: Docker configuration for containerization.

## Setup and Installation

### Prerequisites

Ensure you have **Node.js** and **Docker** installed on your machine.

### Steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vireshkumarmistry/rag-chatbot
   cd rag-chatbot/client/
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   ```

## Running the Application

### Option 1: Using Docker

1. **Build Docker Image:**

   ```bash
   docker build -t client .
   ```

2. **Run the Application in Docker:**

   ```bash
   docker run -p 3000:3000 client
   ```

3. **Access the Application:**

   Open `http://localhost:3000` in your web browser.

### Option 2: Local Development

1. **Start the Application Locally:**

   ```bash
   npm run dev
   ```

2. **Access the Application:**

   Open `http://localhost:3000` in your web browser.

## Configuration
### Tailwind CSS Configuration

- You can customize Tailwind CSS styles in the `tailwind.config.ts` file. This file allows you to extend or override default Tailwind settings.

## Troubleshooting

- **CORS Issues:** Ensure that the backend CORS settings allow requests from the frontend URL (`http://localhost:3000`).
- **TypeScript Errors:** Ensure that all required types are defined correctly in your TypeScript files.
- **Build Errors:** If using Docker, confirm that the Dockerfile is set up correctly and that all dependencies are installed.
- **File Upload Issues:** Check the file type and size restrictions when uploading documents. Ensure that the server is configured to handle the uploaded files correctly.
