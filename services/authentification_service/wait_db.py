import os, socket, time, sys
h = os.getenv("POSTGRES_HOST", "postgres").strip()
p = int(os.getenv("POSTGRES_PORT", "5432").strip())
for i in range(60):
    try:
        socket.getaddrinfo(h, p)                    # DNS ready
        s = socket.create_connection((h, p), 2)     # TCP ready
        s.close()
        sys.exit(0)
    except Exception:
        time.sleep(1)
print(f"DB not reachable: {h}:{p}", file=sys.stderr)
sys.exit(1)
