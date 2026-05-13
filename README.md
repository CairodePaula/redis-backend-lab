# Redis Lab 🧠

Projeto completo com:
- Cache com Redis (TTL 30s)
- Fila (LPUSH / BRPOP)
- Rate limit por IP
- Contador global
- FastAPI + Worker + Docker

---

## 🚀 Como rodar

```bash
docker compose up --build
```

---

## 📌 Endpoints

### Cache
```
GET /cache/{x}
```

- 1ª chamada: MISS (lento)
- 2ª chamada: HIT (rápido)

---

### Fila
```
POST /queue
Body: "job1"
```

Worker processa em background.

---

### Rate limit
```
GET /count
```

Máx: 10 req/min por IP

---

## 🧱 Arquitetura

API → Redis → Worker

---

## 📦 Stack
- FastAPI
- Redis
- Docker Compose

---

## 👨‍💻 Autor

Desenvolvido por Cairo

