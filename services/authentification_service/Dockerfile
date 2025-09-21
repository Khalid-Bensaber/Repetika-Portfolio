FROM python:3.11-slim

RUN groupadd -r user-app && useradd -r -g user-app -u 1000 user-app

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /venv \
 && /venv/bin/pip install --no-cache-dir -r requirements.txt \
 && chown -R user-app:user-app /venv
 
COPY --chown=user-app:user-app . .

COPY --chown=user-app:user-app entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER user-app

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["/entrypoint.sh"]
