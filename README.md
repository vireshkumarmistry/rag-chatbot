

### Docker Compose

---

# Docker Compose - ChatBot Application

## Running Both Services Together

To run both the server and client services together using Docker Compose:

1. **Build and Start Containers:**

   ```bash
   docker-compose up --build
   ```

2. **Access Services:**

   - **Frontend:** `http://localhost:3000`
   - **Backend:** `http://localhost:8000`

## Cleaning Up

To stop and remove containers:

```bash
docker-compose down
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
