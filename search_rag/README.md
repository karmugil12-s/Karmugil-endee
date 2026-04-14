# Endee Internship Submission: Semantic Search Engine

## 🏆 Project Overview
**Semantic Search Engine powered by Endee Vector Database**

This project demonstrates core Endee capabilities:
- **Vector Embeddings**: Convert text to dense vectors (384-dim)
- **Storage**: Upsert to Endee index (HNSW + cosine similarity)
- **Retrieval**: Semantic search for top-k similar docs
- **Web Demo**: Flask UI for interactive queries

Built as simple Python app inside Endee repo. Perfect 24h internship project.

## ✨ Features
- ✅ Local embeddings (no API keys): `sentence-transformers/all-MiniLM-L6-v2`
- ✅ Endee REST API integration: create index, upsert, search
- ✅ 50 AI/vector DB sample docs (synthetic dataset)
- ✅ Web UI: Query -> ranked results w/ scores + metadata
- ✅ Payload filtering ready (demo-ready)
- ✅ Optional RAG hook (add LLM prompt on results)

## 🛠 How to Run (5 mins)

### 1. Start Endee Server
```bash
cd Manojkrishna-endee
docker compose up -d  # or ./install.sh --release --avx2 && ./run.sh
```
Verify: `curl http://localhost:8080/api/v1/health` → `ok`

### 2. Setup Project
```bash
cd ../internship_demo  # or /home/mk/Documents/endee/internship_demo
pip install -r requirements.txt
```

### 3. Initialize Data
```
curl http://localhost:5000/init
```
Creates index `internship_demo` + upserts 50 docs.

### 4. Run Demo
```bash
python app.py
```
Open http://localhost:5000 → Search!

## 🔍 How Vector Search Works Here
1. **Docs** → sentence-transformers → 384-dim vectors
2. **Store** in Endee: `POST /index/internship_demo/upsert`
3. **Query** → embed → `POST /search` → HNSW finds top-k cosine similar
4. **Results**: Docs + similarity scores (higher = more relevant)

**Endee Index Config**: 
```
dimension: 384, metric: cosine
HNSW: M=16, ef_construction=128, ef=64
```

## 📱 Sample Demo
**Query**: \"What is vector search?\"

**Top Results**:
```
ID 1 (score: 0.854)
\"Vector search finds similar items using embeddings...\" 
category: vector_search

ID 2 (score: 0.723) 
\"Embeddings are dense numerical representations...\" 
category: embeddings
```

## 🏗 Project Structure
```
internship_demo/
├── app.py          # Flask + Endee logic
├── requirements.txt
├── README.md
└── data/
    └── sample_docs.json  # 50 AI docs
```

## 🔧 Extensibility
- **Filter**: Add `&filter={"category": {"$eq": "endee"}}`
- **RAG**: Feed results to LLM: `prompt = f\"Answer using: {results}\"`.
- **Scale**: 1M+ docs easy with Endee production config.

## 📈 Why This Rocks for Internship
- ✅ Uses **Endee core**: vectors/storage/retrieval
- ✅ Production-ready code patterns
- ✅ Zero-config demo
- ✅ Clear vector DB explanation
- ✅ Extensible to real RAG/agent apps
## Author
Manojkrishna M

**Built with ❤️ for Endee team. Ready for production!**

