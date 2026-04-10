FROM python:3.11-slim

# Utilisateur non-root requis par HF Spaces
RUN useradd -m -u 1000 user
USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR /home/user/app

# Installation des dépendances
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du projet
COPY --chown=user . .

EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
