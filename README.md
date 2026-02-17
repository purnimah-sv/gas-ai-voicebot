# gas-ai-voicebot
gas-ai-voicebot/
│
├── backend/
│   ├── app.py
│   ├── rag_engine.py
│   ├── voice_pipeline.py
│   ├── exotel_webhook.py
│   ├── embeddings.py
│   ├── config.py
│   ├── requirements.txt
│
├── training/
│   ├── expand_dataset.py
│   ├── finetune_prepare.py
│   ├── generate_qa.py
│
├── data/
│   ├── corpus.json
│   ├── qa_dataset.json
│   ├── bilingual.json
│
├── vector_db/
│   ├── ingest.py
│   ├── query.py
│
├── monitoring/
│   ├── metrics.py
│   ├── logs.py
│
├── ui/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│
├── ivr/
│   ├── call_flow.yaml
│
└── README.md
