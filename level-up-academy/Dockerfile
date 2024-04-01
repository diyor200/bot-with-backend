FROM python:3.10-slim AS build

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY level-up-academy/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Use a smaller base image for the runtime
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the dependencies installation from the previous build stage
COPY --from=build /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application code from the previous build stage
COPY --from=build /app .

# Set the entry point
CMD ["python3", "level-up-academy/level_up_academy/manage.py", "runserver", "0.0.0.0:8001"]