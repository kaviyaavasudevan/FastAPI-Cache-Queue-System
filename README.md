# FastAPI-Cache-Queue-System
A distributed backend system using Redis caching, Kafka event streaming, and CDN edge caching to build a high-performance, scalable API architecture.

I have used:

Redis for caching
Kafka for event-driven messaging
Cloudflare CDN for edge caching
FastAPI for backend APIs

This project simulates above architecture systems reduce latency, decouple services, and handle large-scale traffic efficiently.

Features:
Redis Caching
- Stores frequently accessed product data
- Reduces database/API response time
- Implements TTL-based cache expiry

Kafka Event Streaming
- Publishes events on product access
- Enables async processing (analytics, logging, notifications)
- Decouples services for scalability

CDN Integration (Cloudflare)
- Caches API responses at edge locations
- Reduces latency for global users
- Improves response time significantly

FastAPI Backend
- Lightweight and high-performance REST APIs
- Handles caching + event publishing logic
- Clean separation of concerns

Run Locally

Start infrastructure 
docker-compose up -d

Install dependencies
pip install -r requirements.txt

Run FastAPI server
uvicorn app.main:app --reload

Run Kafka consumer
python worker/consumer.py

CDN Setup

Deploy backend (Render / Railway / VPS)
Add domain to Cloudflare
Enable caching rules

Author
Built as a learning project to understand caching, messaging queues, and distributed system design in modern backend engineering.
